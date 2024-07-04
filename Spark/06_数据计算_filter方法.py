from pyspark import SparkConf, SparkContext
import os

# 设置python解释器
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

# 创建环境
conf = SparkConf().setMaster('local[*]').setAppName('test')
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

# 进行过滤
rdd1 = rdd.filter(lambda x: x % 2 == 0)

# 输出结果
print(rdd1.collect())

# 关闭连接
sc.stop()
