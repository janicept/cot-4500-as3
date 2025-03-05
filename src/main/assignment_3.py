#Euler Method
# Define the function for dy/dt
def dydt(t, y):
    return t - y**2

# Initial conditions
t_start, y_start = 0, 1
t_end = 2
num_steps = 10
step_size = (t_end - t_start) / num_steps  # h = 0.2

# Lists to store results
t_values = [t_start]
y_values = [y_start]

# Apply Euler's Method
t_curr, y_curr = t_start, y_start

for _ in range(num_steps):
    y_next = y_curr + step_size * dydt(t_curr, y_curr)  
    t_curr += step_size 
    
    t_values.append(t_curr)

  #___________________________
  #Runge-Kutta
# Define the function for dy/dt
def dydt(t, y):
    return t - y**2

# Initial conditions
t_start, y_start = 0, 1
t_end = 2
num_steps = 10
step_size = (t_end - t_start) / num_steps  # h = 0.2

t_values = [t_start]
y_values = [y_start]

# Apply Runge-Kutta 4th Order Method
t_curr, y_curr = t_start, y_start

for _ in range(num_steps):
    k1 = step_size * dydt(t_curr, y_curr)
    k2 = step_size * dydt(t_curr + step_size / 2, y_curr + k1 / 2)
    k3 = step_size * dydt(t_curr + step_size / 2, y_curr + k2 / 2)
    k4 = step_size * dydt(t_curr + step_size, y_curr + k3)

    y_next = y_curr + (1/6) * (k1 + 2*k2 + 2*k3 + k4)  # RK4 update
    t_curr += step_size  # Increment t

    t_values.append(t_curr)
    y_values.append(y_next)

    y_curr = y_next  

print(y_curr)
    y_values.append(y_next)

    y_curr = y_next  

print(y_curr)
