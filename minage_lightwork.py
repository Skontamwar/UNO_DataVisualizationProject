import pandas as pd
from matplotlib import pyplot as plt


def show_graph_1(fsize, color):
    plt.rcParams["figure.autolayout"] = True
    columns = ["minage_light_leg_12"]
    df = pd.read_csv("childlabour_6Feb2019CSVversion.csv", usecols=columns)
    cl = ['green', 'red', 'gray']  # default

    if color == 0:
        cl = ['green', 'red', 'gray']  # default
    elif color == 1:
        cl = ['#004C83', '#A27A01', '#7D7D7D']  # deuteranopia

    a = df.minage_light_leg_12.to_list()
    b = [0, 0, 0]  # counters for yes, no and unknown
    for i in range(len(a)):
        if a[i] == 'Yes':
            b[0] += 1
        elif a[i] == 'No':
            b[1] += 1
        else:
            b[2] += 1

    c = ['Yes', 'No', 'Unknown']
    plt.bar(c, b, color=cl)

    plt.rcParams["figure.figsize"] = [10.00, 8.00]
    plt.xticks(fontsize=fsize)
    plt.yticks(fontsize=fsize)
    plt.xlabel('Minimum Working Age', fontsize=fsize + 10)
    plt.show()
