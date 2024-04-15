
import numpy as np
import matplotlib.pyplot as plt
print("hello sbycc")


#plot somethings of there
#data
def ycc_first_plot():
    """
    this is a demo for git flow, it would be 
    plot a simple graph in current winodws
    save in ycc_first_image.png
    """
    #add some shit
    #data
    x = np.arange(0,100,1)
    y = np.sin(x) ** 3
    plt.plot(x, y, '-', linewidth=0.8)
    plt.show()
    plt.savefig("ycc_first_image.png")    

ycc_first_plot()