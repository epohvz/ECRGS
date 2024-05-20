import numpy as np
import matplotlib.pyplot as plt

# 给定的数据点
x = np.array([15, 20, 25, 30, 35, 40, 45, 50])
y = np.array([73.1, 72.62, 72.7, 72.8, 72.1, 71.6, 71.7, 71.5])

# 创建一个新的图形窗口
plt.figure()

# 画出折线图
plt.plot(x, y, 'o-', color="#c64328", markerfacecolor='white', markersize=10, linewidth=3, label = "Citeseer")
plt.tick_params(axis='both', labelsize=20)  # 设置刻度标签的字体大小为14

# 设置坐标轴的范围
plt.xlim(10, 55)
plt.ylim(71, 73.5)


# plt.legend(loc='best')  # 'best' 会让 matplotlib 自动选择一个不碍事的位置来显示图例

plt.legend(fontsize=20, loc='best')       # 直接设置图例字体大小为14
# 显示网格线
plt.grid(True)

plt.savefig('k_1.svg', format='svg', bbox_inches='tight')
