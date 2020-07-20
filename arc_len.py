import math
import time

start_time = time.time()

L = 0.000001

next_point = (0,1)
m = 0
arc_len = 0

def get_delta_x(delta_length, slope):
    return delta_length/(((slope**2)+1)**(1/2))

while (next_point[0] < 1 or next_point[1] > 0):
    m = -(next_point[0]/next_point[1])
    delta_x = get_delta_x(L, m)
    delta_y = m*delta_x
    next_point = (next_point[0] + delta_x, next_point[1] + delta_y)
    arc_len = arc_len + L

pi = arc_len * 2
elapsed_time = time.time() - start_time
accuracy_percent = abs((math.pi-pi)/math.pi)*100

print("Pi: " + str(pi))
print("This took " + str(elapsed_time) + "s.")
print("Accurate within: " + str(accuracy_percent) + "%")

