"""
4. LabExercise: Skin Color Detection

Exercise 3

Skin color classification in principle can be done in a color space with only two dimensions as it largely independent
on the intensity. One of the possible color models that makes an explicit distinction between color and intensity is
the Lab color model. Install skimage to use the function skimage.color.rgb2lab. Then use only the ‘a’ and ‘b’ components
of the color.

1. Make a 2D scatter plot of skin and non skin colors in the ‘ab’ plane. Again use different colors for skin and non skin
colors.
2. Learn a logistic regression classifier using just the ‘a’ and ‘b’ color components.

"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2lab
from sklearn.linear_model import LogisticRegressionCV

f = plt.imread('images/FacePhoto/0520962400.jpg')
m = plt.imread('images/GroundT_FacePhoto/0520962400.png')

f = rgb2lab(f)

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

fig, ax = plt.subplots()
_, xs1, ys1 = np.hsplit(skincolors[:500], 3)
_, xs2, ys2 = np.hsplit(nonskincolors[:500], 3)

ax.scatter(xs1, ys1, marker='o')
ax.scatter(xs2, ys2, marker='^')

ax.set_xlabel('a Value')
ax.set_ylabel('b Value')
ax.set_title('Exercise 3')

plt.show()
fig.savefig('fig/Exercise3')

np.delete(skincolors, 0, 1)
np.delete(nonskincolors, 0, 1)

color = np.vstack((skincolors, nonskincolors))
target = np.concatenate((np.ones(len(skincolors)), np.zeros(len(nonskincolors))))

learn_color = color[1::2]
test_color = color[0::2]
learn_target = target[1::2]
test_target = target[0::2]

logregr = LogisticRegressionCV()
logregr.fit(learn_color, learn_target)
logregr.score(test_color, test_target)

image_colors = f.reshape((-1, 3))
predict_skin = logregr.predict(image_colors).reshape(f.shape[:2])
plt.subplot(121)
plt.imshow(plt.imread('images/FacePhoto/0520962400.jpg'))
plt.subplot(122)
plt.imshow(predict_skin)
plt.show()
