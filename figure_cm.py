'''Image context manager'''
import matplotlib.pyplot as plt
from random import random

class Figure(object):
    def __init__(self, filename=None, title=None, figsize = None, show = False):
        if filename is None:
            filename = str(hash(random()))
        self.filename = filename
        self.title = title
        self.show = show
        self.figsize = figsize
    def __enter__(self,*_):
        plt.figure(self.figsize)
        if self.title is not None:
            plt.suptitle(self.title)
    def __exit__(self, *_):
        plt.savefig(self.filename)
        if self.show:
            plt.show()
