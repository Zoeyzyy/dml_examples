import numpy as np
import matplotlib.pyplot as plt

# 生成 10 个随机数作为示例数据
A = [295381520.0, 293754404.0, 293589628.0, 293530260.0, 293344916.0, 293075588.0, 297021388.0, 294449060.0, 299148500.0, 296824692.0]
B = [279414356.0, 280289512.0, 275068260.0, 269601604.0, 269174900.0, 268497236.0, 270431764.0, 278969172.0, 277994668.0, 273610414.0]

# 创建一个包含 10 个子图的图像
fig, axs = plt.subplots(2, 5, figsize=(15, 6))

# 遍历 A 和 B 列表中的值，绘制矩阵图
for i, (a, b) in enumerate(zip(A, B)):
    row = i // 5
    col = i % 5

    # 创建一个 2x2 的矩阵，对角线元素为0，其他元素根据A[i]和B[i]确定
    matrix = np.array([[0, a], [b, 0]])

    # 绘制矩阵图
    axs[row, col].matshow(matrix, cmap='Blues')

    # 添加标题
    axs[row, col].set_title(f'Epoch {i+1}')

    # 隐藏坐标轴
    axs[row, col].axis('off')

plt.tight_layout()
plt.savefig("TM.png")

