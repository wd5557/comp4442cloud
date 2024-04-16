import sys
import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("generator").getOrCreate()

args = sys.argv
input_filePath = args[1]
output_filePath = args[2]

df = spark.read.csv(input_filePath, header=False)

column_names = [
    "driverID", "carPlateNumber", "Latitude", "Longitude", "Speed", "Direction",
    "siteName", "Time", "isRapidlySpeedup", "isRapidlySlowdown", "isNeutralSlide",
    "isNeutralSlideFinished", "neutralSlideTime", "isOverspeed", "isOverspeedFinished",
    "overspeedTime", "isFatigueDriving", "isHthrottleStop", "isOilLeak"
]

for i, col_name in enumerate(column_names):
    df = df.withColumnRenamed(f"_c{i}", col_name)

columns_to_cast = {
    "Speed": "int",
    "isNeutralSlide": "int",
    "isNeutralSlideFinished": "int",
    "neutralSlideTime": "int",
    "isOverspeed": "int",
    "isOverspeedFinished": "int",
    "overspeedTime": "int",
    "isFatigueDriving": "int",
    "isHthrottleStop": "int",
    "isOilLeak": "int"
}

for col_name, col_type in columns_to_cast.items():
    df = df.withColumn(col_name, df[col_name].cast(col_type))

df = df.withColumn("unix_Time", F.unix_timestamp(F.col("Time"), 'yyyy-MM-dd HH:mm:ss'))

summary = df.groupBy("driverID", "carPlateNumber", "unix_Time").agg(
    F.avg(df["Speed"]).alias("Speed"),
    F.first(df['isOverspeed']).alias("isOverspeed")
)

summary = summary.na.fill(value=0, subset=["isOverspeed"])

driver_ids = summary.select("driverID").distinct().collect()

for driver in driver_ids:
    driver_id = driver.driverID
    driver_summary = summary.filter(summary.driverID == driver_id)
    driver_summary = driver_summary.coalesce(1)
    driver_path = os.path.join(output_filePath, driver_id)
    driver_summary.write.option("header", "true").csv(driver_path)

spark.stop()