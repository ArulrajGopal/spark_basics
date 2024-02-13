-- Databricks notebook source
CREATE DATABASE IF NOT EXISTS stage

-- COMMAND ----------

CREATE DATABASE IF NOT EXISTS curated

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS stage.circuits(
  circuit_id INT,
  circuitref STRING,
  name STRING,
  location STRING,
  country STRING,
  lat Double,
  lng Double,
  alt int
)
using parquet
options (
  'path' '/mnt/stage/circuits'
)
