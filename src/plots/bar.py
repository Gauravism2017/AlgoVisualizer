import os
import copy
import json
import matplotlib
import numpy as np
from numba import jit, jitclass        # import the decorator
from numba import int32, float32
from numba.numpy_support import from_dtype
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.animation as animation
from src.config import SAVE_LOCATION
plt.rcParams['figure.max_open_warning'] = 2000

# def _plot(array, j, k):
#     _pos = list(range(1, len(array) + 1))
#     barlist = plt.bar(_pos, array, color = 'blue')
#     barlist[j].set_color('r')
#     barlist[j + 1].set_color('g')
#     plt.xticks(_pos, array)
#     plt.ylabel('value')
#     plt.title('insertion sort')
#     #plt.show()
#     save = os.path.join(SAVE_LOCATION, '{}.png'.format(k))
#     plt.savefig(save, dpi=plt.gcf().dpi, bbox_inches = 'tight')
#     plt.clf()


class Plot:

    def __init__(self, array, j, k, title, *args, **kwargs):
        self.array = array
        self._len = len(self.array)
        self.j = j
        self.k = k
        self.title = title
        self.__dict__.update(kwargs)
        if hasattr(self, "next"):
            pass
        else:
            self.next = j + 1
        self.images = []

    def _plot(self, first = 0, last = 0):
        fig = plt.figure()
        _pos = list(range(1, self._len + 1))
        barlist = plt.bar(_pos, self.array, color = 'blue')
        print(barlist)
        if(first != 1 and last != 1):
            barlist[self.j].set_color('r')
            barlist[self.next].set_color('g')
        if(self._len < 10):
            plt.xticks(_pos, self.array)
        plt.ylabel('value')
        plt.title(self.title)
        #return plt.plot()
        self.images.append(barlist)
        #plt.show()

        ####################    To save images  #####################
        #############################################################
        # save = os.path.join(SAVE_LOCATION, '{}.png'.format(self.k))
        # plt.savefig(save, dpi=plt.gcf().dpi, bbox_inches = 'tight')
        # plt.clf()

    def update(self, array, j, k, *args, **kwargs):
        self.array = array
        self.j = j
        self.k = k
        if "next" in kwargs:
            self.next = kwargs.get("next")
        else:
            self.next = self.j + 1

##############################################################################################################################3

class AnimatePlot:
    def __init__(self, title, *args, **kwargs):
        self.array = []
        self.j = []
        self.k = []
        self.title = title
        self._len = 0
        self.next = []
        self.mid = []

    
    def update(self, arr, j, k, *args, **kwargs):
        _arr = copy.deepcopy(arr)
        self.array.append(_arr)
        self.j.append(j)
        self.k.append(k)
        if "next" in kwargs:
            self.next.append(kwargs.get("next"))
        else:
            self.next.append(self.j[-1] + 1)
        if "mid" in kwargs:
            self.mid.append(kwargs.get("mid"))
        else:
            self.mid.append(self.j[-1])
        # print("j {} next {}".format(j, kwargs.get("next")))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    
    ####################### NUMBA SUPPORT ########################


    # def __init__(self, title):
    #     self.array = []
    #     self.j = []
    #     self.k = []
    #     self.title = title
    #     self._len = 0
    #     self.next = []

    # def update(self, arr, j, k, next):
    #     _arr = copy.deepcopy(arr)
    #     self.array.append(_arr)
    #     self.j.append(j)
    #     self.k.append(k)
    #     self.next.append(next)

###################################################################

    

    def animate(self, i):
        plt.clf()
        # print(self.next[i])
        _pos = list(range(1, self._len + 1))
        barlist = plt.bar(_pos, self.array[i], color = 'blue')
        #print(barlist)
        if(i != 0 and i <= len(self.array) - 5):
            barlist[self.j[i]].set_color('r')
            barlist[self.next[i]].set_color('g')
        if(self._len <= 10):
            plt.xticks(_pos, self.array[i])
        plt.ylabel('value')
        plt.title(self.title)
        return barlist
        #return plt.plot()
        #plt.show()

    def mergeAnimate(self, i):
        plt.clf()
        # print(self.next[i])
        _pos = list(range(1, self._len + 1))
        barlist = plt.bar(_pos, self.array[i], color = 'blue')
        #print(barlist)
       
        for k in range(self.j[i], self.mid[i] + 1):
            print(k)
            barlist[k].set_color('r')
            #barlist[self.next[i]].set_color('g')

        for k in range(self.mid[i] + 1, self.next[i]):
            print(k)
            barlist[k].set_color('g')

        if(self._len <= 20):
            plt.xticks(_pos, self.array[i])
        # plt.ticklabel_format(style='sci', axis='x', scilimits=(0,384))
        fmt = FuncFormatter(lambda x, pos: tickformat(x / 2**256))
        plt.xaxis.set_major_formatter(fmt)
        plt.xlabel('factor ($s 2^256$)')
        plt.ylabel('value')
        plt.title(self.title)
        return barlist

    def RadixAnimate(self, i):
        plt.clf()
        # print(self.next[i])
        _pos = list(range(1, self._len + 1))
        barlist = plt.bar(_pos, self.array[i], color = np.random.rand(3,))
        #print(barlist)
       

        if(self._len <= 10):
            plt.xticks(_pos, self.array[i])
        plt.ylabel('value')
        plt.title(self.title)
        return barlist
        

        

        



    def CreateVideo(self):
        # _createVideo(self.animate, len(self.array))
        fig = plt.figure()
        if(self.title == "merge Sort"):
            ani = animation.FuncAnimation(fig, self.mergeAnimate, range(len(self.array)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        # if(self.title == "Quick Sort"):
        if(self.title == "Radix Sort"):
            ani = animation.FuncAnimation(fig, self.RadixAnimate, range(len(self.array)),interval = 1000,  blit=True, repeat_delay=5000, save_count = 1000)
        
        else:
            ani = animation.FuncAnimation(fig, self.animate, range(len(self.array)),interval = 500,  blit=True, repeat_delay=5000, save_count = 1000)
        FFwriter=animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
        ani.save(self.title+'.mp4')





