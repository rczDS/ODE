import numpy as np
import matplotlib.pyplot as plt

def g(z1, z2):
    return z2, (1 - pow(z1, 2)) * z2 - z1

def k1(z1, z2):
    return g(z1, z2)

def k2(z1, z2, h):
    z1_, z2_ = g(z1, z2)
    return g(z1 + 2.0 * h * z1_ / 3.0, z2 + 2.0 * h * z2_ / 3.0)


def van_der_Pol(t_max, h, z1_init, z2_init, draw = True):
    t_size = int(t_max / h)
    result_list = []
    cur_result = [z1_init, z2_init]
    result_list.append([z1_init, z2_init])
    for i in range(t_size - 1):
        z1_1, z2_1 = k1(cur_result[0], cur_result[1])
        z1_2, z2_2 = k2(cur_result[0], cur_result[1], h)
        cur_result[0] += h * (z1_1 + z1_2) / 4.0
        cur_result[1] += 3.0 * h * (z2_1 + z2_2) / 4.0
        result_list.append([cur_result[0], cur_result[1]])

    if draw:
        t_list = np.arange(0, h * t_size, h)
        y = np.zeros(t_size)
        dy = np.zeros(t_size)
        for i in range(t_size):
            y[i] = result_list[i][0]
            dy[i] = result_list[i][1]
        plt.suptitle("Figure of Van Der Pol Equation\ny0={}, v0={}, range of t:[0, {}], h={}".format(str(z1_init), str(z2_init), str(t_max), str(h)))
        plt.subplot(1, 2, 1)
        plt.title("y-t, y\'-t")
        plt.plot(t_list, y, 'r-', label='y', markersize=1)
        plt.plot(t_list, dy, 'bo', label='y\'', markersize=1)
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.title("y-y\'")
        plt.plot(y, dy)

        plt.show()


if __name__ == "__main__":
    van_der_Pol(20, 0.01, 2, 0)

