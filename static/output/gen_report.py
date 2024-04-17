import sys
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

df = df.withColumn("Time", F.to_timestamp(F.col("Time"), "yyyy-MM-dd HH:mm:ss"))

summary = df.groupBy("driverID", "carPlateNumber", F.to_date("Time").alias("Date")).agg(
    F.sum("isOverspeed").alias("number_of_overspeed"),
    F.sum("overspeedTime").alias("total_overspeed"),
    F.sum("isFatigueDriving").alias("number_of_fatigueDriving"),
    F.sum("isNeutralSlide").alias("number_of_neutralSlide"),
    F.sum("neutralSlideTime").alias("total_neutralSlideTime"),
    F.avg("Speed").alias("average_speed")
).orderBy("Date")

summary.write.mode("overwrite").option("header", "true").csv(output_filePath)
spark.stop()