def findInverse(b,en):
	i=1
	while True:
		if (b*i)%en==1:
			return i
		i+=1

def encrypt(plain,exp,mod):
	cipher=[None]*len(plain)
	for i in range(0,len(plain)):
		m=ord(plain[i])
		cipher[i]=recExp(m,exp,mod)
	return cipher

def decrypt(cipher,exp,mod):
	message=""
	for i in range(0,len(cipher)):
		m=cipher[i]
		message+=chr(recExp(m,exp,mod))
	return message

def itrExp(base,exp,mod):
	x=1
	for i in range(0,exp):
		x=(x*base)%mod
	return x

def recExp(base,exp,mod):
	if exp==1:
		return base%mod
	if exp==2:
		return (base*base)%mod
	if exp%2==0:
		x=recExp(base,exp/2,mod)
		x=(x*x)%mod
		return x
	else:
		x=(recExp(base,(exp+1)/2,mod)*recExp(base,((exp+1)/2)-1,mod))%mod
		return x

p=6337
q=7841
n=p*q
en=(p-1)*(q-1)

b=977

#a is b inverse a=1/b mod en
#a=findInverse(b,en)
a=26692913

plain="Bond, James Bond, Top Secret, From Russia With Love xx"

cipher=encrypt(plain,b,n)
secret=decrypt(cipher,a,n) 
print(secret)



