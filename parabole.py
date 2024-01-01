import matplotlib.pyplot as plt
import numpy as np
""" lecture des données t,x et y contenues dans le fichier .................."""
from pylab import *
""" ---------------------------------
        CHOIX du PROFESSEUR
------------------------------------- """
# 'avimeca'         (crééer un fichier TXT en export)
t,x,y=loadtxt('parabole.txt', skiprows=1,unpack=True)

"""  GRAPHE  y(x)     ..................................................."""
plot(x,y,'*k:')
xlabel('x(m)');  ylabel('y(m)')

""" rajout vecteur V sur GRAPHE  ..........................................."""
# les vecteurs V depuis le second point jusqu'à l'avant-dernier ................
for i in range(1,len(t)-1):
    vx=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    vy=(y[i+1]-y[i-1])/(t[i+1]-t[i-1])
    arrow(x[i], y[i], vx/10, vy/10,  head_width=0.02, head_length=0.02,color='r',length_includes_head= True,lw=0.5)

""" rajout vecteur a sur GRAPHE  ..........................................."""
# les vecteurs a depuis le troisième point jusqu'à l'antépénultième ............
for i in range(2,len(t)-2):
    vxiplus1=(x[i+2]-x[i])/(t[i+2]-t[i]);   vximoins1=(x[i]-x[i-2])/(t[i]-t[i-2]) ; deltaVx = (vxiplus1-vximoins1)/(t[i+1]-t[i-1])
    vyiplus1=(y[i+2]-y[i])/(t[i+2]-t[i]);   vyimoins1=(y[i]-y[i-2])/(t[i]-t[i-2]) ; deltaVy = (vyiplus1-vyimoins1)/(t[i+1]-t[i-1])
    arrow(x[i], y[i], deltaVx/30, deltaVy/30,  head_width=0.02, head_length=0.02,color='g',length_includes_head= True,lw=0.5)

"""  affichage  ..............................................."""
plt.show()

