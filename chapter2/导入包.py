# 导入包
# 在 包中的 _init__.py 文件中暴露 需要往外使用的方法
import my_package

my_package.send_message.send("1111")
my_package.receive_message.receive()