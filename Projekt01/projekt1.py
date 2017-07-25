import numpy as np
import matplotlib.pyplot as plt

print("Hallo, im first PhysioCode")

Param = {"k_e":0.0888,"k_a1":7.6226,"frac":0.5147,"X0":1.0,"V_val":1.0,"T_lag":10,"k_a2":1.0588}


#k_e=0.0888
#k_a1=7.6226
#frac = 0.5147
#X0 = 1.0
#V_val = 1.0
#T_lag = 2.2862
#T_lag = 10
#k_a2 = 1.0588

time_exp=np.arange(24, dtype=float)

for i in time_exp:

    if time_exp[i] < Param['T_lag']:
        const_exp1 = (Param['k_a1'] * Param['frac'] * Param['X0'] )/(Param['V_val'] * (Param['k_a1'] - Param['k_e']))
        con_exp1 = const_exp1 * (np.exp(-Param['k_e']*time_exp) - np.exp(-Param['k_a1']*time_exp))
        print(i,time_exp[i], Param['T_lag'])

    else:
        const_exp2 = (Param['k_a2'] * (1-Param['frac']) * Param['X0'])/(Param['V_val'] * (Param['k_a2'] - Param['k_e']))
        con_exp2 = con_exp1 + const_exp2 * (np.exp(-Param['k_e']*(time_exp - Param['T_lag'])) - np.exp(-Param['k_a2']*(time_exp - Param['T_lag'])))
        print('xxx ',i,time_exp[i], Param['T_lag'])

plt.plot(time_exp, con_exp1)
plt.plot(time_exp, con_exp2)

print(con_exp1)
print(con_exp2)

### Dzień dobry!
### zaimplementowałem słownika, wszystko oblicza się, ale wykresy nie wyświetlają się((((((
