import matplotlib.pyplot as plt

x = [0]
y = [0]

dataset = open('C:\\Users\\eduar\\OneDrive\\Documents\\GitHub\\PyInstrumentation2\\data\\Loki_static_fire_test_.csv', 'r')

min = float(175500)
max = float(182000)
for line in dataset:
    line = line.strip("\n")
    # X,Y = line.split(',')
    X = primeira coluna
    Y = segunda coluna
    if int(X) > x[len(x)-1]:
        if min < float(X) < max:
            x.append((float(X)-min)/1000.0)
            y.append(float(Y))
x = x[1:]
y = y[1:]

plt.plot(x,y)

plt.title("Loki's thrust curve")
plt.xlabel("Time (s)")
plt.ylabel("Thrust (N)")
plt.grid()
plt.show()
