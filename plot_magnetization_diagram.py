import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 25})
plt.rcParams['font.family'] = 'Helvetica'

file_name = 'example.csv'

df = pd.read_csv(file_name)

image_data = df.to_numpy()

height = image_data.shape[0]  # Get the number of rows (height of the image)

start_index_1 = 4 * height // 6  # Calculate the starting index for the last third
start_index_2 = 5 * height // 6  # Calculate the starting index for the last third

# Crop the array to only include the last third
cropped_image_data_1 = image_data[start_index_1:start_index_2, :]
cropped_image_data_2 = image_data[start_index_2:,:]

sum = (cropped_image_data_1+cropped_image_data_2)/2

# Create a custom colormap that uses red for values near 0
cmap = plt.cm.get_cmap('RdBu')
cmap.set_bad(color='black')

# Now you can plot the last third of the image
plt.imshow(sum, cmap=cmap, vmin=-1, vmax=1)  # Using custom colormap

# 绘制图像
# plt.imshow(image_data, cmap='gray')  # 'gray'是颜色映射，适用于灰度图像
plt.colorbar(label='$M_z$')  # 显示颜色条
plt.axis('off')  # 不显示坐标轴
plt.savefig('example.png', dpi=300, bbox_inches='tight')
plt.show()
