from pyspark.sql import SparkSession
import os, sys
import pyspark.sql.functions as F

# file_name_list = ["detail_record_2017_01_{}_08_00_00.csv".format(str(i).zfill(2)) for i in range(2, 12)]


spark = SparkSession.builder.appName("generator").getOrCreate()

args = sys.args
input_filePath = args[1]
output_filePath = args[2]

df = spark.read.csv(input_filePath)

df = df.withColumnRenamed("_c0", "driverID") \
    .withColumnRenamed("_c1", "carPlateNumber") \
    .withColumnRenamed("_c2", "Latitude") \
    .withColumnRenamed("_c3", "Longtitude") \
    .withColumnRenamed("_c4", "Speed") \
    .withColumnRenamed("_c5", "Direction") \
    .withColumnRenamed("_c6", "siteName") \
    .withColumnRenamed("_c7", "Time") \
    .withColumnRenamed("_c8", "isRapidlySpeedup") \
    .withColumnRenamed("_c9", "isRapidlySlowdown") \
    .withColumnRenamed("_c10", "isNeutralSlide") \
    .withColumnRenamed("_c11", "isNeutralSlideFinished") \
    .withColumnRenamed("_c12", "neutralSlideTime") \
    .withColumnRenamed("_c13", "isOverspeed") \
    .withColumnRenamed("_c14", "isOverspeedFinished") \
    .withColumnRenamed("_c15", "overspeedTime") \
    .withColumnRenamed("_c16", "isFatigueDriving") \
    .withColumnRenamed("_c17", "isHthrottleStop") \
    .withColumnRenamed("_c18", "isOilLeak")

df = df.withColumn("Speed", df.Speed.cast('int'))
df = df.withColumn("isNeutralSlide", df.isOverspeed.cast('int'))
df = df.withColumn("isNeutralSlideFinished", df.isOverspeed.cast('int'))
df = df.withColumn("neutralSlideTime", df.isOverspeedFinished.cast('int'))
df = df.withColumn("isOverspeed", df.isOverspeed.cast('int'))
df = df.withColumn("isOverspeedFinished", df.isOverspeedFinished.cast('int'))
df = df.withColumn("overspeedTime", df.overspeedTime.cast('int'))
df = df.withColumn("isFatigueDriving", df.isFatigueDriving.cast('int'))
df = df.withColumn("isHthrottleStop", df.isHthrottleStop.cast('int'))
df = df.withColumn("isOilLeak", df.isOilLeak.cast('int'))

df = df.withColumn("Time", F.to_date(F.to_timestamp(F.col("Time"), 'yyyy-MM-dd HH:mm:ss')))

summary = df.groupBy("driverID", "carPlateNumber", "Time").sum("isOverspeed", "overspeedTime", "isFatigueDriving",
                                                               "isNeutralSlide", "neutralSlideTime").orderBy("Time")
summary = summary.withColumnRenamed("sum(isOverspeed)", "number_of_overspeed")
summary = summary.withColumnRenamed("sum(overspeedTime)", "total_overspeed")
summary = summary.withColumnRenamed("sum(isFatigueDriving)", "number_of_fatigueDriving")
summary = summary.withColumnRenamed("sum(isNeutralSlide)", "number_of_neutralSlide")
summary = summary.withColumnRenamed("sum(neutralSlideTime)", "total_neutralSlideTime")

summary.write.csv(output_filePath)