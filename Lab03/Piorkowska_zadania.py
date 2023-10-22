import matplotlib.pyplot as plt
import numpy as np

def zadanie_1():
    # Czerwony wykres kropkowany
    std_dev = 1.0
    mean = 0.0
    x = np.arange(-5, 5, 0.1)
    f = (1/(std_dev*np.sqrt(np.pi)))*np.exp((-(x-mean)**2)/(2*std_dev))

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
    plt.plot(x, f_3, 'xk')
    plt.show()

def main():
    zadanie_1()


if __name__ == "__main__":
    main()