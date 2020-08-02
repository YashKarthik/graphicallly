import numpy as np
import matplotlib.pyplot as plt
from termcolor import cprint

x = np.linspace(-10, 10, 100)


def quadratic(a, b, c, x):
    y = a*(x**2)+b*x+c
    return y


def cubic(a, b, c, d, x):
    y = a*(x**3)+b*(x**2)+c*x+d
    return y


def trigonometric(x):
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.plot(x, np.tan(x))
    plt.show()


def plot_graph(x_plot, y_plot):
    plt.plot(x_plot, y_plot)
    plt.show()


def plotter(x):
    cprint("""Which type of plot do u wanna plot??
    Enter 1 for quadratic
    Enter 2 for cubic
    Enter 3 for trigonometric""", 'blue')
    plot_typ = float(input("Enter number for plot type:  "))

    if plot_typ == 3:
        trigonometric(x)

    elif plot_typ == 1:
        a = float(input("Enter value for a =!0:  "))
        b = float(input("Enter value for b:  "))
        c = float(input("Enter value for constant:  "))
        y_plot = quadratic(a, b, c, x)
        plot_graph(x, y_plot)

    elif plot_typ == 2:
        a = float(input("Enter value for a =!0:  "))
        b = float(input("Enter value for b:  "))
        c = float(input("Enter value for c:  "))
        d = float(input('Enter value for constant:  '))
        y_plot = cubic(a, b, c, d, x)
        plot_graph(x, y_plot)


# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(which='major',
        alpha=0.4, linestyle='--')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plotter(x)
