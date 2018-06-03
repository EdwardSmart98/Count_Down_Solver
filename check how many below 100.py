import itertools
import matplotlib.pyplot as plt


def product(list_of_int):
    total = 1;
    for x in list_of_int:
        total = total * x
    return total


values = [x+1 for x in range(10)]
a = list(itertools.combinations_with_replacement(values, 6))
results = [product(x) for x in a]
print(a)
print(len(a))

x = [i for i in range(1000)]

y = [0 for i in range(1000)]
for i in x:
    for j in results:
        if j >= i:
            y[i] = y[i] + 1
    y[i] = y[i]/5000
plt.interactive(False)
plt.plot(x, y)
plt.axis([0, 1000 ,0,1])
plt.show()


