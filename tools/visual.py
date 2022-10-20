##
## visualization tools
##

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

colors = mpl.rcParams['axes.prop_cycle'].by_key()['color']

# plot a function over a given range
# optionally include dashed zero line
def plot(f, x0, x1, N=100, ax=None, zero=None, **kwargs):
    if ax is None:
        fig, ax = plt.subplots()
    x = np.linspace(x0, x1, N)
    y = f(x)
    ax.plot(x, y, **kwargs)
    if zero is not None:
        ax.hlines(zero, *ax.get_xlim(), color='k', linestyle='--', linewidth=1, zorder=-1)

def plot_homotopy(ppath, xpaths, rzero=None, czero=None, equal=True, axs=None):
    if axs is None:
        _, axs = plt.subplots(ncols=2, figsize=(10, 4))

    if rzero is not None:
        axs[0].plot(rzero, ppath, linewidth=1, color='k', linestyle='--')
    if czero is not None:
        axs[1].plot(czero, ppath, linewidth=1, color='k', linestyle='--')

    for xp in xpaths:
        axs[0].plot(xp.real, ppath.real)
        axs[1].plot(xp.imag, ppath.real)

    if equal:
        axs[0].set_aspect('equal')
        axs[1].set_aspect('equal')

    axs[0].set_xlabel('Solution (Real)')
    axs[1].set_xlabel('Solution (Imaginary)')
    axs[0].set_ylabel('Parameter')
