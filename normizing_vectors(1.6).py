import math

#u_normal = u/ (||u||)


u = [0,5]
if u[0] == 0 or u[1] == 0:
    print("Não é possível dividir por 0!")
else:
    u_normal_x = u[0] / math.sqrt(u[0] * u[0] + u[1] * u[1])
    u_normal_y = u[1] / math.sqrt(u[0] * u[0] + u[1] * u[1])
    print(u_normal_x, u_normal_y)
