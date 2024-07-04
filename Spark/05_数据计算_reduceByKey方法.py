from pyspark import SparkConf, SparkContext
import os

# 设置python解释器
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

# 创建环境
conf = SparkConf().setMaster('local[*]').setAppName('test')
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('a', 1), ('a', 1), ('b', 1), ('b', 2)])

# 进行转换
rdd1 = rdd.reduceByKey(lambda x, y: x + y)

# 输出结果
print(rdd1.collect())

# 关闭连接
sc.stop()
