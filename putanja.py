import matplotlib.pyplot as plt
import numpy as np
import math

R = 4700
visina = 9600
g = 9.81
v_max = 147.22
vt = 350
h = visina

# Iz modela bombe
tp = math.sqrt(2 * visina / g)
D = v_max * tp
print (f'Domet: {D} m') 

alfa_max = 2 * math.atan(R / D)

print (math.pi - alfa_max)

luk_OK = R * (math.pi - alfa_max)
print(f'Duzina luka: {luk_OK} m')

t1 = R * (math.pi - alfa_max) / v_max

print(f'Trajanje skretanja: {t1} s')

# Iz modela aviona
ts = 83.74972931346211

print(f'Talas udara u avion u trenutku : {ts} s')

def grafik(alfa):

	fig, ax = plt.subplots()
	ax.plot([-6000,0], [-R,-R], color='b')

	ax.plot([0,D], [-R,-R], linestyle='--', color='g')

	# Radijus okreta

	fi = math.pi/2 - alfa
	tacke = np.linspace(-math.pi/2, fi , 100)
	xr = list()
	yr = list()

	for x in tacke:
		xr.append(math.cos(x)*R)
		yr.append(math.sin(x)*R)
	    
	
	ax.plot(xr, yr, color='b')
	
	tacke = np.linspace(fi, math.pi/2, 100)
	xr = list()
	yr = list()

	for x in tacke:
		xr.append(math.cos(x)*R)
		yr.append(math.sin(x)*R)
	    
	
	ax.plot(xr, yr, color='b', linestyle='--')

	# Tangenta PK

	kx = D + math.cos(math.pi-alfa)*D
	ky = math.sin(math.pi-alfa)*D -R

	x1 = [kx, D]
	y1 = [ky, -R]
	ax.plot(x1, y1, linestyle='--', color='g')
	
	# Putanja aviona
	
	put = (ts-t1) * v_max
	
	Ax = kx + math.cos(math.pi-alfa) * put
	Ay = ky + math.sin(math.pi-alfa) * put
	
	x1 = [kx, Ax]
	y1 = [ky, Ay]
	ax.plot(x1, y1, color='b')
	
	tacke_x = [0, D, kx, Ax]
	tacke_y = [-R, -R, ky, Ay]
	ax.plot(tacke_x, tacke_y, 'ro')
	
	ax.text(0, -R + 300, ' t0')
	ax.text(D, -R, '  E')
	ax.text(kx, ky, '  t1')
	ax.text(Ax, Ay, '  ts')
	
	plt.show()
	
	
grafik(alfa_max)