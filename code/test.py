import os

from dotenv import load_dotenv

from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

load_dotenv("/opt/spark/env/minio-local.env")

s3_url: str = os.getenv("MINIO_URL")
s3_access_key: str = os.getenv("MINIO_ACCESS_KEY")
s3_secret_key: str = os.getenv("MINIO_SECRET_KEY")

conf = SparkConf()

conf.set("spark.hadoop.fs.s3a.endpoint", s3_url)
conf.set("spark.hadoop.fs.s3a.access.key", s3_access_key)
conf.set("spark.hadoop.fs.s3a.secret.key", s3_secret_key)
conf.set("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
conf.set("spark.hadoop.fs.s3a.path.style.access", "true")
conf.set(
    "spark.jars",
    "/opt/spark/driver/hadoop-aws-3.3.4.jar,/opt/spark/driver/aws-java-sdk-bundle-1.12.262.jar",
)


spark = (
    SparkSession.builder.appName("spark-standalone-minio")
    .config(conf=conf)
    .getOrCreate()
)

spark.range(10).write.mode("overwrite").parquet("s3a://lakehouse/abc")
