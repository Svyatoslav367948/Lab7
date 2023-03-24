import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data2(1).csv", encoding='windows-1251') as r_file:
    incl_col = [3]
    data2 = []
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        col = list(row[i] for i in incl_col)
        data2.append(col)
    time = []
    PDZ = []
    PDZnor = []
    max = 0
    count = 0
    for i in range(7186):
        if count == 0:
            count += 1
        else:
            if float(data2[i][0]) > max: max = float(data2[i][0])
            PDZ.append(float(data2[i][0]))
            # print(max)

    koef = max / 100
    for i in range(7185):
        PDZnor.append(PDZ[i] / koef)
    f_std = np.std(PDZnor)
    print("Отклонение")
    print(f_std)
    fig, (axs, axs2) = plt.subplots(1, 2)

    axs.hist(PDZ, bins=20)
    axs2.hist(PDZnor, bins=20)

    axs.set_facecolor('lightyellow')
    axs2.set_facecolor('lightyellow')

    fig.set_facecolor('aqua')
    fig.set_figwidth(11)  # ширина
    fig.set_figheight(5)  # высота
    plt.show()