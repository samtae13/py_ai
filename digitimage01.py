import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

print(digits.images[1])

plt.imshow(digits.images[1], cmap='Greys')
plt.show()