    try:
    mes=int(input("Introduce en mes (1-12):"))
     if mes==2:
    print("El mes tiene 28 dias")
    elif mes in(1,3,5,7,8,10,12):
    print("el mes tiene 31 dias")
    elif mes in (2,4,6,9,11):
    print ("el mes tiene 31 dias")
    else:
    print("Numero erroneo")

    except:
    print("Numero no correcto, intentalo de nuevo")
