#mod8(202313211021) = 5 
import numpy as np

def enerjiFormulu(theta, I, alpha):
    return I * np.cos(theta - alpha)

def gradientHesaplama(theta, I, alpha):
    return -I * np.sin(theta - alpha)

saatLineerAralik = np.array([11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5])

#Isik siddeti W/m^2ile hesaplanir
isikSiddeti = np.array([850, 900, 950, 925, 875, 800, 700, 550, 300])

#Gunes acisi derece ile hesaplanir
GunesAcisi = np.array([65, 70, 75, 72, 68, 60, 50, 35, 15])


#Saat 17:00 teki interpolasyon
zaman = 17.0
zamanadakiIsikSiddeti = np.interp(zaman, saatLineerAralik, isikSiddeti)
zamandakiAlpha = np.interp(zaman, saatLineerAralik, GunesAcisi)
zamandakiAlphaRadiani = np.radians(zamandakiAlpha)

# E(theta)'yi maksimize etmek icin egim artisi
theta = 0.0
thetaRadiani = np.radians(theta)
egimArtisi = 0.1
tolerans = 0.000001
maxIterasyon = 1000

#zamandaki max enerji
maxEnerji = enerjiFormulu(thetaRadiani,zamanadakiIsikSiddeti,zamandakiAlphaRadiani)
for _ in range(maxIterasyon):
    grad = gradientHesaplama(theta, zamanadakiIsikSiddeti, zamandakiAlphaRadiani)
    thetaYeni = theta + egimArtisi * grad
    if abs(thetaYeni - theta) < tolerans:
        break
    theta = thetaYeni

# Theta'nin [0, 2*pi] icinde oldugundan emin olun
optimumThetaRad = theta % (2 * np.pi)
optimumThetaDer = np.degrees(optimumThetaRad)

# Sonuc:
print(f"Hesaplanacak saat: {zaman}")
print(f"Enterpolasyon Işık şiddeti (I): {zamanadakiIsikSiddeti} W/m^2")
print(f"Enterpolasyon Güneş Açı (α): {zamandakiAlpha} degrees ({zamandakiAlphaRadiani:.5f} radians)")
print(f"Optimum θ: {optimumThetaRad:.2f} radians ({optimumThetaDer:.2f} derece)")
print(f"Maksimum Enerji: {maxEnerji:.2f} W/m^2")