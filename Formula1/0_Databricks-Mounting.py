# Databricks notebook source
dbutils.fs.ls("dbfs:/")

# COMMAND ----------

storage_account_name = "sparkdemostorageaccount"  
accountkey= "ha8V0wsWYgj55/w7EMvwczPxDmcLXkKkkSN0+w0bMu9r/mDn0X4olKKim4Vw29S3Wgu3EA3UKwJD+AStVfFw7g=="  
container_name = "raw"
fullname = "fs.azure.account.key." +storage_account_name+ ".blob.core.windows.net"


dbutils.fs.mount(  
  source = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/{container_name}", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

dbutils.fs.ls("dbfs:/")

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/mnt/"))

# COMMAND ----------

display(dbutils.fs.ls("dbfs:/mnt/raw/"))

# COMMAND ----------


