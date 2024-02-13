# install pyspark
!pip install pyspark

from pyspark.sql import SparkSession

#create spark session
spark= SparkSession.builder.appName('mysparksession').getOrCreate()

#create spark context
sc = spark.sparkContext
