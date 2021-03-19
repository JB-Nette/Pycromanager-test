import numpy as np

def yMoveTo(y):
    print("Move Y", y)
def vMoveTo(z):
    print("Move Z", z)
def xMoveTo(x):
    print("Move x", x)

xstart= 0
ystart= 0
zstart= 0
xdim= 100
ydim = 100
zdim = 5
ystep =10
zstep =1
xend = xstart+xdim
ypos = np.arange(ystart,ystart+ydim, ystep)
zpos = np.arange(zstart,zstart+zdim, zstep)
exp_time = 0.01 #s
channels = ["red", "green"]
exp_channels = [50, 100]

for num_chan, chan in enumerate(channels):
    exp_ch = exp_channels[num_chan]
    print(exp_ch)
    print(chan)
    for y in ypos:
        yMoveTo(y)
        for znum, z in enumerate(zpos):
            if znum%2 ==0:
                vMoveTo(z)
                xMoveTo(xend)
                #MDA
            if znum%2 ==1:
                vMoveTo(z)
                xMoveTo(xstart)
                #MDA

#MDA
Measure_velo = (0.94169947*velocity)-0.004195909745559313
Cal_time = xdim/Measure_velo
Num_timepoint = Cal_time/exp_time











