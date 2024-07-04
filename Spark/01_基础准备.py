# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# setMaster()设置运行模式，setAppName()设置任务名字

# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行(停止PySpark程序)
sc.stop()
