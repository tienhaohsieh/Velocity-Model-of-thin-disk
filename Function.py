#! bin/python
from numpy import *

dis=293 #pc
bound=0.5;binn=0.01
ran=arange(-bound,bound,binn)
xx_obs,yy_obs=meshgrid(-ran,ran)

def V_kep(R,Vr10):
    outV=Vr10*(R/10)**-0.5
    return outV
def V_AM(R,Vr10):
    outV=Vr10*(R/10)**-1.
    return outV
def IMrot(xx,yy,PA):
    PA=deg2rad(-PA)
    xx_p=cos(PA)*xx-sin(PA)*yy
    yy_p=sin(PA)*xx+cos(PA)*yy
    return xx_p,yy_p
def IncA(Long,Short):
    ratio=Short/Long
    if ratio>=1:
        ratio=1./ratio
    outA=rad2deg(arccos(ratio))
    return outA

def img_Model(Vr10,xcen,ycen,Inc=0,PA=0,mod='Kep'):
    Inc=deg2rad(Inc)

    xx,yy=IMrot(xx_obs-xcen,yy_obs-ycen,PA)
    xx=(xx)/cos(Inc)*dis  # arcsec to au
    yy=(yy)*dis

    R=( xx**2 + yy**2 )**0.5
    theta=arctan( xx/yy )
    if mod=='Kep':
        Vobs=V_kep(R,Vr10)*cos(theta)*sin(Inc)
    if mod=='AM':
        Vobs=V_AM(R,Vr10)*cos(theta)*sin(Inc)
    Vobs[yy<0]=-Vobs[yy<0]
    Vobs[R>100]=0
    return Vobs

def RV(x_obs,y_obs,v_obs,xcen,ycen,Inc=0,PA=0):
    Inc=deg2rad(Inc)

    x,y=IMrot(x_obs-xcen,y_obs-ycen,PA)
    x=(x)/cos(Inc)*dis  # arcsec to au
    y=(y)*dis

    R=(x**2+y**2)**0.5
    theta=arctan(x/y)
    V=v_obs/(cos(theta)*sin(Inc))
    return R,V


