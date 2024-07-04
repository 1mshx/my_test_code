from pyspark import SparkConf, SparkContext
import os

# 设置python解释器
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"
os.environ['HADOOP_HOME'] = "D:/BigData/hadoop-3.3.5"

# 创建环境
conf = SparkConf().setMaster('local[*]').setAppName('test').set('spark.default.parallelism', '1')
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('a', 11, '你好'), ('b', 22, '你也好'), ('c', 33, 'python'), ('d', 44, 'ithma')])
rdda = sc.parallelize([1, 2, 3, 4, 5], 1)

# 排序
rdd1 = rdd.sortBy(lambda x: x[0], ascending=True, numPartitions=2)

# 输出结果
print(rdd1.collect())

# 输出到文件夹
rdd.saveAsTextFile('D:/my_code/Spark/Output')

# 关闭连接
sc.stop()
