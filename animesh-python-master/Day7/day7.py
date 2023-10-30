from pyspark.sql import SparkSession
from pyspark.sql.types import *
if __name__=="__main__":
    print('Data ingestion from local system started...')

    spark=SparkSession.builder.appName('File').getOrCreate()

    input_csv_schema=StructType([
     StructField("company",StringType(), True),
     StructField("body style",StringType(), True),
     StructField("length",IntegerType(), True),
     StructField("engine",StringType(), True),
     StructField("mileage",IntegerType(), True),
     StructField("sunroof",StringType(), True),

    ])
stream_df=spark.readStream.format("csv").option("header","true") .schema(input_csv_schema).load(path="/home/ubuntu/Downloads/d")

stream_df .printSchema()

stream_df_query= stream_df.writeStream.format("console").start()

stream_df_query.awaitTermination()

print('scaning closed')


