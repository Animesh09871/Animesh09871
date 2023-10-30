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
     StructField("company",StringType(), True),
     StructField("body style",StringType(), True),
     StructField("length",IntegerType(), True),
     StructField("engine",StringType(), True),
     StructField("mileage",IntegerType(), True),
     StructField("sunroof",StringType(), True),

    ])


