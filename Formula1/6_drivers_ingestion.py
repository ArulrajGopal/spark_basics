# Databricks notebook source
# MAGIC %run ./1_common

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from pyspark.sql.functions import concat, col,lit

# COMMAND ----------

name_schema = StructType(fields=[StructField("forename", StringType(), True),
                                 StructField("surname", StringType(), True)

])
drivers_schema = StructType(fields=[StructField("driverId", IntegerType(), False),
                                    StructField("driverRef", StringType(), True),
                                    StructField("number", IntegerType(), True),
                                    StructField("code", StringType(), True),
                                    StructField("name", name_schema),
                                    StructField("dob", DateType(), True),
                                    StructField("nationality", StringType(), True),
                                    StructField("url", StringType(), True)  

])

# COMMAND ----------

drivers_df = spark.read \
    .format("json")\
    .schema(drivers_schema)\
    .load(f'/mnt/raw/drivers.json')

# COMMAND ----------

drivers_df.display()

# COMMAND ----------

final_df = drivers_df.withColumn("name", concat(col("name.forename"), lit(" "), col("name.surname")))\
    .drop("url")

# COMMAND ----------

final_df.write\
    .format('csv')\
    .mode('overwrite')\
    .option("path","/mnt/stage/drivers")\
    .saveAsTable('stage.drivers')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from stage.drivers

# COMMAND ----------


