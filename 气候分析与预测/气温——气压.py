import matplotlib.pyplot as plt
import pandas as pd
from numpy import *

table = pd.read_excel("C:\\Users\\33668\\Desktop\\气象数据分析\\weatherData.xlsx", keep_default_na=False)
# 按城市读取气温数据
tem0 = table.iloc[0:8759]["TEMPERATURE"]
tem1 = table.iloc[8759:8759 * 2]["TEMPERATURE"]
tem2 = table.iloc[8759 * 2: 8759 * 3]["TEMPERATURE"]
tem3 = table.iloc[8759 * 3: 8759 * 4]["TEMPERATURE"]
tem4 = table.iloc[8759 * 4: 8759 * 5]["TEMPERATURE"]
tem5 = table.iloc[8759 * 5: 8759 * 6]["TEMPERATURE"]
tem6 = table.iloc[8759 * 6: 8759 * 7]["TEMPERATURE"]
tem7 = table.iloc[8759 * 7: 8759 * 8]["TEMPERATURE"]
# 按城市读取气压数据
pre1 = table.iloc[0:8759]["PRESSURE"]
pre2 = table.iloc[8759:8759 * 2]["PRESSURE"]
pre3 = table.iloc[8759 * 2: 8759 * 3]["PRESSURE"]
pre4 = table.iloc[8759 * 3: 8759 * 4]["PRESSURE"]
pre5 = table.iloc[8759 * 4: 8759 * 5]["PRESSURE"]
pre0 = table.iloc[8759 * 5: 8759 * 6]["PRESSURE"]
pre6 = table.iloc[8759 * 6: 8759 * 7]["PRESSURE"]
pre7 = table.iloc[8759 * 7: 8759 * 8]["PRESSURE"]


# 处理表格中的空值
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


# 数据处理总函数，求出气温气压的平均值之后，运用plt画图，并设置图形属性
def plot_figure(a, b, x, y, name):
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

    pre_1 = b.iloc[0:743]
    pre_2 = b.iloc[743:1415]
    pre_3 = b.iloc[1415:2159]
    pre_4 = b.iloc[2159:2879]
    pre_5 = b.iloc[2879:3623]
    pre_6 = b.iloc[3623:4343]
    pre_7 = b.iloc[4343:5087]
    pre_8 = b.iloc[5087:5831]
    pre_9 = b.iloc[5831:6551]
    pre_10 = b.iloc[6551:7295]
    pre_11 = b.iloc[7295:8015]
    pre_12 = b.iloc[8015:8759]

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

    pre_1 = deal(pre_1)
    pre_2 = deal(pre_2)
    pre_3 = deal(pre_3)
    pre_4 = deal(pre_4)
    pre_5 = deal(pre_5)
    pre_6 = deal(pre_6)
    pre_7 = deal(pre_7)
    pre_8 = deal(pre_8)
    pre_9 = deal(pre_9)
    pre_10 = deal(pre_10)
    pre_11 = deal(pre_11)
    pre_12 = deal(pre_12)

    mean_tem_1 = mean(tem_1)
    mean_tem_2 = mean(tem_2)
    mean_tem_3 = mean(tem_3)
    mean_tem_4 = mean(tem_4)
    mean_tem_5 = mean(tem_5)
    mean_tem_6 = mean(tem_6)
    mean_tem_7 = mean(tem_7)
    mean_tem_8 = mean(tem_8)
    mean_tem_9 = mean(tem_9)
    mean_tem_10 = mean(tem_10)
    mean_tem_11 = mean(tem_11)
    mean_tem_12 = mean(tem_12)
    mean_pre_1 = mean(pre_1)
    mean_pre_2 = mean(pre_2)
    mean_pre_3 = mean(pre_3)
    mean_pre_4 = mean(pre_4)
    mean_pre_5 = mean(pre_5)
    mean_pre_6 = mean(pre_6)
    mean_pre_7 = mean(pre_7)
    mean_pre_8 = mean(pre_8)
    mean_pre_9 = mean(pre_9)
    mean_pre_10 = mean(pre_10)
    mean_pre_11 = mean(pre_11)
    mean_pre_12 = mean(pre_12)

    mean_tem_month = [mean_tem_1, mean_tem_2, mean_tem_3, mean_tem_4, mean_tem_5, mean_tem_6, mean_tem_7, mean_tem_8,
                      mean_tem_9, mean_tem_10, mean_tem_11, mean_tem_12]
    mean_pre_month = [mean_pre_1, mean_pre_2, mean_pre_3, mean_pre_4, mean_pre_5, mean_pre_6, mean_pre_7, mean_pre_8,
                      mean_pre_9, mean_pre_10, mean_pre_11, mean_pre_12]
    month = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    # plt.plot(x, y)
    plt.plot(mean_pre_month, mean_tem_month, marker=".")
    for i in range(12):
        plt.text(mean_pre_month[i], mean_tem_month[i], month[i], fontsize=6, rotation=-90)
    plt.xlabel('平均气压/(10Pa)')
    plt.ylabel('平均气温/℃')
    # name.set_xticks(range(1004, 1024, 4))
    # name.set_xlim(1004, 1024)
    # name.set_ylim(-10, 35)
    # name.set_yticks(range(-10, 35, 5))
    plt.title(title + "气温_气压关系")
    plt.show()


plot_figure(tem0, pre0, 0, 0, "MINNEAPOLIS")
plot_figure(tem1, pre1, 0, 1, 'OKLAHOMA')
plot_figure(tem2, pre2, 0, 2, 'KANSAS')
plot_figure(tem3, pre3, 0, 3, 'DENVER')
plot_figure(tem4, pre4, 1, 0, 'NASHVILLE')
plot_figure(tem5, pre5, 1, 1, 'ATLANTA')
plot_figure(tem6, pre6, 1, 2, 'LAS_VEGAS')
plot_figure(tem7, pre7, 1, 3, 'CHICAGO')
