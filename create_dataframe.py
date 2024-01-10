
data = [
    ("John", 28, "New York"),
    ("Jane", 24, "San Francisco"),
    ("Bob", 22, "Los Angeles"),
    ("Alice", 30, "Chicago")
]

columns = ["Name", "Age","City" ]


df = spark.createDataFrame(data, columns)


df.show()
