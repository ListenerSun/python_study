# 读取文件
# 方法一
file = open("readme.txt")
text = file.read()
print(text)
# 关闭文件
file.close()

# 方法二
file = open("readme.txt")
while True:
    text = file.readline()
    if not text:
        break
    print(text)


# 关闭文件
file.close()

# 追加文件内容
f = open("readme.txt", "a")

f.write("hhahha",)
f.close()

# 文件复制
file = open("readme.txt")
file_copy = open("readme_copy.txt", "w+")
text = file.read()
file_copy.write(text)
file.close()
file_copy.close()
