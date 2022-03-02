import numpy as np
import random as r

# Terminal velocity for raindrop is approxiamtely 9 m/s
# I will take this as its constant vertical speed and add effects of the wind and the speed of the box

# For top surface, rain or running speed does not effect the number of accumulated raindrops

# For side surfaces, wind speed effcts can be summarized as
# The projection of surface will form a parallellogram on the cloud

# For front and back

# The height of the parallelogram is box_size*relative_speed_x/vertical speed

# The top and the bottom parts are box_size and box_size*relative_speed_y/vertical speed

# Total parallellogram area is
# 0.5 * box_size^2 * (v_x / mg) * (1 + (v_y / mg)) 
# v_x/mg = tan(alpha)
# v_y/mg = tan(beta)
# projected area = 0.5 * size^2 * tan(alpha) * (1 + tan(beta))
# scale : 0.5 * tan(alpha) * (1 + tan(beta))
 
# For left and right
# The height of the parallelogram is box_size*relative_speed_y/vertical speed
# The top and the bottom parts are box_size and box_size*relative_speed_y/vertical speed
# Total parallellogram area is
# 0.5 * box_size^2 * (v_y / mg) * (1 + (v_x / mg)) 
# v_x/mg = tan(alpha)
# v_y/mg = tan(beta)
# projected area = 0.5 * size^2 * tan(beta) * (1 + tan(alpha))
# scale : 0.5 * tan(beta) * (1 + tan(alpha))

# While simulating the raindrop i have assumed that every raindrop has scaled probability since it is a projection 


def relativeSpeedTangent(windX : float, windY : float, mg : float, speed : float):
    
    # I have assumed that box moves in x direction
    v_x = windX + speed
    v_y = windY
    
    tan_a = v_x / mg
    tan_b = v_y / mg
    
    tan = [tan_a, tan_b]
    
    return tan 

def rainSurfaces(box : list, tan : list, rainDensity : float):
    
    #Slice surfaces
    top = np.copy(box[0])
    front = np.copy(box[2])
    back = np.copy(box[3])
    left = np.copy(box[4])
    right = np.copy(box[5])
    
    # Extract tangents    
    tan_a = tan[0]
    tan_b = tan[1]
    
    scaleCoeffFB = abs(tan_a) * (1 + abs(tan_b))
    scaleCoeffLR = abs(tan_b) * (1 + abs(tan_a))
    
    # Accumulate raindrops for top surface/undirectionally
    for i in range(len(top)):
        for j in range(len(top[0])):
            top[i][j] = r.random()
            if top[i][j] < rainDensity:
                top[i][j] = 1
            else:
                top[i][j] = 0
                
    
    
    # Accumulate raindrops according to the direction
    if tan_a > 0:
         for i in range(len(front)):
            for j in range(len(front[0])):
                front[i][j] = r.random()
                if front[i][j] < rainDensity * scaleCoeffFB: # Scale the rain density wrt area scale
                    front[i][j] = 1
                else:
                    front[i][j] = 0
                
    if tan_a < 0:
         for i in range(len(back)):
            for j in range(len(back[0])):
                back[i][j] = r.random()
                if back[i][j] < rainDensity * scaleCoeffFB:
                    back[i][j] = 1
                else:
                    back[i][j] = 0
                
    if tan_b > 0:
        for i in range(len(left)):
            for j in range(len(left[0])):
                left[i][j] = r.random()
                if left[i][j] < rainDensity * scaleCoeffLR:
                    left[i][j] = 1
                else:
                    left[i][j] = 0
                
    if tan_b < 0:
        for i in range(len(right)):
            for j in range(len(right[0])):
                right[i][j] = r.random()
                if right[i][j] < rainDensity * scaleCoeffLR:
                    right[i][j] = 1
                else:
                    right[i][j] = 0
                    
    
    box[0] = box[0] + top
    box[2] = box[2] + front
    box[3] = box[3] + back
    box[4] = box[4] + left
    box[5] = box[5] + right
    
    return box
    
        
                
    