# 1. 赋值、变量与数据类型

## 整数
### 在Python中，你不需要显式地声明变量的类型。解释器会根据赋值自动推断类型。
### 例如将42赋值给a之后，内存中就存在a这个变量了，不需要提前声明有a这个变量
### 对比java中需要提前声明，类似下面两行
### int a;
### a = 42;
# 新增
a = 42
p = print
p(a)  # 输出: 42，print是python自带的方法，可以将入参打印在console控制台
## 浮点数
b = 3.14
print(b)  # 输出: 3.14

## 字符串
c = "Hello, World!"
print(c)  # 输出: Hello, World!

## 布尔值
d = True
print(d)  # 输出: True


# 2. 条件语句，解决如果xxx就执行xxx，否则执行xxx的情况
# 使用`if`, `elif`, 和 `else`关键字可以实现条件判断。
# 一般情况下代码中只出现if，当出现elif或else时，尽量重构，经验来看，只用if会极大降低出错概率，程序易于维护
age = 18
if age < 18:
    print("未成年")
elif age == 18:
    print("刚好成年")
else:
    print("成年人")

# 上方的可重构为
newAge = -1
if newAge < 18:
    print("未成年")
if age == 18:
    print("刚好成年")
if newAge > 18:
    print("成年人")
# 抛出异常值
try:
    if newAge < 0:
        raise ValueError("异常啦")
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)


# 3. 循环

## 支持`for`和`while`两种类型的循环。

# For循环，用于操作列表，将列表中的元素一个个拿出来进行处理

# 遍历列表中的元素，将列表中的信息打印到console
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While循环，数据分析可能比较常见，用于一直循环到满足某种条件

# 例子为，当count小于5时一直循环，直到 count >= 5 跳出循环
count = 0
while count < 5:
    print(count)
    count += 1 # 这个等同于 count = count + 1, 非常常见的写法


# 4. 函数定义，将一段固定的逻辑封装起来，减少重复代码，提高可读性

# 使用`def`关键字定义函数。
# 例如定义一个函数，计算一组数的标准差
def calculate_std_dev(data):
    n = len(data)
    # if n < 2:
    #     raise ValueError("The list must contain at least two values to compute the standard deviation.")

    mean = sum(data) / n
    sum_x = 0
    for x in data:
        sum_x = sum_x + (x - mean) ** 2
    try:
        var_value = sum_x/(n-1)
    except ZeroDivisionError as e:
        return None
    std_value = var_value ** 0.5

    # variance = sum((x - mean) ** 2 for x in data) / (n - 1)  # 使用n-1是为了得到样本标准差
    # std_dev = variance ** 0.5
    return std_value

# 示例数据
try:
    data_list = [1]
    std_dev = calculate_std_dev(data_list)
    print(f"手动计算的标准差: {std_dev}")
except ValueError as e:
    print(e)
# 如果使用numpy库，直接调用函数即可
import numpy as np

# 示例数据
data_list = [1,2,3,4,5]
std_dev = np.std(data_list, ddof=1)  # 设置ddof=1以获得样本标准差
print(f"使用numpy计算的标准差: {std_dev}")

### 5. 列表生成器，可以用for循环代替，先了解，熟练后尝试使用。
squares = [lambda x:x**2 for x in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

### 6. 异常处理，是为了让程序在出现异常时可以让我们通过代码处理，然后让代码继续执行

# 使用`try`, `except`, `finally`块来捕获并处理异常。
# 这个例子是在计算时，如果出现分母是0的时候打印日志，在数据分析中，经常用于循环计算一组数时，
# 在脏数据导致异常时进行处理，跳过这个脏数据继续处理后面的数据
try:
    result = 10 / 0
except ZeroDivisionError as e:
    # 这个ZeroDivisionError不是随便写的，这个是python中会抛出的异常，基本上抛出异常时都会有对应的异常名称
    print("错误："+str(e))
    print(f"错误: {e}")
finally:
    print("执行完毕")

# 如果不知道抛出的异常名字，可以直接捕获Exception
try:
    # 这里放置可能抛出异常的代码
    result = 10 / 0  # 这将抛出ZeroDivisionError
except Exception as e:
    # 捕获所有继承自Exception类的异常，并将异常对象赋值给变量e
    print(f"捕获到一个异常: {e}")
