"""
2. Introduction to Python for Image Processing And Computer Vision

Exercise 1

Time these alternatives using an image of size 64x64 for several sizes of the neighborhood (from 3x3 to 11x11 eg).
Make a plot with the timings as function of the neighborhood size for all filters.

"""

import cv2
import time
import numpy as np
import matplotlib.pyplot as plt


def linfilter(f, w):
    """Linear Correlation"""
    g = np.empty(f.shape, dtype=f.dtype)
    M, N = f.shape
    K, L = (np.array(w.shape) - 1) // 2

    def value(i, j):
        if i < 0 or i >= M or j < 0 or j >= N:
            return 0
        return f[i, j]

    for j in range(N):
        for i in range(M):
            summed = 0
            for k in range(-K, K + 1):
                for l in range(-L, L + 1):
                    summed += value(i + k, j + l) * w[k + K, l + L]
            g[i, j] = summed
    return g


def get_time(img, size):
    """Calculate excution time"""
    kernel = np.ones((size, size)) / size * size

    start = time.time()
    _ = linfilter(img, kernel)

    return round(time.time() - start, 1)


def autolabel(rects):
    """Add value to bar"""
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 0.5, '%.1f s' % float(height), ha='center', va='bottom')


img = cv2.imread('images/cameraman.png', 0)
sizes = []
times = []

for i in range(3, 13, 2):
    sizes.append(str(i) + 'x' + str(i))
    times.append(get_time(img, i))

x_pos = [i for i, _ in enumerate(sizes)]
# print(sizes)
# print(times)

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, times, color='b')

ax.set_xlabel('Kernel size')
ax.set_ylabel('Execution time (s)')

ax.set_ylim(0, int(max(times)) + 5)
ax.bar(sizes, times)

autolabel(rects1)
ax.set_title('Exercise 1')

plt.show()
fig.savefig('fig/Exercise1')
