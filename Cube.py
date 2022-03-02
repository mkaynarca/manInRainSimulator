import numpy as np

def createBox(size:int):
    
    top = np.zeros([size,size])
    bottom = np.zeros([size,size])
    front = np.zeros([size,size])
    back = np.zeros([size,size])
    left = np.zeros([size,size])
    right = np.zeros([size,size])
    
    box = [top, bottom, front, back, left, right]
    
    return box