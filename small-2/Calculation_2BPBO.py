# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:15:28 2024

@author: ansell
"""
#2BPBO

import numpy as np
#a = 10
#b = 2
#c = np.sqrt(b)
#print('c =',c)

#NO UNIT COMMENT = SI units
sigma_DFT = 7.1594725   #hbar/e S/cm
hbar = 1.055e-34
h =  2*np.pi*hbar
e = 1.602e-19           #Buat ubah dari eV ke joule  
m_e = 9.109e-31
c = 3e+8
#Slopes are obtained from quadratic approximation of a nearest band to the Fermi level
slope_1 = 19.988e-19/e
m_1 = (hbar**2)/(2*e**2 *slope_1)
slope_2 = 28.925e-19/e
m_2 = (hbar**2)/(2*e**2 *slope_2)
m = (m_1 + m_2)/(2)
Ef = 9.4724*e
n_imp = 0.05
N_0 = 2.66/e
elcond = 1.447e+6
#kf = "{:e}".format(np.sqrt(2*m*Ef/hbar**2))
kf = np.sqrt(2*m*Ef/hbar**2)
etaBarSO = (hbar * kf/(2 * m * c))**2

b_SJ = 2*etaBarSO* e**2 *kf /(3*np.pi*h)
V_imp = np.sqrt(hbar**2 * kf**2 * b_SJ/(2 * np.pi * m * n_imp * etaBarSO * N_0 * elcond))
a_SS = 2*np.pi*etaBarSO*N_0*V_imp/3
sigma_SS = a_SS * elcond * 2
sigma_SJ = b_SJ*2 
sigma_berry = sigma_DFT*2e+2
sigma_theoretical = sigma_berry + sigma_SJ + sigma_SS
sigma_experiment = 2.3e+5

comparison = sigma_experiment/sigma_theoretical

print('')
print('QUADRATIC APPROX')
print('Effective mass left =',"{:e}".format(m_1), 'kg')
print('Effective mass right =',"{:e}".format(m_2), 'kg')
print('Effective mass =',"{:e}".format(m), 'kg')
print('kf =',"{:e}".format(kf), '1/m')
print('etaBarSO =',"{:e}".format(etaBarSO))
print('b_SJ =',"{:e}".format(b_SJ), 'S/m')
print('Mass =', "{:e}".format(m), 'kg')
#print('', "{:e}".format(), 'unit')
print('V_imp =', "{:e}".format(V_imp), 'J')
print('a_SS =', "{:e}".format(a_SS))
print('Electrical Conductivity =', "{:e}".format(2*elcond), 'hbar/2e S/m')
print('')
print('SHC side jump =', "{:e}".format(sigma_SJ),'hbar/2e S/m')
print('SHC skew scattering =', "{:e}".format(sigma_SS), 'hbar/2e S/m')
print('SHAngle side jump =', "{:e}".format(sigma_SJ/(2*elcond)),'dimensionless')
print('SHAngle skew scattering =', "{:e}".format(sigma_SS/(2*elcond)), 'dimensionless')
print('SHC external =', "{:e}".format(sigma_SS + sigma_SJ), 'hbar/2e S/m')
print('')
print('SHC internal =', "{:e}".format(sigma_berry), 'hbar/2e S/m')
print('SHAngle internal =', "{:e}".format(sigma_berry/(2*elcond)), 'dimensionless')
print('SHC Theoretical =', "{:e}".format(sigma_theoretical), 'hbar/2e S/m')
print('')
print('SHC Experiment =', "{:e}".format(sigma_experiment), 'hbar/2e S/m')
print('Comparison SHC exp / SHC theo = ', comparison)




