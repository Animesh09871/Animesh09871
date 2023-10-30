from pyspark.sql.types import FloatType
from textblob import TextBlob
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
'''''''''
text = "I love this product! It's amazing."
blob = TextBlob(text)

# Analyze sentiment
sentiment = blob.sentiment
print(sentiment)  
'''''
if __name__ == "__main__":
    print('Streaming is started')

    # Create a SparkSession
    spark = SparkSession.builder.appName('stream').getOrCreate()

    # Read data from a socket
    stream_df = spark.readStream.format("socket") .option("host", "127.0.0.1") .option("port", 1400) .load()

    print(stream_df.isStreaming)
    stream_df.printSchema()
    def analyze_sentiment(text):
        analysis = TextBlob(text)
    analyze_sentiment_udf = udf(analyze_sentiment, StringType())

    # Apply sentiment analysis to the streaming data
    stream_df = stream_df.withColumn("sentiment", analyze_sentiment_udf(col("value")))

    # Start the streaming query and write to the console
    write_query = stream_df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    # Wait for the query to terminate
    write_query.awaitTermination()

    print('Streaming ended!')

