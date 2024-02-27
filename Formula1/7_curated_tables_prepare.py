# Databricks notebook source
from pyspark.sql.functions import col

# COMMAND ----------

races_df = spark.read.table('Stage.races')
circuits_df = spark.read.table('Stage.circuits')
drivers_df = spark.read.table('stage.drivers')
results_df = spark.read.table('stage.results')

# COMMAND ----------

races_circuits_joined_df = races_df.alias("LH") .join(circuits_df.alias("RH"),
                col("LH.circuitId") == col("RH.circuitId"),'left')\
                .select(col("LH.raceId"),col("LH.year"),col("RH.name").alias("circuit_name"),col("RH.location"))

# COMMAND ----------

races_circuits_joined_df.display()

# COMMAND ----------

results_drivers_joined_df = results_df.alias("LH") .join(drivers_df.alias("RH"),
                col("LH.driverId") == col("RH.driverId"),'left')\
                .select(col("LH.raceId"),col("LH.points"),col("RH.name").alias("driver_name"))

# COMMAND ----------

results_drivers_joined_df.display()

# COMMAND ----------

races_circuits_joined_df.write\
                .format('csv')\
                .mode('overwrite')\
                .option("path","/mnt/curated/races_circuits")\
                .saveAsTable('curated.races_circuits')

# COMMAND ----------

results_drivers_joined_df.write\
                .format('csv')\
                .mode('overwrite')\
                .option("path","/mnt/curated/results_drivers")\
                .saveAsTable('curated.results_drivers')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from curated.races_circuits

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from curated.results_drivers

# COMMAND ----------


