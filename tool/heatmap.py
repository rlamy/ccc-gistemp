#!/usr/bin/env python
"""
Create raster maps of subbox-gridded data.
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from code import eqarea

the_grid = list(eqarea.smartgrid())

class GridMap(Basemap):

    def __init__(self, *args, **kwargs):
        Basemap.__init__(self, *args, **kwargs)
        self.drawmapboundary()
        self.drawcoastlines()

    def gridplot(self, data, colorbar=True):
        """
        Plot gridded data as a heat map.

        data: an 8000-item sequence of data-points corresponding to the subboxes
        returned by eqarea.grid8k, in the same order.

        colorbar: whether to draw the colorbar
        """
        data = np.asanyarray(data)
        vmax, vmin = data.max(), data.min()
        for (i, box) in enumerate(the_grid):
            lons, lats = box.submesh()
            x, y = self(*np.meshgrid(lons, lats))
            try:
                self.pcolor(x, y, data[i*100:(i+1)*100].reshape((10,10)),
                                                        vmax=vmax, vmin=vmin)
            except ValueError:  #pcolor raises if none of the subboxes is drawable
                pass
        if colorbar:
            self.add_colorbar()

    def add_colorbar(self, orientation=None):
        """
        Add a colorbar with specified orientation.

        If the orientation isn't specified, choose vertical or horizontal based
        on aspect ratio.
        """
        if orientation is None:
            if self.aspect <0.6:
                orientation = 'h'
            else:
                orientation = 'v'
        plt.colorbar(orientation=orientation)

