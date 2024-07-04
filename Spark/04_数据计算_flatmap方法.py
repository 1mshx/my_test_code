from pyspark import SparkConf, SparkContext
import os

# 设置python解释器
os.environ['PYSPARK_PYTHON'] = "D:/Python/python.exe"

# 创建环境
conf = SparkConf().setMaster('local[*]').setAppName('test')
sc = SparkContext(conf=conf)

# 准备一个RDD
lst = [[1, 2, [3,4,5]], [2, 3, 4], [3, 4, 5]]
st = ['itheima itcast 666', 'itheima itheima itcast', 'python itheima']
rdd = sc.parallelize(lst)
rdd2 = sc.parallelize(st)

# 进行转换
rdd1 = rdd.map(lambda x: x)
rdd5 = rdd.flatMap(lambda x: x)
rdd3 = rdd2.flatMap(lambda x: x.split(" "))
rdd4 = rdd2.map(lambda x: x.split(" "))

# 输出结果
print(rdd1.collect())
print(rdd5.collect())
print(rdd3.collect())
print(rdd4.collect())

# 关闭连接
sc.stop()
