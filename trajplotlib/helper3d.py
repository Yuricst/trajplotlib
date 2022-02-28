"""
3D plots helpers
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import CubicSpline


def set_equal_axis(ax, xlims, ylims, zlims, scale=1.0, dim3=True):
    """Helper function to set equal axis
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        xlims (list): 2-element list containing min and max value of x
        ylims (list): 2-element list containing min and max value of y
        zlims (list): 2-element list containing min and max value of z
        scale (float): scaling factor along x,y,z
        dim3 (bool): whether to also set z-limits (True for 3D plots)
    """
    # compute max required range
    max_range = np.array([max(xlims)-min(xlims), max(ylims)-min(ylims), max(zlims)-min(zlims)]).max() / 2.0
    # compute mid-point along each axis
    mid_x = (max(xlims) + min(xlims)) * 0.5
    mid_y = (max(ylims) + min(ylims)) * 0.5
    mid_z = (max(zlims) + min(zlims)) * 0.5
    # set limits to axis
    if dim3==True:
        ax.set_box_aspect((max_range, max_range, max_range))
    ax.set_xlim(mid_x - max_range*scale, mid_x + max_range*scale)
    ax.set_ylim(mid_y - max_range*scale, mid_y + max_range*scale)
    if dim3==True:
        ax.set_zlim(mid_z - max_range*scale, mid_z + max_range*scale)
    return


def get_sphere_coordinates(radius, center=None):
    """Get x,y,z coordinates for sphere

    Args:
        radius (float): sphere radius
        center (list): x,y,z coordinates of center; if None, set to [0.0, 0.0, 0.0]
    
    Returns:
        (tuple): x, y, z coordinates of sphere
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0, 0.0]
    # construct reference sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    #u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_sphere = center[0] + radius*np.cos(u)*np.sin(v)
    y_sphere = center[1] + radius*np.sin(u)*np.sin(v)
    z_sphere = center[2] + radius*np.cos(v)
    return x_sphere, y_sphere, z_sphere



