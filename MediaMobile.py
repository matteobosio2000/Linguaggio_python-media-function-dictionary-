#!/usr/bin/env python3

import random

def calcola_media_mobile(lista, n):

    medie_mobili = []    
    for i in range(len(lista)):
        finestra = lista[max(0, i - n + 1):i + 1]
        media = sum(finestra) / len(finestra)
        medie_mobili.append(media)
    return medie_mobili

# Passi principali del programma
def main():
    # Chiedi quanti numeri vuole inserire
    while True:
        try:
            num_elementi = int(input("Quanti numeri vuoi inserire? "))
            if num_elementi <= 0:
                print("Per favore, inserisci un numero maggiore di 0.")
            else:
                break
        except ValueError:
            print("Inserisci un numero valido.")

    # Chiedi se i numeri devono essere inseriti manualmente
    scelta = input("Vuoi inserire i numeri manualmente? (y/n): ").lower()
    numeri = []

    if scelta == 'y':
        print(f"Inserisci {num_elementi} numeri uno alla volta:")
        for i in range(num_elementi):
            while True:
                try:
                    numero = float(input(f"Inserisci il numero {i + 1}: "))
                    numeri.append(numero)
                    break
                except ValueError:
                    print("Inserisci un numero valido.")
    else:
        # Genera numeri casuali
        numeri = [random.uniform(1, 100) for _ in range(num_elementi)]
        print(f"Numeri generati automaticamente: {numeri}")

    # Chiedi il valore di n per la media mobile
    while True:
        try:
            n = int(input("Quanti elementi vuoi considerare per la media mobile? "))
            if n <= 0:
                print("Per favore, inserisci un numero maggiore di 0.")
            else:
                break
        except ValueError:
            print("Inserisci un numero valido.")

    # Calcola e mostra i risultati
    medie_mobili = calcola_media_mobile(numeri, n)
    print(f"\nArray completo: {numeri}")
    print(f"Media mobile dinamica: {medie_mobili}")

if __name__ == "__main__":
    main()

