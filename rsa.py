def findInverse(b, en):
	i = 1
	while True:
		if (b * i ) % en == 1:
			return i
		i += 1

def encrypt(plain, exp, mod):
	cipher = []
	for i in range(0, len(plain)):
		m = ord(plain[i])
		cipher += [itrExp(m, exp, mod)]
	return cipher

def decrypt(cipher, exp, mod):
	message = ""
	for i in range(0, len(cipher)):
		m = cipher[i]
		message += chr(recExp(m, exp, mod))
	return message

def itrExp(base, exp, mod):
	if exp == 0:
		return 1 % mod
	else:
		power = 1
		result = 1
		temp = base % mod

		while power < exp:
			if power * 2 < exp:
				temp = (temp * temp) % mod
				power *= 2
			else:
				result = (result * temp) % mod
				exp -= power
				power = 1
				temp = base % mod
		return (temp * result) % mod


def recExpX(base, exp, mod, power, temp, result):
	if power == exp:
		return (temp * result) % mod
	elif power * 2 <= exp:
		return recExpX(base, exp, mod, power * 2, (temp * temp) % mod, result)
	else:
		return recExpX(base, exp - power, mod, 1, base % mod, (result * temp) % mod)

def recExp(base, exp, mod):
	if exp == 0:
		return 1 % mod
	else:
		return recExpX(base, exp, mod, 1, base % mod, 1)

p = 6337
q = 7841
n = p * q
en = (p - 1) * (q - 1)

b = 977

#a is b inverse a=1/b mod en
#a=findInverse(b,en)
a = 26692913

plain="Bond, James Bond, Top Secret, From Russia With Love xx"

cipher = encrypt(plain,b,n)
secret = decrypt(cipher,a,n) 
print(secret)



