#! bin/python

from pylab import *
from matplotlib import patches
from Function import *
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

class Cursor():
    def __init__(self, ax):
        self.Inc = 45.
        self.PA = 0
        self.Vr10 = 10
        self.vmax = 5
        self.vmin = -5
        self.cmap = 'bwr'
        self.extent = bound+binn/2
        self.ax = ax
        self.figure_layout()  # preset the layout

    def draw_figure(self, Vmod):

        self.ax.cla()  # clear the main axes
        self.cax.cla()  # clear the colorbar
        im = self.ax.imshow(Vmod, extent=(self.extent, -self.extent, -self.extent, self.extent), zorder=0,
                       vmax=self.vmax, vmin=self.vmin, cmap=self.cmap, origin='lower')
        self.ax.annotate(r'$\theta_{\rm inc}$='+'%.d'%self.Inc+'$^\circ$',
                         xycoords='axes fraction', xy=(0.05, 0.9))
        self.ax.annotate(r'$PA$='+'%.d'%self.PA+'$^\circ$',
                         xycoords='axes fraction', xy=(0.05, 0.8))
        self.figure_layout()
        cbar = colorbar(im,cax=self.cax)
        cbar.set_label(r'km s$^{-1}$')
        cbar.set_ticks(arange(self.vmin, self.vmax,1))
        plt.draw()

    def figure_layout(self):

        self.ax.set_xlim(0.4, -0.4)
        self.ax.set_ylim(-0.4, 0.4)
        self.ax.set_xlabel(r'$\delta X$ (arcsec)')
        self.ax.set_ylabel(r'$\delta Y$ (arcsec)')
        self.ax.set_aspect('equal')
        self.cax = axes([0.87, 0.1, 0.03, 0.87])
        subplots_adjust(left=0.15, right=0.85, bottom=0.1, top=0.97)

    def mouse_move(self,event):
        if not event.inaxes:
            return
        x, y = event.xdata, event.ydata
        self.PA=rad2deg(arctan(x/y))
        self.PA=180+self.PA if y<0 else self.PA

        Vmod=img_Model(Vr10=self.Vr10,xcen=0.,ycen=0.,Inc=self.Inc,PA=-self.PA,mod='Kep')
        self.draw_figure(Vmod)

    def scrolling(self,event):
        if event.button=='up':
            self.Inc += 2
        elif event.button=='down':
            self.Inc -= 2
        Vmod=img_Model(Vr10=self.Vr10,xcen=0.,ycen=0.,Inc=self.Inc,PA=-self.PA,mod='Kep')
        self.draw_figure(Vmod)

fig = figure(figsize=(6, 5))
ax = fig.add_subplot(1, 1, 1)

disk_model = Cursor(ax)
#disk_model.Vr10 = 8
#disk_model.cmap = 'jet'
mouse = disk_model
connect('motion_notify_event', mouse.mouse_move)
connect('scroll_event', mouse.scrolling)
Vmod=img_Model(Vr10=disk_model.Vr10,xcen=0.,ycen=0.,Inc=disk_model.Inc,PA=-disk_model.PA,mod='Kep')
disk_model.draw_figure(Vmod)

show()

