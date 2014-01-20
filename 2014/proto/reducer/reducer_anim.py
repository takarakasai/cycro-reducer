#!/opt/local/bin/ipython-2.7

import matplotlib.pyplot
import matplotlib.animation as animation

fig = matplotlib.pyplot.figure(1,(6,6),80,'w','k')
ax = fig.add_subplot(111)
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)

#rc,rm,rd = 72,4,1
rc,rm,rd = 36,4,2

def lot_xy(x,y,sita):
  return x*cos(sita)+y*sin(sita), -x*sin(sita)+y*cos(sita)

def plot_circle(posx,posy,r,linetype='red'):
  sita = linspace(-pi,pi,100)
  x,y = r*cos(sita) + posx, r*sin(sita) + posy
  plot(x,y,linetype)

def plot_circles(num,cr,r):
  for sita in linspace(-pi,pi,num+1):
    plot_circle(cr*cos(sita), cr*sin(sita), r)

def plot_planetary_circles(num, posx, posy, cr, r, rot_sita = 0, linetype ='red'):
  for sita in linspace(-pi,pi,num+1):
    x1,y1 = lot_xy(cr*cos(sita), cr*sin(sita), rot_sita)
    plot_circle(x1 + posx, y1 + posy, r, linetype)

def plot_torochoid(offset_x, offset_y, offset_sita):
  sita = linspace(-np.pi,np.pi,100) 
  offset_sita = offset_sita * rm / rc
  x = (rc+rm)*np.cos(sita)-rd*np.cos((rc+rm)/rm*sita)
  y = (rc+rm)*np.sin(sita)-rd*np.sin((rc+rm)/rm*sita) 
  x1,y1 = lot_xy(x,y,offset_sita)
  x1 = x1 + offset_x
  y1 = y1 + offset_y
  clf()
  xlim(-rc*1.4,rc*1.4)
  ylim(-rc*1.4,rc*1.4)
  plot_circles(rc/rm+1,rc+rm+rd,rd)
  plot_circle(0,0,rc+rm+rd*2)
  print '%f' % offset_sita
  plot_circle(offset_x, offset_y,rm)
  plot_planetary_circles(8, offset_x, offset_y, rc*2/3, 4, offset_sita)
  plot_planetary_circles(8, 0, 0, rc*2/3, 2, offset_sita, 'blue')
  plot_circle(0,0,rc*2/3)
  plot_circle(0,0,rm+rd)
  plot(rc*cos(sita),rc*sin(sita),'blue',x1,y1,'red')

sita = linspace(-np.pi*3,np.pi*3,100)
def timer_handler(i):
  plot_torochoid(rd*cos(sita[i]),rd*sin(sita[i]),sita[i])

anim = animation.FuncAnimation(fig,timer_handler,frames=100,interval=100)
show()

