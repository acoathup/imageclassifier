import numpy as np
import scipy
from matplotlib import pyplot as plt


def main():

    a = np.load('/home/acoathup/train_data2.npz')

    for i in a['with_seed'][0:10]:

        fig, ax = plt.subplots()

        ax.imshow(i, origin='lower', cmap='Greys_r')
        plt.show()





def f():
    print('hello world')


class Nolan(object):
    def __init__(self, last_name):
        self.last_name = last_name
        pass

    def f(self):
        print('hello world')


if __name__ == '__main__':
    main()