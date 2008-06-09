from pylab import *
from matplotlib.patches import Ellipse
from matplotlib.collections import LineCollection
from matplotlib.colors import colorConverter

def plot_curve(x, color=None, label=None, ax=None):
    points = zip(1-x[1],1-x[0])
    segments = zip(points[:-1], points[1:])
    if ax is None:
        ax = axes(frameon=True)
    LC = LineCollection(segments, label=label)
    if not (color is None):
        LC.color(color)
    ax.add_collection(LC)
    axis([0, 1, 0, 1])
