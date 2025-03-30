import numpy as np
import matplotlib.pyplot as plt

# 定义二次方程的系数
a = 1.1
b = -4.21
c = 14.82

# 计算与y轴的交点 (x=0)
y_intercept = c

# 计算抛物线的顶点 (最小值点)
vertex_x = -b / (2 * a)
vertex_y = a * vertex_x**2 + b * vertex_x + c

# 创建x的数据范围
x = np.linspace(-5, 10, 400)

# 计算对应的y值
y = a * x**2 + b * x + c

# 创建图形和轴对象
fig, ax = plt.subplots()

# 绘制二次方程曲线
ax.plot(x, y, label='t = 1.1x^2 - 4.21x + 14.82')

# 标注y轴截距
ax.scatter(0, y_intercept, color='red')
ax.annotate(f'y={y_intercept:.2f}', xy=(0.9, y_intercept-4), xytext=(-20, 20),
            textcoords='offset points')

# # 标注顶点
ax.scatter(vertex_x, vertex_y, color='green')
ax.annotate(f'({vertex_x:.2f}, {vertex_y:.2f})', xy=(vertex_x, vertex_y), xytext=(20, -20),
            textcoords='offset points')

# 在顶点处画一条虚线到x轴，并标注交点
ax.axvline(x=vertex_x, ymin=2/30, ymax=vertex_y/45, linestyle='--', color='gray')
ax.scatter(vertex_x, -0.2, color='blue')
ax.annotate(f'x={vertex_x:.2f}', xy=(vertex_x+0.2, -0.3), xytext=(0, -20),
            textcoords='offset points')

# 设置图形属性
ax.set_xlabel('Volume(in thousand)')
ax.set_ylabel('Travel Time(min)')
ax.legend(loc='upper right')
ax.grid(True)

# 设置原点为 (0, 0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 显示图形
# plt.title('Plot of the quadratic equation and its key points')
plt.xlim(-5, 10)
plt.ylim(-5, 60)
plt.show()



