import matplotlib.pyplot as plt
import pandas as pd
from numpy import *

table = pd.read_excel("C:\\Users\\33668\\Desktop\\气象数据分析\\weatherData.xlsx", keep_default_na=False)

# 按城市读取气温的数据
tem0 = table.iloc[0:8759]["TEMPERATURE"]
tem1 = table.iloc[8759:8759 * 2]["TEMPERATURE"]
tem2 = table.iloc[8759 * 2: 8759 * 3]["TEMPERATURE"]
tem3 = table.iloc[8759 * 3: 8759 * 4]["TEMPERATURE"]
tem4 = table.iloc[8759 * 4: 8759 * 5]["TEMPERATURE"]
tem5 = table.iloc[8759 * 5: 8759 * 6]["TEMPERATURE"]
tem6 = table.iloc[8759 * 6: 8759 * 7]["TEMPERATURE"]
tem7 = table.iloc[8759 * 7: 8759 * 8]["TEMPERATURE"]

# 创建2x4的图形对象


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 处理表格中的空值
def deal(a):
    list1 = a.tolist()
    list2 = []
    for i in range(len(list1)):
        if list1[i] != '':
            list2.append(list1[i])
            a = pd.Series(list2)
    return a

# 按月读取气温数据并求平均值
def plot_figure(a, x, y, name):
    title = name
    tem_1 = a.iloc[0:743]
    tem_2 = a.iloc[743:1415]
    tem_3 = a.iloc[1415:2159]
    tem_4 = a.iloc[2159:2879]
    tem_5 = a.iloc[2879:3623]
    tem_6 = a.iloc[3623:4343]
    tem_7 = a.iloc[4343:5087]
    tem_8 = a.iloc[5087:5831]
    tem_9 = a.iloc[5831:6551]
    tem_10 = a.iloc[6551:7295]
    tem_11 = a.iloc[7295:8015]
    tem_12 = a.iloc[8015:8759]

    tem_1 = deal(tem_1)
    tem_2 = deal(tem_2)
    tem_3 = deal(tem_3)
    tem_4 = deal(tem_4)
    tem_5 = deal(tem_5)
    tem_6 = deal(tem_6)
    tem_7 = deal(tem_7)
    tem_8 = deal(tem_8)
    tem_9 = deal(tem_9)
    tem_10 = deal(tem_10)
    tem_11 = deal(tem_11)
    tem_12 = deal(tem_12)

    mean_1 = mean(tem_1)
    mean_2 = mean(tem_2)
    mean_3 = mean(tem_3)
    mean_4 = mean(tem_4)
    mean_5 = mean(tem_5)
    mean_6 = mean(tem_6)
    mean_7 = mean(tem_7)
    mean_8 = mean(tem_8)
    mean_9 = mean(tem_9)
    mean_10 = mean(tem_10)
    mean_11 = mean(tem_11)
    mean_12 = mean(tem_12)
    mean_month = [mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8, mean_9, mean_10, mean_11, mean_12]
    month = range(1, 13, 1)
    temperature = range(-10, 40, 5)

    # 设置图例
    # name = axes[x, y]
    plt.xticks(month)
    plt.yticks(temperature)
    plt.plot(month, mean_month, marker=".")
    plt.xlabel('月份')
    plt.ylabel('平均气温/℃')
    plt.ylim(-10, 35)

    plt.title(title + "月均气温")
    plt.show();


plot_figure(tem0, 0, 0, "MINNEAPOLIS")
plot_figure(tem1, 0, 1, 'DENVER')
plot_figure(tem2, 0, 2, 'CHICAGO')
plot_figure(tem3, 0, 3, 'OKLAHOMA')
plot_figure(tem4, 1, 0, 'KANSAS')
plot_figure(tem5, 1, 1, 'ATLANTA')
plot_figure(tem6, 1, 2, 'LAS_VEGAS')
plot_figure(tem7, 1, 3, 'NASHVILLE')
