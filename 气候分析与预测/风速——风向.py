import matplotlib.pyplot as plt
import pandas as pd
from numpy import *
# import npx
# import sys
# sys.modules["multibox_target"]
#
# npx.multibox_target()
# 读取excel数据为dataframe
table = pd.read_excel("weatherData.xlsx", keep_default_na=False)
# 按城市获得风速数据
speed1 = table.iloc[0:8759]["WIND-AVG-SPEED"]
speed2 = table.iloc[8759:8759 * 2]["WIND-AVG-SPEED"]
speed3 = table.iloc[8759 * 2: 8759 * 3]["WIND-AVG-SPEED"]
speed4 = table.iloc[8759 * 3: 8759 * 4]["WIND-AVG-SPEED"]
speed5 = table.iloc[8759 * 4: 8759 * 5]["WIND-AVG-SPEED"]
speed6 = table.iloc[8759 * 5: 8759 * 6]["WIND-AVG-SPEED"]
speed7 = table.iloc[8759 * 6: 8759 * 7]["WIND-AVG-SPEED"]
speed8 = table.iloc[8759 * 7: 8759 * 8]["WIND-AVG-SPEED"]
# 按城市获得风向数据
direction1 = table.iloc[0:8759]["WIND-DIRECTION"]
direction2 = table.iloc[8759:8759 * 2]["WIND-DIRECTION"]
direction3 = table.iloc[8759 * 2: 8759 * 3]["WIND-DIRECTION"]
direction4 = table.iloc[8759 * 3: 8759 * 4]["WIND-DIRECTION"]
direction5 = table.iloc[8759 * 4: 8759 * 5]["WIND-DIRECTION"]
direction6 = table.iloc[8759 * 5: 8759 * 6]["WIND-DIRECTION"]
direction7 = table.iloc[8759 * 6: 8759 * 7]["WIND-DIRECTION"]
direction8 = table.iloc[8759 * 7: 8759 * 8]["WIND-DIRECTION"]


# 函数处理表格中的空格
def deal(a):
    list1 = a.tolist()
    list2 = []
    for i in range(len(list1)):
        if list1[i] != '':
            list2.append(list1[i])
            a = pd.Series(list2)
    return a


# 创建图形对象
# fig, axes = plt.subplots(2, 4)
# plt.ylim(-10, 25)
# plt.xlim(1, 12)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 数据处理总函数，求出每个月风速风向的平均值之后，运用plt画图，并设置图形属性
def plot_figure(a, b, x, y, name):
    title = name
    speed_1 = a.iloc[0:743]
    speed_2 = a.iloc[743:1415]
    speed_3 = a.iloc[1415:2159]
    speed_4 = a.iloc[2159:2879]
    speed_5 = a.iloc[2879:3623]
    speed_6 = a.iloc[3623:4343]
    speed_7 = a.iloc[4343:5087]
    speed_8 = a.iloc[5087:5831]
    speed_9 = a.iloc[5831:6551]
    speed_10 = a.iloc[6551:7295]
    speed_11 = a.iloc[7295:8015]
    speed_12 = a.iloc[8015:8715]

    direction_1 = b.iloc[0:743]
    direction_2 = b.iloc[743:1415]
    direction_3 = b.iloc[1415:2159]
    direction_4 = b.iloc[2159:2879]
    direction_5 = b.iloc[2879:3623]
    direction_6 = b.iloc[3623:4343]
    direction_7 = b.iloc[4343:5087]
    direction_8 = b.iloc[5087:5831]
    direction_9 = b.iloc[5831:6551]
    direction_10 = b.iloc[6551:7295]
    direction_11 = b.iloc[7295:8015]
    direction_12 = b.iloc[8015:8759]

    speed_1 = deal(speed_1)
    speed_2 = deal(speed_2)
    speed_3 = deal(speed_3)
    speed_4 = deal(speed_4)
    speed_5 = deal(speed_5)
    speed_6 = deal(speed_6)
    speed_7 = deal(speed_7)
    speed_8 = deal(speed_8)
    speed_9 = deal(speed_9)
    speed_10 = deal(speed_10)
    speed_11 = deal(speed_11)
    speed_12 = deal(speed_12)
    direction_1 = deal(direction_1)
    direction_2 = deal(direction_2)
    direction_3 = deal(direction_3)
    direction_4 = deal(direction_4)
    direction_5 = deal(direction_5)
    direction_6 = deal(direction_6)
    direction_7 = deal(direction_7)
    direction_8 = deal(direction_8)
    direction_9 = deal(direction_9)
    direction_10 = deal(direction_10)
    direction_11 = deal(direction_11)
    direction_12 = deal(direction_12)

    mean_speed_1 = mean(speed_1)
    mean_speed_2 = mean(speed_2)
    mean_speed_3 = mean(speed_3)
    mean_speed_4 = mean(speed_4)
    mean_speed_5 = mean(speed_5)
    mean_speed_6 = mean(speed_6)
    mean_speed_7 = mean(speed_7)
    mean_speed_8 = mean(speed_8)
    mean_speed_9 = mean(speed_9)
    mean_speed_10 = mean(speed_10)
    mean_speed_11 = mean(speed_11)
    mean_speed_12 = mean(speed_12)
    mean_direction_1 = mean(direction_1)
    mean_direction_2 = mean(direction_2)
    mean_direction_3 = mean(direction_3)
    mean_direction_4 = mean(direction_4)
    mean_direction_5 = mean(direction_5)
    mean_direction_6 = mean(direction_6)
    mean_direction_7 = mean(direction_7)
    mean_direction_8 = mean(direction_8)
    mean_direction_9 = mean(direction_9)
    mean_direction_10 = mean(direction_10)
    mean_direction_11 = mean(direction_11)
    mean_direction_12 = mean(direction_12)

    mean_speed_month = [mean_speed_1, mean_speed_2, mean_speed_3, mean_speed_4, mean_speed_5, mean_speed_6,
                        mean_speed_7, mean_speed_8,
                        mean_speed_9, mean_speed_10, mean_speed_11, mean_speed_12]
    mean_direction_month = [mean_direction_1, mean_direction_2, mean_direction_3, mean_direction_4, mean_direction_5,
                            mean_direction_6, mean_direction_7, mean_direction_8,
                            mean_direction_9, mean_direction_10, mean_direction_11, mean_direction_12]
    month = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    plt.plot(mean_direction_month, mean_speed_month, marker=".")
    for i in range(12):
        plt.text(mean_direction_month[i], mean_speed_month[i], month[i], fontsize=6)
    plt.xlabel('平均风向/deg')
    plt.ylabel('平均风速/(m/s)')
    plt.title(title + "风速_风向关系")
    plt.show()


plot_figure(speed1, direction1, 0, 0, "MINNEAPOLIS")
plot_figure(speed2, direction2, 0, 1, 'OKLAHOMA')
plot_figure(speed3, direction3, 0, 2, 'KANSAS')
plot_figure(speed4, direction4, 0, 3, 'DENVER')
plot_figure(speed5, direction5, 1, 0, 'NASHVILLE')
plot_figure(speed6, direction6, 1, 1, 'ATLANTA')
plot_figure(speed7, direction7, 1, 2, 'LAS_VEGAS')
plot_figure(speed8, direction8, 1, 3, 'CHICAGO')

