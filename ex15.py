# Read files

# Using argv to read filename from users

#从sys module导入argv功能
from sys import argv

#利用argvuoqu用户输入它想要打开的文件名
script, filename = argv

# !!! Function: open (). Exp.: open(filename, mode ='r')
# mode = 'r' : open for reading
# mode = 'w' : open for writing, truncating the file first
# mode = 'x' : create a new file and open it for writing
# mode = 'a' : open for writing, appending to the end of the file if it exists
# mode = 'b' : binary Mode
# mode = 't' : text mode (default)
# mode = '+' : open a disk file for updating (reading and writing)
# Intact: open(filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


# 打开文件名为filename的文件，并把他赋值给txt变量
txt = open(filename)
#打印打开的文件名，并在字符串中插入变量
print(f"Here is your file {filename}:")
# 利用.read命令来读取变量txt的字符串
print(txt.read())
txt.close()
print(txt.read())

# Using input () to read filename
print("Type the filename again:")
#使用input 函数来让用户输入它想要打开的文件的名字，并把它赋值给变量
file_again = input(">")
#使用open 函数打开文件，赋值给变量
txt_again = open(file_again)
#读取txt_again的字符串内容，并打印
print(txt_again.read())
txt_again.close()

# Notes
# Step1: Using import argv or input() to understand which file the user want to open
# Steo2: Using open () to list the content of the file to a variable
# Step3: Using     .read   to read and display the content.
