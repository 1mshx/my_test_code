from pyspark import SparkConf, SparkContext
import os

# 设置python解释器
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

# 创建环境
conf = SparkConf().setMaster('local[*]').setAppName('test')
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5, 6])


# 通过map方法把每个元素乘以10
def func(data):
    return data * 10


rdd2 = rdd.map(func)
rdd3 = rdd.map(lambda x: 5 * x)
rdd4 = rdd.map(lambda x: 5 + x).map(lambda x: x * 10)

# 查看结果
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())


# 关闭连接
sc.stop()
