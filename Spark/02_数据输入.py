from pyspark import SparkConf, SparkContext
import warnings

# 过滤警告
warnings.filterwarnings("ignore")

# 创建基础环境
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 传入数据
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize((1, 2, 3, 4, 5))
rdd3 = sc.parallelize({1, 2, 3, 4, 5})
rdd4 = sc.parallelize('ab,cdefg')
rdd5 = sc.parallelize({'a': 111, 'b': 222})

# 查看rdd内容
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

# # 通过textFile方法，读取文件数据加载到Spark内，成为RDD对象
# rdd = sc.textFile(r'D:\OneDrive\桌面\2015.csv')
#
# # 查看rdd内容
# print(rdd.collect())

# 关闭连接
sc.stop()

