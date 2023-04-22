import matplotlib.pyplot as plt
import pandas as pd
from numpy import *

table = pd.read_excel("C:\\Users\\33668\\Desktop\\气象数据分析\\weatherData.xlsx", keep_default_na=False)


def year_temperature(table):
    tem_MINNEAPOLIS = []
    tem_OKLAHOMA = []
    tem_KANSAS = []
    tem_DENVER = []
    tem_NASHVILLE = []
    tem_ATLANTA = []
    tem_LAS_VEGAS = []
    tem_CHICAGO = []

    # 按城市读取气温数据
    for i in range(0, 8759):
        tem_MINNEAPOLIS.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759, 8759 * 2):
        tem_OKLAHOMA.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 2, 8759 * 3):
        tem_KANSAS.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 3, 8759 * 4):
        tem_DENVER.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 4, 8759 * 5):
        tem_NASHVILLE.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 5, 8759 * 6):
        tem_ATLANTA.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 6, 8759 * 7):
        if table.iloc[i]["TEMPERATURE"] != '':
            tem_LAS_VEGAS.append(table.iloc[i]["TEMPERATURE"])
    for i in range(8759 * 7, 8759 * 8):
        tem_CHICAGO.append(table.iloc[i]["TEMPERATURE"])


    avg_tem_CHICAGO = mean(tem_CHICAGO)
    avg_tem_MINNEAPOLIS = mean(tem_MINNEAPOLIS)
    avg_tem_OKLAHOMA = mean(tem_OKLAHOMA)
    avg_tem_KANSAS = mean(tem_KANSAS)
    avg_tem_DENVER = mean(tem_DENVER)
    avg_tem_ATLANTA = mean(tem_ATLANTA)
    avg_tem_NASHVILLE = mean(tem_NASHVILLE)
    avg_tem_LAS_VEGAS = mean(tem_LAS_VEGAS)

    data1 = [['MINNEAPOLIS', avg_tem_MINNEAPOLIS], ['DENVER', avg_tem_DENVER], ['CHICAGO', avg_tem_CHICAGO],
             ['OKLAHOMA', avg_tem_OKLAHOMA], ['KANSAS', avg_tem_KANSAS], ['ATLANTA', avg_tem_ATLANTA],
             ['LAS_VEGAS', avg_tem_LAS_VEGAS], ['NASHVILLE', avg_tem_NASHVILLE]]
    data2 = [['MINNEAPOLIS', 1269], ["OKLAHOMA", 778], ["KANSAS", 1073], ["DENVER", 1335], ["NASHVILLE", 663],
             ["ATLANTA", 376],
             ["LAS_VEGAS", 364], ["CHICAGO", 1153]]
    year_avg_tem = pd.DataFrame(data1, columns=['city', 'avg_tem'])
    distance = pd.DataFrame(data2, columns=['city', 'distance'])
    link = pd.merge(year_avg_tem, distance)
    link = link.sort_values(by=["distance"])  # 得到列属性为城市，距离，气温的dataframe

    x = []
    y = []
    z = []

    for i in range(8):
        x.append(link.iloc[i]["distance"])
        y.append(link.iloc[i]["avg_tem"])
        z.append(link.iloc[i]["city"])


    # 设置图形属性
    plt.plot(x, y)
    for i in range(8):
        plt.text(x[i], y[i], z[i], fontsize=7)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.ylabel('年平均气温')
    plt.xlabel('离海距离')
    plt.show()


print(year_temperature(table))
