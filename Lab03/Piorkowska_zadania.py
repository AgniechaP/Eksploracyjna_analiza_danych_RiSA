import matplotlib.pyplot as plt
import numpy as np
import requests
import json
import random


def zadanie_1():
    # Czerwony wykres kropkowany
    std_dev = 1.0
    mean = 0.0
    x = np.arange(-5, 5, 0.1)
    f = (1 / (std_dev * np.sqrt(np.pi))) * np.exp((-(x - mean) ** 2) / (2 * std_dev))

    std_dev_2 = 2
    mean_2 = -2
    f_2 = (1 / (std_dev_2 * np.sqrt(np.pi))) * np.exp((-(x - mean_2) ** 2) / (2 * std_dev_2))

    std_dev_3 = 3
    mean_3 = 3
    f_3 = (1 / (std_dev_3 * np.sqrt(np.pi))) * np.exp((-(x - mean_3) ** 2) / (2 * std_dev_3))

    std_dev_4 = 4
    mean_4 = 4
    f_4 = (1 / (std_dev_4 * np.sqrt(np.pi))) * np.exp((-(x - mean_4) ** 2) / (2 * std_dev_4))

    plt.plot(x, f, 'or')
    plt.plot(x, f_2, ':b')
    plt.plot(x, f_3, '--g')
    plt.plot(x, f_4, 'xk')
    plt.show()


def zadanie_2():
    fig, ax = plt.subplots()
    ax.set_title('Rozkład Gaussa', fontsize=16)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    std_dev = 1.0
    mean = 0.0
    x = np.arange(-5, 5, 0.1)
    f = (1 / (std_dev * np.sqrt(np.pi))) * np.exp((-(x - mean) ** 2) / (2 * std_dev))

    std_dev_2 = 2
    mean_2 = -2
    f_2 = (1 / (std_dev_2 * np.sqrt(np.pi))) * np.exp((-(x - mean_2) ** 2) / (2 * std_dev_2))

    std_dev_3 = 3
    mean_3 = 3
    f_3 = (1 / (std_dev_3 * np.sqrt(np.pi))) * np.exp((-(x - mean_3) ** 2) / (2 * std_dev_3))

    std_dev_4 = 4
    mean_4 = 4
    f_4 = (1 / (std_dev_4 * np.sqrt(np.pi))) * np.exp((-(x - mean_4) ** 2) / (2 * std_dev_4))

    plt.plot(x, f, 'or', label=f'$\sigma$ = {std_dev}, $\mu$  = {mean}')
    plt.plot(x, f_2, ':b', label=f'$\sigma$ = {std_dev_2}, $\mu$  = {mean_2}')
    plt.plot(x, f_3, '--g', label=f'$\sigma$ = {std_dev_3}, $\mu$  = {mean_3}')
    plt.plot(x, f_4, 'xk', label=f'$\sigma$ = {std_dev_4}, $\mu$  = {mean_4}')

    ax.legend(loc='upper left')
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(0, 1.2, 0.2))
    ax.set_xticklabels(ax.get_xticks(), rotation=45)
    ax.grid(color='k', linestyle='-', linewidth=0.1)
    plt.show()


def zadanie_3_and_4():
    url = "https://jug.dpieczynski.pl/lab-ead/_resources/lab_03/cancer_survival_in_us.json"
    req = requests.get(f"{url}")
    data = json.loads(req.text)

    label_axis = []

    fig, ax = plt.subplots()
    for label in data['age_groups']:
        label_name = label['age']
        label_axis.append(label_name)

    male_survivors = []
    female_survivors = []
    for survivor in data['age_groups']:
        male_survivor_number = survivor['male_survivors']
        female_survivor_number = survivor['female_survivors']

        male_survivors.append(male_survivor_number)
        female_survivors.append(female_survivor_number)

    x = np.arange(len(male_survivors))
    width = 0.3

    ax.bar(x - width / 2, male_survivors, width, label='Man')
    ax.errorbar(x - width / 2, male_survivors, yerr=random.uniform(0.01, 0.9), fmt='.k', capsize=2)
    ax.bar(x + width / 2, female_survivors, width, label='Woman')
    ax.errorbar(x + width / 2, female_survivors, yerr=random.uniform(0.03, 0.7), fmt='.k', capsize=2)
    ax.set_xticks(x)
    ax.set_xticklabels(label_axis, rotation=90)

    y_ticks = ax.get_yticks()
    y_labels = [f"{int(label)}%" for label in y_ticks]
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)
    ax.set_axisbelow(True)
    ax.grid(axis='y', linewidth=0.2, color='gray', linestyle='solid')
    ax.legend(loc='upper left')
    plt.show()
    print(male_survivors)


def main():
    # zadanie_1()
    # zadanie_2()
    zadanie_3_and_4()


if __name__ == "__main__":
    main()
