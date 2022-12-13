import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def g(y, a=10., b=8./3., c=28.):
    tmp_y = np.zeros(3)
    tmp_y[0] = a * (y[1] - y[0])
    tmp_y[1] = - y[0] * y[2] + c * y[0] - y[1]
    tmp_y[2] = y[0] * y[1] - b * y[2]
    return tmp_y

def runge_kutta(t_max, h, init, draw = True):
    t_size = int(t_max / h)
    result_list = []
    cur_result = np.zeros(3)
    cur_result[0] = init[0]
    cur_result[1] = init[1]
    cur_result[2] = init[2]
    result_list.append([init[0], init[1], init[2]])

    for i in range(t_size - 1):
        k1 = g(cur_result)
        k2 = g(cur_result + 0.5 * h * k1)
        k3 = g(cur_result + 0.5 * h * k2)
        k4 = g(cur_result + h * k3)

        # print(k1, k2, k3, k4)
        cur_result += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

        # print(cur_result)

        result_list.append([cur_result[0], cur_result[1], cur_result[2]])

    x = np.zeros(t_size)
    y = np.zeros(t_size)
    z = np.zeros(t_size)
    for i in range(t_size):
        x[i] = result_list[i][0]
        y[i] = result_list[i][1]
        z[i] = result_list[i][2]
    
    return x, y, z
    

if __name__ == "__main__":
    # T2
    init = np.zeros(3)
    init[0] = 2
    init[1] = 2
    init[2] = 10.

    x1, y1, z1 = runge_kutta(50, 0.01, init)
    
    init[2] = 10.01
    x2, y2, z2 = runge_kutta(50, 0.01, init)
    

    t_list = np.arange(0, 50, 0.01)
    plt.suptitle("Figure of Lorenz Equation")
    
    # plt.subplot(1, 3, 1)
    # plt.plot(t_list, x1, 'r-', label='x1', markersize=1)
    # plt.plot(t_list, x2, 'b-', label='x2', markersize=1)
    # plt.legend()
    
    # plt.subplot(1, 3, 2)
    # plt.plot(t_list, y1, 'r-', label='x1', markersize=1)
    # plt.plot(t_list, y2, 'b-', label='x2', markersize=1)
    # plt.legend()
    
    # plt.subplot(1, 3, 3)
    # plt.plot(t_list, y1, 'r-', label='x1', markersize=1)
    # plt.plot(t_list, y2, 'b-', label='x2', markersize=1)
    # plt.legend()
    # plt.show()

    # t_list = np.arange(0, 50, 0.01)
    # plt.title("Figure of Lorenz Equation\nx0={}, y0={}, z0={}, range of t:[0, {}], h={}"
    #     .format(str(init[0]), str(init[1]), str(init[2]), str(t_max), str(h)))
    # plt.plot(t_list, x, 'r-', label='x', markersize=1)
    # plt.plot(t_list, y, 'b-', label='y', markersize=1)
    # plt.plot(t_list, z, 'g-', label='z', markersize=1)
    # plt.legend()
    # plt.show()

    # ax = plt.axes(projection='3d')
    # for i in range(50/0.01):
    #     ax.scatter(x[i], y[i], z[i])
    # ax.set_zlabel('Z', fontdict={'size': 5})
    # ax.set_ylabel('Y', fontdict={'size': 5})
    # ax.set_xlabel('X', fontdict={'size': 5})
    # plt.show()
