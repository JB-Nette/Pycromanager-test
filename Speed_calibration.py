import json
import numpy as np
import matplotlib.pyplot as plt


with open('Y:/lightsheetsatge/stage_time_distance3_speed3.txt') as f:
    json_data = json.load(f)

path = 'Y:/lightsheetsatge/'
vallist=[]
distance = np.array([20000,30000,40000,50000])
key = '7.5'
xtrue = np.divide(distance*0.001,float(key))
print(xtrue)
for val in json_data[key]:
    print(val)
    val = str(val)
    vallist.append(val)


a = round(float(vallist[1]),3)
b = round(float(vallist[1])+float(vallist[2]),3)
c= round(float(vallist[1])+float(vallist[2])+float(vallist[3]),3)
d= round(float(vallist[1])+float(vallist[2])+float(vallist[3])+float(vallist[4]),3)
#e= round(float(vallist[1])+float(vallist[2])+float(vallist[3])+float(vallist[4])+float(vallist[5]),3)
#plt.figure()
_, ax =plt.subplots()
plt.title("Velocity of "+ key+ "mm/s")
ax.plot(distance,np.array([a,b,c,d]))
ax.plot(distance,xtrue)
_ = ax.set_xlabel('distance')
_ = ax.set_ylabel('time')
_ = ax.set_title("Velocity of "+ key+ "mm/s")
_ = ax.legend(["Measure", "True"])
ax.grid()
plt.show()
plt.savefig(path + "Velocity of "+ key+ "mm-s"+ '_2'+'.png')



#plt.figure()
#plt.title("Velocity of "+ key+ "mm/s")
#plt.plot(distance, [vallist[1],round(float(vallist[1])+float(vallist[2]),3),round(float(vallist[1])+float(vallist[2])+float(vallist[3]),3),round(float(vallist[1])+float(vallist[2])+float(vallist[3])+float(vallist[4]),3)])
#plt.plot(distance, xtrue)
#plt.show()
#plt.savefig(path + "Velocity of "+ key+ "mm-s" +"_2"+'.png')
a = round(float(vallist[1]),3)
b = round(float(vallist[1])+float(vallist[2]),3)
c= round(float(vallist[1])+float(vallist[2])+float(vallist[3]),3)
d= round(float(vallist[1])+float(vallist[2])+float(vallist[3])+float(vallist[4]),3)
#e= round(float(vallist[1])+float(vallist[2])+float(vallist[3])+float(vallist[4])+float(vallist[5]),3)
#plt.figure()
truevelo = [0.008,0.01,0.025,0.05,0.075,0.1,0.25,0.5,0.75,1,2.5,5,7.5]
measurevelo = [0.0076,0.0076,0.019,0.036,0.057,0.1,0.25,0.5,0.72,1,2.3,4.2,6]
_, ax =plt.subplots()
ax.plot(truevelo, measurevelo, 'ro-')
ax.plot(truevelo, truevelo, 'bo-')
#ax.plot(distance,truevelo)
_ = ax.set_xlabel('true velo (mm-s)')
_ = ax.set_ylabel('measure velo (mm-s)')
_ = ax.set_title("True vs Measure Velo mm/s")
_ = ax.legend(["Measure","True"])
plt.ylim((-0.5,8))
ax.grid()
plt.show()
plt.savefig(path + "True Vs Measure velocity mm-s_all"+ '_2'+'.png')

truevelo = [0.008,0.01,0.025,0.05,0.075,0.1]
measurevelo = [0.0076,0.0076,0.019,0.036,0.057,0.1]
_, ax =plt.subplots()
ax.plot(truevelo, measurevelo, 'ro-')
ax.plot(truevelo, truevelo, 'bo-')
#ax.plot(distance,truevelo)
_ = ax.set_xlabel('true velo (mm-s)')
_ = ax.set_ylabel('measure velo (mm-s)')
_ = ax.set_title("True vs Measure Velo mm/s")
_ = ax.legend(["Measure","True"])
plt.ylim((-0.01,0.15))
ax.grid()
plt.show()
plt.savefig(path + "True Vs Measure velocity mm-s"+ '_3'+'.png')

