import numpy as np
from sklearn.linear_model import LinearRegression

#Model 1
#X = [velocity, distance] then Y = total time

X = np.array([[0.01,500], [0.01,250], [0.1,500], [0.1,1000]]).reshape((-1,2))
print(X)

y = np.array([56.69,32.44,6.23,11.12])
print(y)

model = LinearRegression().fit(X, y)

print('slope', model.coef_)

print('intercept', model.intercept_)

print('predict', model.predict(np.array([0.1,200]).reshape((-1,2))))
# I don't think we should mix this 2 velocity in 1 equation cuz' the 0.1 is close to normal time = velocity/distance

#Model 2 for only velocity of 0.01 mm/s
#X2 [velocity, distance] then y = total time

X2 = np.array([[0.01,500], [0.01,250]]).reshape((-1,2))
print(X2)

y2 = np.array([56.69,32.44])
print(y2)

model2 = LinearRegression().fit(X2, y2)

print('slope', model2.coef_)

print('intercept', model2.intercept_)

#Model 3 for True and Measure Velo for velocity at 0.01 to 0.1
#X3 thue velo (that we input) then y = measure velo

x3 = np.array([0.008,0.01,0.025,0.05,0.075,0.1]).reshape((-1,1))
y3 = np.array([0.0076,0.0076,0.019,0.036,0.057,0.1])
print(y3)

model3 = LinearRegression().fit(x3, y3)

print('slope', model3.coef_)
print('intercept', model3.intercept_)

x_pred = 0.03
y_pred = model3.coef_*(x_pred)+model3.intercept_
print(y_pred)