"""
2D plots helpers
"""

import numpy as np
import matplotlib.pyplot as plt


def quickplot2(xs, ys, ax=None, n_figsize=5,
        lw_traj=0.75, c_traj="navy", 
        radius: float=None, center=None,
        scatter_start=True, marker_start="x", c_start="r", 
        scatter_end=True, marker_end="*", c_end="g"):
	return