# simple wordcount example with apahce spark structured streaming

## Usage

### Data 
* from netcat utility on linux terminal.

'''
nc -l 9999
'''

![netcat session on linux terminal](/images/netcat.png)

### Run spark job with spark-submit <appname> <host> <port>
'''
spark-submit spark-Application.py localhost 9999
'''
![spark-streaming-job](/images/spark-stream.png)
