# calculo del desbalance final 
# el cofre de plata se incrementa de acuerdo al numero de dia (dia 1=1, dia 2=2, etc)
# el cofre de oro se incrementa de acuerdo al numero de dia  par (dia 2=2, dia 4=4, etc) los dias impares no hay ningun incremento

def calcular_desbalance_final(k):
    # se calcula el total del cofre de plata
    cofre_plata = k * (k + 1) // 2  

    # se calcula el numero de dias pares
    dias_pares = k //2

    # se calcula el total del cofre de oro (dias pares)
    cofre_oro = dias_pares * (dias_pares + 1)

    # se hace el calculo del desbalance final con la diferencia absoluta
    desbalance_final = abs(cofre_plata - cofre_oro)

    return desbalance_final


# para el programa principal

if __name__ == "__main__":
    # se solicita y lee el valor de "k" al usuario por consola
    k = int(input())

    # se realiza el calculo del desbalance final y se muestra el resultado
    resultado = calcular_desbalance_final(k)
    print(resultado)
