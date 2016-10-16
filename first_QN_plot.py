'''
Quick plot of the noise spectral density of a convensional grav wave interferometer

'''
import matplotlib.pyplot as plt
import numpy as np

omega = np.linspace(0.1, 10, 100)
omega_2 = omega*omega

S = (1.0/(omega_2*(1+omega_2)) + omega_2*(1+omega_2))

sq_S_over_h = np.sqrt(S)

plt.plot(omega,sq_S_over_h)

plt.xlabel('$omega/gamma$')
plt.ylabel('$sqrt(S_{h})/h_{SQL}$')

#plt.xlabel('$\frac{\Omega}{\gamma}$')
#plt.ylabel('$\frac{\sqrt{S_{h}}}{h_{SQL}}$')


plt.xscale('log')

plt.yscale('log')
#plt.ylim([0.05,10])
plt.show()