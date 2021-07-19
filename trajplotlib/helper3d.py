"""
3D plots helpers
"""

import numpy as np

def set_equal_axis(ax, xlims, ylims, zlims):
    """Helper function to set equal axis
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        xlims (list): 2-element list containing min and max value of x
        ylims (list): 2-element list containing min and max value of y
        zlims (list): 2-element list containing min and max value of z
    """
    # compute max required range
    max_range = np.array([max(xlims)-min(xlims), max(ylims)-min(ylims), max(zlims)-min(zlims)]).max() / 2.0
    # compute mid-point along each axis
    mid_x = (max(xlims) + min(xlims)) * 0.5
    mid_y = (max(ylims) + min(ylims)) * 0.5
    mid_z = (max(zlims) + min(zlims)) * 0.5
    # set limits to axis
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    return


def get_sphere_coordinates(radius, center=None):
    """Get x,y,z coordinates for sphere

    Args:
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0, 0.0]
    # construct reference sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_sphere = center[0] + radius*np.cos(u)*np.sin(v)
    y_sphere = center[1] + radius*np.sin(u)*np.sin(v)
    z_sphere = center[2] + radius*np.cos(v)
    return x_sphere, y_sphere, z_sphere


def plot_sphere_wireframe(ax, radius, center=None, color="k", linewidth=0.5):
    """Plot sphere wireframe
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        color (str): color
        linewidth (float): linewidth
    """
    x_sphere, y_sphere, z_sphere = get_sphere_coordinates(radius, center)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color=color, linewidth=linewidth)
    return