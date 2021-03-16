#! bin/python

from pylab import *
from matplotlib import patches
from Function import *
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

Vr10=10
vmax=5
vmin=-5
cmap='bwr'
extent=bound+binn/2

fig=figure(figsize=(6,5))
ax=fig.add_subplot(1,1,1)

Inc=45;PA=0
class Cursor():
    def __init__(self, ax):
        self.ax = ax
	self.Inc = 45.
    def mouse_move(self,event):
	ax.cla()
	if not event.inaxes:
	    return
	x, y = event.xdata, event.ydata
	self.PA=rad2deg(arctan(x/y))
	self.PA=180+self.PA if y<0 else self.PA

	Vmod=img_Model(Vr10=Vr10,xcen=0.,ycen=0.,Inc=self.Inc,PA=-self.PA,mod='Kep')
	ax.imshow(Vmod,extent=(extent,-extent,-extent,extent),zorder=0,vmax=vmax,vmin=vmin,cmap=cmap,origin='lower')
	ax.annotate(r'$\theta_{\rm inc}$='+'%.d'%self.Inc+'$^\circ$',xycoords='axes fraction',xy=(0.05,0.9))
	ax.annotate(r'$PA$='+'%.d'%self.PA+'$^\circ$',xycoords='axes fraction',xy=(0.05,0.8))
	setup(self.ax)
	plt.draw()

    def scrolling(self,event):
	ax.cla()
        if event.button=='up':
          self.Inc += 2
        elif event.button=='down':
          self.Inc -= 2
	Vmod=img_Model(Vr10=Vr10,xcen=0.,ycen=0.,Inc=self.Inc,PA=-self.PA,mod='Kep')
	ax.imshow(Vmod,extent=(extent,-extent,-extent,extent),zorder=0,vmax=vmax,vmin=vmin,cmap=cmap,origin='lower')
	ax.annotate(r'$\theta_{\rm inc}$='+'%.d'%self.Inc+'$^\circ$',xycoords='axes fraction',xy=(0.05,0.9))
	ax.annotate(r'$PA$='+'%.d'%self.PA+'$^\circ$',xycoords='axes fraction',xy=(0.05,0.8))
	setup(self.ax)
	plt.draw()

def setup(ax):
	ax.set_xlim(0.4,-0.4)
	ax.set_ylim(-0.4,0.4)
	ax.set_xlabel(r'$\delta X$ (arcsec)')
	ax.set_ylabel(r'$\delta Y$ (arcsec)')
	ax.set_aspect('equal')
	
mouse=Cursor(ax)
connect('motion_notify_event', mouse.mouse_move)
connect('scroll_event', mouse.scrolling)

setup(ax)
cax=axes([0.87, 0.1, 0.03, 0.87])
Vmod=img_Model(Vr10=10,xcen=0.,ycen=0.,Inc=Inc,PA=PA,mod='Kep')
im=ax.imshow(Vmod,extent=(extent,-extent,-extent,extent),zorder=0,vmax=vmax,vmin=vmin,cmap=cmap,origin='lower')
cbar=colorbar(im,cax=cax)
cbar.set_label(r'km s$^{-1}$')
cbar.set_ticks(arange(vmin,vmax,1))
subplots_adjust(left=0.15,right=0.85,bottom=0.1,top=0.97)


show()

