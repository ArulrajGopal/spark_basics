-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS stage

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS curated

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS stage.circuits(
  circuit_id Integer,
  circuitref STRING,
  name STRING,
  location STRING,
  country STRING,
  lat Double,
  lng Double,
  alt int,
  loaded_time timestamp
)
using parquet
options (
  'path' '/mnt/stage/circuits'
)

-- COMMAND ----------


