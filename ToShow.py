#! bin/python

from pylab import *
from matplotlib import patches
from Function import *
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

vmax=5
vmin=-5
cmap='bwr'

PAuse=33.6  # Tobin et al. 2018 for Per-emb-44B
ellip_B=[0.32,0.2] # Tobin et al. 2018 for Per-emb-44B
Inc_use=IncA(ellip_B[0],ellip_B[1])
ellip_A=[0.16,0.093] # Tobin et al. 2018 for Per-emb-44A


fig=figure(figsize=(6,5))
ax=fig.add_subplot(1,1,1)

ax.legend(fontsize='small', ncol=2,loc='upper left')
cax=axes([0.87, 0.1, 0.03, 0.87])
cbar=colorbar(im,cax=cax)
cbar.set_label(r'km s$^{-1}$')
cbar.set_ticks(arange(vmin,vmax,1))
ax.set_xlim(0.4,-0.4)
ax.set_ylim(-0.4,0.4)
ax.set_xlabel(r'$\delta X$ from Per-emb-44B (arcsec)')
ax.set_ylabel(r'$\delta Y$ from Per-emb-44B (arcsec)')
ax.set_aspect('equal')
subplots_adjust(left=0.15,right=0.85,bottom=0.1,top=0.97)

Vmod=img_Model(Vr10=5,xcen=0.,ycen=0.,Inc=Inc_use,PA=-PAuse,mod='Kep')
extent=bound+binn/2
ax.imshow(Vmod,extent=(extent,-extent,-extent,extent),zorder=0,vmax=vmax,vmin=vmin,cmap=cmap,origin='lower')
#ax.contour(Vmod,extent=(extent,-extent,-extent,extent),levels=arange(vmin,vmax,0.5),zorder=1)

savefig('Per-emb-44B_Model.pdf')
show()

