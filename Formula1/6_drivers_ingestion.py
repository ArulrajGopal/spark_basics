# Databricks notebook source
# MAGIC %run ./1_Functions

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

container_name = 'raw'
file_name = 'drivers.json'

drivers_df = spark.read \
.schema(drivers_schema) \
.json(f"abfss://{container_name}@adls9867external.dfs.core.windows.net/{file_name}")

# COMMAND ----------

final_df = drivers_df.withColumn("name", concat(col("name.forename"), lit(" "), col("name.surname")))

# COMMAND ----------

final_df.write\
    .format('delta')\
    .mode('overwrite')\
    .option("path","abfss://stage@adls9867external.dfs.core.windows.net/drivers")\
    .saveAsTable('formulaone.stage.drivers')

# COMMAND ----------



# COMMAND ----------


