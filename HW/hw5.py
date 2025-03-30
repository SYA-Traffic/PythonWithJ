import matplotlib.pyplot as plt
import numpy as np

# 定义x的范围
x1 = np.linspace(0, 8, 800)
x2 = np.linspace(0, 8, 800)

# 计算y值
t1 = 1.4 + 0.8 * x1
t2 = 3.7 + 0.3 * x2

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制两条线
plt.plot(x1, t1, label='t1 = 1.4 + 0.8x1', color='blue')
plt.plot(x2, t2, label='t2 = 3.7 + 0.3x2', color='red')

# 添加水平线 y=3.77
plt.axhline(y=3.77, color='green', linestyle='--', label='y = 3.77')

# 计算交点
intersection_x1 = (3.77 - 1.4) / 0.8
intersection_y1 = 3.77

intersection_x2 = (3.77 - 3.7) / 0.3
intersection_y2 = 3.77

# 绘制垂直虚线到交点
plt.axvline(x=intersection_x1, ymin=0, ymax=intersection_y1/10, color='purple', linestyle=':')
plt.axvline(x=intersection_x2, ymin=0, ymax=intersection_y2/10, color='orange', linestyle=':')

# # 标注交点
# plt.text(intersection_x1, intersection_y1 + 0.1, f'({intersection_x1:.3f}, {intersection_y1:.3f})',
#          verticalalignment='bottom', horizontalalignment='right',
#          color='purple', fontsize=10, backgroundcolor='white')
# plt.text(intersection_x2, intersection_y2 + 0.1, f'({intersection_x2:.3f}, {intersection_y2:.3f})',
#          verticalalignment='bottom', horizontalalignment='left',
#          color='orange', fontsize=10, backgroundcolor='white')
#
# 在横轴和纵轴上标注交点的数值
plt.scatter([intersection_x1, intersection_x2], [0, 0], color=['purple', 'orange'], zorder=5)
plt.text(intersection_x1, -0.2, f'{intersection_x1:.3f}',
         verticalalignment='top', horizontalalignment='center',
         color='purple', fontsize=10, backgroundcolor='white')
plt.text(intersection_x2, -0.2, f'{intersection_x2:.3f}',
         verticalalignment='top', horizontalalignment='center',
         color='orange', fontsize=10, backgroundcolor='white')

# plt.scatter([0, 0], [intersection_y1, intersection_y2], color=['purple', 'orange'], zorder=5)
plt.text(-0.1, intersection_y1-0.6, f'{intersection_y1:.3f}',
         verticalalignment='bottom', horizontalalignment='right',
         color='purple', fontsize=10, backgroundcolor='white')
# plt.text(-0.2, intersection_y2, f'{intersection_y2:.3f}',
#          verticalalignment='bottom', horizontalalignment='left',
#          color='orange', fontsize=10, backgroundcolor='white')

# 设置坐标轴范围从0开始
plt.xlim(0, 10)
plt.ylim(0, 10)

# 添加标题和标签
# plt.title('Plot of Two Equations and Horizontal Line with Vertical Intersections')
plt.xlabel('Volume(in thousand)')
plt.ylabel('Travel Time(min)')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 展示图形
plt.show()
