"""
4. LabExercise: Skin Color Detection

Exercise 2

Make a 3D scatter plot (using plt.scatter) of skin colors and non skin colors. Randomly select say 500 colors from each
class to speed things up. Be sure to label the axes of the plot and to pick different colors for the skin and non skin
colors (no need to color each individual color with its RGB value).

"""

import numpy as np
import matplotlib.pyplot as plt

f = plt.imread('images/FacePhoto/0520962400.jpg')
m = plt.imread('images/GroundT_FacePhoto/0520962400.png')

# plt.subplot(121)
# plt.imshow(f)
# plt.subplot(122)
# plt.imshow(m)
# plt.show()

# Select all skin colors and non skin color, remove duplicate and shuffle them
skincolors = f[m[:, :, 0] > 0]
print(skincolors.shape)
skincolors = np.unique(skincolors, axis=0)
np.random.shuffle(skincolors)
print(skincolors.shape)

nonskincolors = f[m[:, :, 0] == 0]
print(nonskincolors.shape)
nonskincolors = np.unique(nonskincolors, axis=0)
np.random.shuffle(nonskincolors)
print(nonskincolors.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Split value to three axiss
xs1, ys1, zs1 = np.hsplit(skincolors[:500], 3)
xs2, ys2, zs2 = np.hsplit(nonskincolors[:500], 3)

ax.scatter(xs1, ys1, zs1, marker='o')
ax.scatter(xs2, ys2, zs2, marker='^')

ax.set_xlabel('R Value')
ax.set_ylabel('G Value')
ax.set_zlabel('B Value')
ax.set_title('Exercise 2')

plt.show()
fig.savefig('figures/Exercise2')
