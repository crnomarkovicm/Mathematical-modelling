import matplotlib.pyplot as plt
import math

visina = 9600
g = 9.81
v_max = 147.22

# domet (D) = Vmax * t
# t = sqrt ( 2 * h / g )
# D = Vmax * sqrt (2 * h / g)

t = math.sqrt(2 * visina / g)
print (f'Trajanje pada: {t} s')

domet = v_max * t
print (f'Domet bombe: {domet} m') 

# Za iscrtavanje grafika proveravamo gde se projektil
# nalazi na svakih 50 metara

x_tacke = list(range(0, int(domet + 50), 50))
y_tacke = list()

# Visinski pad dobijamo sa:
# h = g / 2 * (x / Vmax)^2
# gde je x predjeni put po x
# ako od visine oduznemo pad
# dobijamo trenutni polozaj

for x in x_tacke: 
    y_tacke.append(visina - g/2*(x/v_max)**2)

# Iscrtavanje grafika
fig, ax = plt.subplots()
ax.plot(x_tacke, y_tacke)
ax.plot([0, domet], [visina,0], 'ro')
ax.text(0, visina, '  h0 = 9600m')
ax.text(domet-1800, 0, f'D = {round(domet,3)} m')
ax.set_xlabel('Daljina (m)')
ax.set_ylabel('Visina (m)')
ax.set_title('Model bombe')
plt.show()