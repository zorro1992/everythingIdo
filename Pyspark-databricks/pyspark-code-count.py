#The code basically is searching for the the transcation section and counting the transcation done via visa Credit_Card_Type
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.conf import SparkConf
action1 = spark.read.option("header", "true").option("delimiter", ",").csv("/FileStore/tables/MOCK_DATA__1__copy_2-64854.csv")
action1.where(action1.Credit_Card_Type == "visa").count()
