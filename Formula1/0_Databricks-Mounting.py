# Databricks notebook source
display(dbutils.fs.mounts())

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

display(dbutils.fs.mounts())

# COMMAND ----------

display(dbutils.fs.ls("/mnt/raw"))

# COMMAND ----------

dbutils.fs.mount(  
  source = f"wasbs://stage@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/stage", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

dbutils.fs.mount(  
  source = f"wasbs://curated@{storage_account_name}.blob.core.windows.net", 
  mount_point =f"/mnt/curated", 
  extra_configs = {fullname : accountkey}) 

# COMMAND ----------

display(dbutils.fs.mounts())
