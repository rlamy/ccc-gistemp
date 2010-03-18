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

    def gridplot(self, data):
        """
        Plot gridded data as a heat map.

        data: a 8000-long sequence of data-points corresponding to the subboxes
        returned by eqarea.grid8k, in the same order.
        """
        data = np.asarray(data)
        norm = matplotlib.colors.Normalize()
        norm.autoscale(data)
        for (i, box) in enumerate(the_grid):
            lons, lats = box.submesh()
            x, y = self(*np.meshgrid(lons, lats))
            try:
                self.pcolor(x, y, data[i*100:(i+1)*100].reshape((10,10)), norm=norm)
            except ValueError:  #pcolor raises if none of the subboxes is drawable
                pass
        plt.colorbar()
