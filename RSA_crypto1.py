#комментарий короче
from math import sqrt, gcd
import time, random

#функция возврата простого числа
def prime_num(n):
	lst=[2]
	for i in range(3, n+1, 2):
		if (i > 10) and (i%10==5):
			continue
		for j in lst:
			if j*j-1 > i:
				lst.append(i)
				break
			if (i % j == 0):
				break
		else:
			lst.append(i)
	return lst[len(lst)-1]


n = random.randint(900, 1000)
p = prime_num(n)
n = random.randint(900, 1000)
q = prime_num(n)
n = p*q
f = (p-1)*(q-1)
e = 2
while gcd(f, e) != 1:
	e+=1

k = 1
while True:
	if ((k*f)+1)%e == 0:
		d = int(((k*f)+1)/e)
		break
	else:
		k+=1



print(f'p = {p}, q = {q}, n = {n}, f = {f}, e = {e}, k = {k}, d = {d}')

secret_key = [d, n]
open_key = [e, n]

lst_test = []
lst_cypher = []
lst_usual = []
text = input('Введите что нужно зашифровать: ')
for i in range(len(text)):
	lst_usual.append(ord(text[i])-1039)

print(f'Секретный ключ: {secret_key}; Открытый ключ: {open_key}')

for i in range(len(text)):
	lst_cypher.append((lst_usual[i] ** e) % n)
	lst_test.append((lst_cypher[i] ** d) % n)

print(f'text = {text} \nlst_usual = {lst_usual} \nlst_cypher = {lst_cypher} \n lst_test = {lst_test}')