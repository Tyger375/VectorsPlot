import matplotlib.pyplot as plt
import numpy as np


class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def modulo(self):
        return np.sqrt((pow(self.x, 2) + pow(self.y, 2)))

    def __add__(self, other):
        if type(other) != Vector2D:
            raise Exception("Invalid type")
        return Vector2D((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        if type(other) != Vector2D:
            raise Exception("Invalid type")
        return Vector2D((self.x - other.x), (self.y - other.y))


class Grafico:
    def __init__(self, size=None, xticks=0.1, yticks=0.1, title=None):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax
        if size:
            self.ax.plot([size[0].x, size[1].x], [size[0].y, size[1].y], linestyle="none")
            # self.ax.
            self.ax.set_xticks(np.arange(size[0].x, (size[1].x), xticks))
            self.ax.set_yticks(np.arange(size[0].y, (size[1].y), yticks))
        if title != None:
            self.set_title(title)

    def set_title(self, title):
        self.ax.set_title(title)

    def set_x_interval(self, xticks):
        size = self.ax.get_xlim()
        print(size)
        array = np.arange(round(size[0]), round(size[1]), xticks).tolist()
        print(array)
        self.ax.set_xticks(array)

    def set_y_interval(self, yticks):
        size = self.ax.get_ylim()
        print(size)
        array = np.arange(round(size[0]), round(size[1]), yticks).tolist()
        print(array)
        self.ax.set_yticks(array)

    def set_size(self, size):
        self.ax.set_xlim((size[0].x, size[1].x))
        self.ax.set_ylim((size[0].y, size[1].y))

    def add_arrow(self, vectorto, vectorfrom=Vector2D(), width=1.5, head_width=0.45, head_length=0.5, colore_punta='lightblue', colore_linea='black', linestyle="solid"):
        self.ax.arrow(vectorfrom.x, vectorfrom.y, vectorto.x, vectorto.y, head_length=head_length,
                      head_width=head_width, fc=colore_punta, ec=colore_linea, ls=linestyle)

    def set_grid(self, grid):
        if grid == True:
            self.ax.grid(color='black', ls='-', lw=0.25)
        else:
            self.ax.grid(False)

    def save(self, nomefile="grafico.png"):
        self.fig.savefig(nomefile)
        # plt.show()

    def punta_coda(self, vectors):
        sommavettori = Vector2D()
        for vettore in vectors:
            self.add_arrow(vettore, sommavettori)
            sommavettori += vettore
        self.add_arrow(sommavettori)

    def parallelogramma(self, vectors):
        primovettore = None
        sommavettori = Vector2D()
        for vettore in vectors:
            print(vettore)
            if not primovettore:
                primovettore = vettore
            else:
                self.add_arrow(primovettore, vectorfrom=sommavettori)
                self.add_arrow(vettore, vectorfrom=(
                    sommavettori + primovettore))
                self.add_arrow(primovettore, vectorfrom=(
                    sommavettori + vettore), linestyle="dashed")
                self.add_arrow(vettore, vectorfrom=sommavettori,
                               linestyle="dashed")
                self.add_arrow(primovettore + vettore, vectorfrom=sommavettori)
                sommavettori = sommavettori + primovettore + vettore
                primovettore = vettore
                break

    def plot(self, x, y, type="lines", size=20, pointtype="o", errx=None, erry=None):
        if type == "lines":
            self.ax.plot(x, y)
        elif type == "points":
            self.ax.scatter(x, y, s=size)
        elif type == "+":
            self.ax.scatter(x, y, marker="+", s=size)
        elif type == "xyerrorbars":
            self.ax.errorbar(x, y, errx, erry, fmt=pointtype, capsize=5)
        else:
            print("invalid type")

    def fit(self, x, y):
        x = np.array(x)
        x = np.insert(x, 0, 0)
        x = np.append(x[(len(x)-1)] + x[1], x)

        y = np.array(y)
        y = np.insert(y, 0, 0)
        y = np.append(y[(len(y)-1)] + y[1], y)

        a, b = np.polyfit(x, y, 1)

        self.plot(x, a*x+b)

    def set_xlabel(self, name):
        self.ax.set_xlabel(name)
    def set_ylabel(self, name):
        self.ax.set_ylabel(name)
