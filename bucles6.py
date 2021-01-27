import time;
i=int(input("ingrese la tasa de interes: "));
n=int(input("ingrese el capital inicial: "));
t=int(input("ingrese la cantidad de tiempo que va a dejar el capital:  "));
for x in range(t):
	c=i*n*x;
	print("el capital que usted tiene despues de",x," "+"es: ", c)
time.sleep(60);

