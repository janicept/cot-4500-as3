# Euler Method
def func1(t, y):  
    return t - y**2  

# Initial conditions for Euler Method
#example (range: 0 < t < 2, y(0) or f(0) = 1, iterations = 10) 
t1, y1 = 0, 1  
end_t1 = 2  
steps1 = 10  
h1 = (end_t1 - t1) / steps1  

# Apply Euler's Method
for _ in range(steps1):
    y1 += h1 * func1(t1, y1)  
    t1 += h1  

print(y1)

print()  
#__________________________
# Runge-Kutta Method
def func2(t, y):  
    return t - y**2  

# Initial conditions for Runge-Kutta
t2, y2 = 0, 1  
end_t2 = 2  
steps2 = 10  
h2 = (end_t2 - t2) / steps2  

# Apply Runge-Kutta 4th Order Method
for _ in range(steps2):
    k1 = h2 * func2(t2, y2)
    k2 = h2 * func2(t2 + h2 / 2, y2 + k1 / 2)
    k3 = h2 * func2(t2 + h2 / 2, y2 + k2 / 2)
    k4 = h2 * func2(t2 + h2, y2 + k3)

    y2 += (1/6) * (k1 + 2*k2 + 2*k3 + k4)  
    t2 += h2  

print(y2)
