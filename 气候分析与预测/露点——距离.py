import matplotlib.pyplot as plt
import pandas as pd
from numpy import *

table = pd.read_excel("C:\\Users\\33668\\Desktop\\气象数据分析\\weatherData.xlsx", keep_default_na=False)


def year_dewp(table):
    dewp_MINNEAPOLIS = []
    dewp_OKLAHOMA = []
    dewp_KANSAS = []
    dewp_DENVER = []
    dewp_NASHVILLE = []
    dewp_ATLANTA = []
    dewp_LAS_VEGAS = []
    dewp_CHICAGO = []

    # 按城市读取露点数据
    for i in range(0, 8759):
        dewp_MINNEAPOLIS.append(table.iloc[i]["DEWP"])
    for i in range(8759, 8759 * 2):
        dewp_OKLAHOMA.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 2, 8759 * 3):
        dewp_KANSAS.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 3, 8759 * 4):
        dewp_DENVER.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 4, 8759 * 5):
        dewp_NASHVILLE.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 5, 8759 * 6):
        dewp_ATLANTA.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 6, 8759 * 7):
        if table.iloc[i]["DEWP"] != '':
            dewp_LAS_VEGAS.append(table.iloc[i]["DEWP"])
    for i in range(8759 * 7, 8759 * 8):
        dewp_CHICAGO.append(table.iloc[i]["DEWP"])


    avg_dewp_CHICAGO = mean(dewp_CHICAGO)
    avg_dewp_MINNEAPOLIS = mean(dewp_MINNEAPOLIS)
    avg_dewp_OKLAHOMA = mean(dewp_OKLAHOMA)
    avg_dewp_KANSAS = mean(dewp_KANSAS)
    avg_dewp_DENVER = mean(dewp_DENVER)
    avg_dewp_ATLANTA = mean(dewp_ATLANTA)
    avg_dewp_NASHVILLE = mean(dewp_NASHVILLE)
    avg_dewp_LAS_VEGAS = mean(dewp_LAS_VEGAS)

    data1 = [['MINNEAPOLIS', avg_dewp_MINNEAPOLIS], ['DENVER', avg_dewp_DENVER], ['CHICAGO', avg_dewp_CHICAGO],
             ['OKLAHOMA', avg_dewp_OKLAHOMA], ['KANSAS', avg_dewp_KANSAS], ['ATLANTA', avg_dewp_ATLANTA],
             ['LAS_VEGAS', avg_dewp_LAS_VEGAS], ['NASHVILLE', avg_dewp_NASHVILLE]]
    data2 = [['MINNEAPOLIS', 1269], ["OKLAHOMA", 778], ["KANSAS", 1073], ["DENVER", 1335], ["NASHVILLE", 663],
             ["ATLANTA", 376],
             ["LAS_VEGAS", 364], ["CHICAGO", 1153]]
    year_avg_tem = pd.DataFrame(data1, columns=['city', 'avg_dewp'])
    distance = pd.DataFrame(data2, columns=['city', 'distance'])
    link = pd.merge(year_avg_tem, distance)
    link = link.sort_values(by=["distance"])  # 得到列属性为城市，露点，距离的dataframe
    x = []
    y = []
    z = []

    for i in range(8):
        x.append(link.iloc[i]["distance"])
        y.append(link.iloc[i]["avg_dewp"])
        z.append(link.iloc[i]["city"])

    # 设置图形属性
    plt.plot(x, y)
    for i in range(8):
        plt.text(x[i], y[i], z[i], fontsize=7)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.ylabel('年平均露点/℃')
    plt.xlabel('离海距离/km')
    # plt.xticks(range(300, 1500, 100))
    # plt.yticks(range(-2, 14, 2))
    plt.title("8大城市露点_距离关系")
    plt.show()


year_dewp(table)
