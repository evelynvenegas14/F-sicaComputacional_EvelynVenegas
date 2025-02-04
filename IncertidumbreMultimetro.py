import numpy as np




print("¿Qué estás midiendo?")
type= input("1 para Voltaje ; 2 para Corriente ; 3 para Resistencia")

if type == 1:
    inc200mV= 200*0.00004
    inc2V= 2*0.00003
    inc20V= 20*0.00004
    inc200V=200*0.00003

    print("¿En qué rango estás midiendo?")
    rango= input("1 para 200 mV ; 2 para 2V ; 3 para 20V ; 4 para 200V")

    if rango == 1:
        medicion= input("Ingresa la medida del multímetro")
        incertidumbre = (medicion*0.00015)+ inc200mV

        print("La incertidumbre es: {incertidumbre}")

    if rango == 2:
        medicion= input("Ingresa la medida del multímetro")
        incertidumbre = (medicion*0.00015)+ inc2V

        print("La incertidumbre es: {incertidumbre}")
    
    if rango == 3:
        medicion= input("Ingresa la medida del multímetro")
        incertidumbre = (medicion*0.00015)+ inc20V

        print("La incertidumbre es: {incertidumbre}")

    if rango == 4:
        medicion= input("Ingresa la medida del multímetro")
        incertidumbre = (medicion*0.00015)+ inc200V

        print("La incertidumbre es: {incertidumbre}")

if type == 2:
    inc2mA = 2*0.00005
    inc20mA= 20*0.00005
    inc200mA= 200*0.00005

else 

 