x0 = float(input('initial position: '))
u = float(input('initial velocity: '))
a = float(input('acceleration: '))
T = float(input('total Time: '))
dt = float(input('time step: '))
pos = []
dist = []
vel = []
time = []
t = 0
formula_displacement = (u * T + (1/2 * a * T * T)) + x0

def natureOfMotion(initialVel, acc):
    if initialVel == 0:
        return 'AT REST'
    elif acc == 0:
        return 'UNIFORM MOTION'
    elif initialVel * acc > 0:
        return 'SPEEDING UP'
    elif initialVel * acc < 0:
        return 'SLOWING DOWN'
nature = natureOfMotion(u, a)

def ifDirectionChanged():
    if nature == 'SLOWING DOWN':
        for index, value in enumerate(vel):
            if (index + 1)<len(vel) and value * vel[index + 1] < 0:
                return time[index + 1]
            else:
                return 'NO DIRECTION CHANGE'
    else:
        return 'NO DIRECTION CHANGE'

while t <= T:
    pos.append(x0)
    dist.append(abs(x0))
    vel.append(u)
    time.append(t)
    x0 += u*dt  
    u += a*dt
    t += dt
v = vel[-1]
x = pos[-1]
print(f'{x}\n{v}')
print(max(dist))
print(nature)
print(time[dist.index(min(dist))])
print(formula_displacement - x)
print(ifDirectionChanged())