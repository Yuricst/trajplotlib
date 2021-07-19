"""
3D plots helpers
"""

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

    