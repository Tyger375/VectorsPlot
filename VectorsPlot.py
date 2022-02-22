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
    
xticks=None, yticks=None):
        self.ax.set_xticks(np.arange(size[0].x, (size[1].x + 1), xticks))
      if yticks != None:
        self.ax.set_yticks(np.arange(size[0].y, (size[1].y + 1), yticks))

  def set_title(self, title):
    self.ax.set_title(title)
        
  def set_x_interval(self, xticks):
    size = self.ax.get_xlim()
    self.ax.set_xticks(np.arange(size[0], (size[1] + 1), xticks))
  def set_y_interval(self, xticks):
    size = self.ax.get_ylim()
    self.ax.set_yticks(np.arange(size[0], (size[1] + 1), xticks))

  def set_size(self, size):
    self.ax.set_xlim((size[0].x, size[1].x))
    self.ax.set_ylim((size[0].y, size[1].y))
  
  def add_arrow(self, vectorto, vectorfrom=Vector2D(), width=1.5, head_width=0.45, head_length=0.5, colore_punta='lightblue', colore_linea='black', linestyle="solid"):
    self.ax.arrow(vectorfrom.x, vectorfrom.y, vectorto.x, vectorto.y, head_length=head_length, head_width=head_width, fc=colore_punta, ec=colore_linea, ls=linestyle)

  def set_grid(self, grid):
    if grid == True:
      self.ax.grid(color='black', ls = '-', lw = 0.25)
    else:
      self.ax.grid(False)

