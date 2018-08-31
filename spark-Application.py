import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
'''
we will be using netcat to receive data from our localmachine,
nc -l 9999, this is will open a session on port 9999 to send data.
'''
if __name__ == "__main__":
#sys.argv expects 3 arguments
	if len(sys.argv) != 3:
		print ("usage spark-submit spark-Application.py <hostname> <port>")
		exit(-1)
	#first argument is the host
	host = sys.argv[1] 
	#second argument is the port, we will cast it to int.
	port = int (sys.argv[2])
# Move to build a spark session.
	spark = SparkSession\
			.builder\
			.appName("netcatWordCount")\
			.getOrCreate()

	#suppresing the log level to ERROR
	spark.sparkContext.setLogLevel("ERROR")

	lines = spark\
	.readStream\
	.format('socket')\
	.option('host',host)\
	.option('port',port)\
	.load()

#new data will be updated in 'lines' and we will perform operations on it.
	words = lines.select(
		explode(
			split(lines.value, ' ')
			).alias('word')#word,name of column in dataframe
		)
	wordCounts = words.groupBy('word')\
					.count()
	query = wordCounts.writeStream\
					  .outputMode('complete')\
					  .format('console')\
					  .start()
	query.awaitTermination()
