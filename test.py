from matplotlib.colors import Colormap
import cube
from matplotlib import pyplot as plt
import environment
import time

area = 100
density = 0.0002 * 50
mg = 10
windx = 10
windy = 10
speed = 1000

# Rainfall types according to some random website that i found

# Light rain - <2.5 mm/hr*m^2
# Moderate rain - 2.5 mm/hr - 7.5 mm/hr*m^2
# Heavy rain - 7.5 mm/hr - 50 mm/hr*m^2
# Violent rain - >50 mm/hr*m^2

# Each raindrop can be in between 0.001 ml and 0.3 ml, in average 0.15 ml

# 1 mm per hour per m^2 = 1 liter  per hour 

# => 1 mm per hour per m^2 = 1 liter per hour =~ 6700 raindrops per hour =~ 2 raindrops per second


box = cube.createBox(area)

tans = environment.relativeSpeedTangent(windx, windy, mg, speed)

fgr = plt.ion()

for i in range(100):
    box = environment.rainSurfaces(box,tans,density)

    '''fgr = plt.imshow(box[0], cmap='gray')
    fgr = plt.pause(0.00000000000000000001)
    fgr = plt.clf()'''
    
""" for i in range(100):
    box = environment.rainSurfaces(box, tans, density)


plt.figure("top")
plt.imshow(box[0])


plt.figure("front")
plt.imshow(box[2])


plt.figure("back")
plt.imshow(box[3])


plt.figure("left")
plt.imshow(box[4])


plt.figure("right")
plt.imshow(box[5])

plt.show(block=False) """

print("top : ", sum(sum(box[0])) , " raindrops ~=", sum(sum(box[0]))/6700, " liter water")
print("front : ", sum(sum(box[2])) , " raindrops ~=", sum(sum(box[2]))/6700, " liter water")
print("back : ", sum(sum(box[3])) , " raindrops ~=", sum(sum(box[3]))/6700, " liter water")
print("left : ", sum(sum(box[4])) , " raindrops ~=", sum(sum(box[4]))/6700, " liter water")
print("right : ", sum(sum(box[5])) , " raindrops ~=", sum(sum(box[5]))/6700, " liter water")