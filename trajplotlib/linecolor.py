"""
Helper for line-color for trajectory plotting
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numbers


def get_lc_traj_singleColor(xs, ys, cs, vmin, vmax, cmap, lw=0.8):
    """
    Get line collection object for a trajectory with a single color based on a colormap defined by vmin ~ vmax

    For plotting, run:
        line = ax.add_collection(lc)
        fig.colorbar(line, ax=ax, label="Colorbar label")

    Args:
        xs (np.array): array-like object of x-coordinates of the trajectory
        ys (np.array): array-like object of y-coordinates of the trajectory
        cs (float or np.array): float or array-like object of color-values along the coordinates
        vmin (float): minimum bound on colorbar
        vmax (float): maximum bound on colorbar
        cmap (str): colormap, e.g. 'viridis'
        lw (float): linewidth of trajectory

    Returns:
        (obj): line collection object
    """
    # check if cs is a float, and if it is convert it to an array
    if isinstance(cs, numbers.Real) == True:
    	cs = cs * np.ones((len(xs),))

    # generate segments
    points = np.array([ xs , ys ]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    plt_color = cs

    # create color bar
    norm = plt.Normalize( vmin, vmax )
    lc = LineCollection(segments, cmap=cmap, norm=norm)
    # Set the values used for colormapping
    lc.set_array( plt_color )
    lc.set_linewidth( lw )
    return lc