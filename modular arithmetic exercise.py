# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:24:00 2022

@author: jingy
"""

'''
Investigate the first several (say, to 103) odd prime numbers p and divide them into
two categories: those for which x*x+1 = 0 has a solution in Zp and those for which
it does not.
'''

primes = []
for i in range(2,104):
    for j in range(2,i):
        if i % j == 0:
            break
        elif j == i-1:
            primes.append(i)

primes_w_solution = {}
primes_wo_solution = []

for p in primes:
    solutions = []
    for i in range(2,p):
        sol = ((i*i)+1) % p
        if sol == 0:
            solutions.append(i)
            if len(solutions) == 2:
                tup_solutions = (solutions[0],solutions[1])
                primes_w_solution[p] = tup_solutions
                break
        elif i==p-1:
            primes_wo_solution.append(p)
            
print(primes_w_solution)
print(primes_wo_solution)

print(f'{"PRIMES":<8}|\n--------')

for p in primes:
    print(f'{p:<8}|',end='')
    if p in primes_w_solution.keys():
        print(f'{str(primes_w_solution.get(p)):^15}')
    else:
        print(f'{"No solutions":>15}')