def get_circle_coordinates(radius, center=None, n=50):
    """Get x,y,z coordinates for circle
    
    Args:
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0]
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0]
    thetas = np.linspace(0, 2*np.pi, n)
    x_circle, y_circle = [], []
    for theta in thetas:
        x_circle.append(center[0] + radius*np.cos(theta))
        y_circle.append(center[1] + radius*np.sin(theta))
    return x_circle, y_circle


def plot_sphere_wireframe(ax, radius, center=None, color="k", linewidth=0.5):
    """Plot sphere wireframe
    
    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        radius (float): radius
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        color (str): color of wireframe
        linewidth (float): linewidth of wireframe
    """
    x_sphere, y_sphere, z_sphere = get_sphere_coordinates(radius, center)
    ax.plot_wireframe(x_sphere, y_sphere, z_sphere, color=color, linewidth=linewidth)
    return


def get_ellipsoid_coordinates(rx, ry, rz, center=None, n=60):
    """Get x,y,z coordinates for ellipsoid

    Args:
        rx (float): radius in x-direction
        ry (float): radius in y-direction
        rz (float): radius in z-direction
        center (list): x,y,z coordinates of center; if None, set to [0.0, 0.0, 0.0]
        n (int): number of points to be used in each mesh direction

    Returns:
        (tuple): x, y, z coordinates of ellipsoid
    """
    # check if center is provided
    if center is None:
        center = [0.0, 0.0, 0.0]

    # grid setup
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)

    # Cartesian coordinates of ellipsoid
    x_el = center[0] + rx * np.outer(np.cos(u), np.sin(v))
    y_el = center[1] + ry * np.outer(np.sin(u), np.sin(v))
    z_el = center[2] +rz * np.outer(np.ones_like(u), np.cos(v))
    return x_el, y_el, z_el


def plot_ellipsoid_wireframe(ax, rx, ry, rz, center=None, color="k", linewidth=0.5, n=60):
    """Plot ellipsoid wireframe

    Args:
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`
        rx (float): radius in x-direction
        ry (float): radius in y-direction
        rz (float): radius in z-direction
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        color (str): color of wireframe
        linewidth (float): linewidth of wireframe
        n (int): number of points to be used in each mesh direction
    """
    x_el, y_el, z_el = get_ellipsoid_coordinates(rx, ry, rz, center=center, n=n)
    ax.plot_wireframe(x_el, y_el, z_el, color=color, linewidth=linewidth)
    return


def quickplot3(xs, ys, zs, ax=None, n_figsize=5, scale=1.0,
        lw_traj=0.75, c_traj="navy", 
        radius: float=None, center=None, label=None,
        scatter_start=True, marker_start="x", c_start="r", 
        scatter_end=True, marker_end="*", c_end="g",
        background=False,
        facecolor=None):
    """Plot 3D trajectory around body. 
    If `ax` is not provided, a new `matplotlib` trajectory is initialized. 
    If `ax` is provided, the trajectory is appended. 
    
    Args:
        xs (ndarray): x-coordinates of trajectory
        ys (ndarray): y-coordinates of trajectory
        zs (ndarray): z-coordinates of trajectory
        ax (Axes3DSubplot): matplotlib 3D axis, created by `ax = fig.add_subplot(projection='3d')`. If set to None, new set of axis is created. 
        n_figsize (int): fig_size is set to (n_figsize, n_figsize)
        scale (float): scaling factor along x,y,z
        lw_traj (float): linewidth for trajectory
        c_traj (str): color for trajectory
        radius (float): radius of sphere at the center
        center (list): x,y,z coordinates of center, if None set to [0.0, 0.0, 0.0]
        scatter_start (bool): whether to plot marker at the beginning of trajectory
        marker_start (str): marker at the beginning of trajectory
        c_start (str): marker color at the beginning of trajectory
        scatter_end (bool): whether to plot marker at the end of trajectory
        marker_end (str): marker at the end of trajectory
        c_end (str): marker color at the end of trajectory
        background (bool): whether to plot gray box at the background
    """
    if ax is None:
        fig = plt.figure(figsize=(n_figsize,n_figsize))
        ax = fig.add_subplot(projection='3d')
        # reference sphere around asteroid
        if radius is not None:
            plot_sphere_wireframe(ax, radius, center=center, color="k", linewidth=0.5)
        # equal size grid
        xlims = [min(xs), max(xs)]
        ylims = [min(ys), max(ys)]
        zlims = [min(zs), max(zs)]
        set_equal_axis(ax, xlims, ylims, zlims, scale)
    else:
        fig = None
    # plot trajectory
    ax.plot(xs, ys, zs, linewidth=lw_traj, c=c_traj, label=label)
    # scatter at the beginning/end of trajectory
    if scatter_end is True:
        ax.scatter(xs[0], ys[0], zs[0], marker=marker_start, c=c_start)
    if scatter_end is True:
        ax.scatter(xs[-1], ys[-1], zs[-1], marker=marker_end, c=c_end)
    # turn off background
    if background is False:
        ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
        ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    if facecolor is not None:
        ax.set_facecolor(facecolor)
        fig.set_facecolor(facecolor)
    # return Axes3DSubplot object
    return fig, ax


def animate_trajectory_3d(
        xs, 
        ys, 
        zs, 
        times, 
        nt=100, 
        multiple_traj=False, 
        scale=1.2, 
        fig=None, 
        filename=None, 
        interval=20, 
        repeat_delay=0, 
        fps=20, 
        lw_traj=0.5, 
        c_traj='navy'
    ):
    """Animate trajectory in 3D using `matplotlib.animation.FuncAnimation`

    Args:
        xs (lst): list or list of multiple trajectories' list of x-coordinates
        ys (lst): list or list of multiple trajectories' list of y-coordinates
        zs (lst): list or list of multiple trajectories' list of z-coordinates
        times (lst): list of time-stamps corresponding to states xs, ys, zs
        nt (int): number of steps to use for interpolating and creating animation
        multiple_traj (bool): whether xs,ys,zs are lists (False) or lists of lists (True)
        scale (float): scaling for setting limits on axis
        fig (matplot): if previous figure has been created
        filename (str): FIXME!! saving gif file, not supported for multiple animations
        
    Returns:
        (tuple): fig, ax, list of animations
    """
    assert len(xs) == len(ys) == len(zs) == len(times), "xs, ys, zs, and times must be of equal length"

    # clean up data if time is not strictly increasing
    ordered_time = all(i < j for i, j in zip(times, times[1:]))
    if ordered_time == False:
        t_ordered, xs_ordered, ys_ordered, zs_ordered = [], [], [], []
        if multiple_traj is False:
            assert len(times) == len(xs) == len(ys) == len(zs)
            for j in range(len(times)-1):
                if times[j] < times[j+1]:  # if strictly less than next time-step
                    t_ordered.append(times[j])
                    xs_ordered.append( xs[j] )
                    ys_ordered.append( ys[j] )
                    zs_ordered.append( zs[j] )
        else:
            for i_traj in range(len(xs)):
                assert len(times) == len(xs[i_traj]) == len(ys[i_traj]) == len(zs[i_traj])
                xi_ordered, yi_ordered, zi_ordered = [], [], []
                for j in range(len(times)-1):
                    if times[j] < times[j+1]:  # if strictly less than next time-step
                        if i_traj == 0:
                            t_ordered.append(times[j])
                        xi_ordered.append( xs[i_traj][j] )
                        yi_ordered.append( ys[i_traj][j] )
                        zi_ordered.append( zs[i_traj][j] )
                xs_ordered.append( xi_ordered )
                ys_ordered.append( yi_ordered )
                zs_ordered.append( zi_ordered )

    else:
        t_ordered = times
        xs_ordered = xs
        ys_ordered = ys
        zs_ordered = zs

    # create inerpolation
    if multiple_traj is False:
        cxs = CubicSpline(t_ordered, xs_ordered)
        cys = CubicSpline(t_ordered, ys_ordered)
        czs = CubicSpline(t_ordered, zs_ordered)
        t_interp = np.linspace(t_ordered[0], t_ordered[-1], nt)
        xs_interp = cxs(t_interp)
        ys_interp = cys(t_interp)
        zs_interp = czs(t_interp)

    else:
        xs_interp, ys_interp, zs_interp = [], [], []
        for i_traj in range(len(xs_ordered)):
            cxs = CubicSpline(t_ordered, xs_ordered[i_traj])
            cys = CubicSpline(t_ordered, ys_ordered[i_traj])
            czs = CubicSpline(t_ordered, zs_ordered[i_traj])
            t_interp = np.linspace(times[0], times[-1], nt)
            xs_interp.append( cxs(t_interp) )
            ys_interp.append( cys(t_interp) )
            zs_interp.append( czs(t_interp) )

    # prep base figure if none is provided
    if fig is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # set equal axis
        if multiple_traj is False:
            xlims = [min(xs_interp), max(xs_interp)]
            ylims = [min(ys_interp), max(ys_interp)]
            zlims = [min(zs_interp), max(zs_interp)]
        else:
            xlims = [min(xs_interp[0]), max(xs_interp[0])]
            ylims = [min(ys_interp[0]), max(ys_interp[0])]
            zlims = [min(zs_interp[0]), max(zs_interp[0])]
        set_equal_axis(ax, xlims, ylims, zlims, scale=scale, dim3=True)

    # prep drawing funciton
    def update_frame(num, dataSet, line):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(dataSet[0:2, :num])    
        line.set_3d_properties(dataSet[2, :num])    
        return line

    if multiple_traj is False:
        dataSet = np.array([xs_interp, ys_interp, zs_interp])
        # NOTE: Can't pass empty arrays into 3d version of plot()
        line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=lw_traj, c=c_traj)[0] # For line plot
        anis = animation.FuncAnimation(fig, update_frame, frames=len(t_interp), fargs=(dataSet,line), interval=interval, repeat=True, repeat_delay=repeat_delay, blit=False)

    else:   # multiple trajectory (multiple_traj==True case)
        anis = []
        for i_traj in range(len(xs_interp)):
            dataSet = np.array([xs_interp[i_traj], ys_interp[i_traj], zs_interp[i_traj]])
            # NOTE: Can't pass empty arrays into 3d version of plot()
            line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=lw_traj, c=c_traj[i_traj])[0] # For line plot
            anis.append( animation.FuncAnimation(fig, update_frame, frames=len(t_interp), fargs=(dataSet,line), interval=interval, repeat=True, repeat_delay=repeat_delay, blit=False)
            )

    if filename is not None:
        ani.save(fn+'.gif',writer='imagemagick',fps=fps)
    return fig, ax, anis
