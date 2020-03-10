#1
nombre=input("Dime tu nombre:")
print(nombre)
#para concatenar 2 cadenas se utiliza el +
print("buenos dias" +nombre)


#2
base=int (input("Introduce la base:"))
altura=int (input("Introduce la altura:"))

perimetro=(2*base)+(2*altura)
area=base*altura
print("El area del rectangulo es:",area)
print("El perimetro del rectangulo es",perimetro)

#3

pi=3.1416
radio=int(input("Introduce el radio:"))
perimetro=2*pi*radio
area=pi*radio*radio
print("El area del circulo es:",area)
print("El area del circulo es:",circulo)

#4
#5

#6
datos1_5=int (input("Introduce un numero,porfavor:"))
texto=str(datos1_5)
numero=texto[1]
print(numero)

#2opcion
numero=int(input("Introduce un numero:"))
resto=numero%10
print ("La ultima cifra es:",resto)