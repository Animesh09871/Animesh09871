import csv
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import *

Hr=pd.read_csv('HR_Hiring_details_transaction.csv')
columns_to_drop = ['Candidate_Ref', 'Duration_to_accept_offer','Age','LOB_Id','Domicile_Id','Location_ID','Rex_in_Yrs','Postal_Code','Notice_Period','DOJ_Extended']
Hr = Hr.drop(columns=columns_to_drop, axis=1)
Hr.to_csv('amended_HR_Hiring_details.csv', index=False)
print(Hr)

if __name__=="__main__":
    print('Data ingestion from local system started...')

    spark=SparkSession.builder.appName('File').getOrCreate()

    input_csv_schema=StructType([
     StructField("Sno",IntegerType(), True),
     StructField("ected_in_CTCPercent_hike_exp",IntegerType(), True),
     StructField("Percent_hike_offered_in_CTC",IntegerType(), True),
     StructField("Gender",StringType(), True),
     StructField("Percent_difference_CTC",IntegerType(), True),
     StructField("Candidate_Source",StringType(), True),

    ])

stream_df=spark.readStream.format("csv").option("header","true") .schema(input_csv_schema).load(path="/home/ubuntu/Downloads/d")

stream_df .printSchema()

stream_df_query= stream_df.writeStream.format("console").start()

stream_df_query.awaitTermination()

print('scaning closed')
