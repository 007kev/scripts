# Author: Kevin Arias 2/5/2026

import numpy as np

tau_n = 887.8 # [s]
taus = np.append(tau_n, np.logspace(2, -9, 12)) # exponents are 2 all the way to -9

beta = 0.7
gamma = 1/(np.sqrt(1-beta**2)) # ~1.40028
print(f'gamma = {gamma}')

lambda_0 = 1/taus
lambda_l = lambda_0/gamma # 13 values
print(f'lambda lab for 887.6s lifetime = {lambda_l[0]}')

l = 6 # [m]
t = l/(beta * 3e08) 

P_survive = np.exp(-lambda_l*t)
P_decay = 1 - P_survive
print(f'Probability of neutron decay for 887.6s lifetime = {P_decay[0]}')

N_n = 1/P_decay
for i, tau in enumerate(taus):
    print(f'Number of neutrons needed if tau_rest is {tau:9.3e} s: {N_n[i]:9.3e}')