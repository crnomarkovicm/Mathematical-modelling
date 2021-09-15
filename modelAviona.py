
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math

#Pocetni uslovi
R = 4700
h = 9600
g = 9.81
v_max = 147.22
vt = 350
v = v_max

#Pozicija bombe, D je daljina na koju je bomba pala
tb = math.sqrt(2 * h / g)
D = v_max * tb

#Vreme skretanja aviona
def t_1(fi):
	return R * fi / v

#Pozicija aviona u datom trenutku
def x(t_s, fi, t1):
	return v * math.cos(fi)*(t_s - t1) + R * math.sin(fi)

def y(t_s, fi, t1):
	return v * math.sin(fi)*(t_s - t1) + R * (1- math.cos(fi))
	


#Udaljenost na kojoj se avion nalazi u trenutku kada ga udarni talas stigne
def d(fi, ts):
	t1 = t_1(fi)
	x_ts = x(ts, fi, t1)
	y_ts = y(ts, fi, t1)
	return math.sqrt((x_ts-D)**2 + y_ts**2 + h**2) 

#Poluprecnik udarnog talasa u trenutku t
def r(t):
	return vt * (t-tb)
	

#Nizovi u kojima cemo cuvati vreme kretanja t i udaljenost d (koliko je avion udaljen od mesta eksplozije)
niz_t = list()
niz_d = list()

maks_fi = 0

#Uzimamo za ugao fi vrednosti 0-pi i racunamo vreme kretanja i udaljenost na kojoj ce se avion nalaziti ukoliko skrene za ugao fi
for fi in range(0,round(math.pi*1000)):
	fi = fi/1000
	
	def func(ts):
		return d(fi,ts) - r(ts)
		
	root = fsolve(func, 10)
	if(root[0] - t_1(fi) <= 0):
		niz_t.append(root[0])
		niz_d.append(r(root[0]))
		maks_d = r(root[0])
		print(maks_d)
		print(fi)
		for fi_2 in range(round(fi*1000),round(math.pi*1000)):
			fi = fi/1000
			niz_d.append(maks_d)
		break;
		
		
	niz_t.append(root[0])
	niz_d.append(r(root[0]))
	
#Pronalazimo maksimalnu udaljenost aviona od mesta eksplozije, i vreme kretanja za koje je ona postignuta
max_d = max(niz_d)
ugao = niz_d.index(max_d)
ts = niz_t[ugao]

max_d = max(niz_d)
ugao = niz_d.index(max_d)
ts = niz_t[ugao]


print (f'Ugao skretanja: {ugao/1000} rad')
print (f'Trenutak sudara sa talasom: {ts} s')
print (f'Udaljenost od mesta eksplozije {max_d} m')


#Ovaj grafik prikazuje kako se udaljenost menja sa vremenom
x = list()
for i in range(len(niz_d)):
	x.append(i/1000);

fig, ax = plt.subplots()

ax.plot(x, niz_d)
ax.plot([x[ugao]], [max_d], 'ro')
ax.text(x[ugao], max_d, f'  d = {round(max_d, 2)} m')
ax.set_xlabel('Ugao (rad)')
ax.set_ylabel('Daljina (m)')
ax.set_title('Maksimalna daljina')

plt.show()
