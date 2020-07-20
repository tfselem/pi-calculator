import math
import time

start_time = time.time()

delta = 0.000000001
area = 0

def y(x):
    return (1-x**2)**(0.5)

x = 0
while x <= 1:
    area = area + (delta*y(x))
    x = x + delta

pi = 4*area
elapsed_time = time.time() - start_time
accuracy_percent = abs((math.pi-pi)/math.pi)*100

print("Pi: " + str(pi))
print("This took " + str(elapsed_time) + "s.")
print("Accurate within: " + str(accuracy_percent) + "%")

