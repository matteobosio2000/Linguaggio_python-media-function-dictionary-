#!/usr/bin/env python3

import re

def conta_occorrenze(test):
    # Converti il testo in minuscolo
    testo_lower = test.lower()
    
    # Rimuovi la punteggiatura usando una regular expression
    testo_senza_punteggiatura = re.sub(r'[^\w\s]', '', testo_lower)
    
    # Splitta il testo in parole (usando gli spazi come delimitatori)
    parole = testo_senza_punteggiatura.split()
    
    # Crea un dizionario per contare le occorrenze delle parole
    dizionario_occorrenze = {}
    
    for parola in parole:
        # Incrementa il conteggio della parola nel dizionario
        if parola in dizionario_occorrenze:
            dizionario_occorrenze[parola] += 1
        else:
            dizionario_occorrenze[parola] = 1
    
    return dizionario_occorrenze

# Chiedi il testo all'utente
testo_utente = input("Inserisci il testo da analizzare: ")

# Calcola e stampa il risultato
risultato = conta_occorrenze(testo_utente)
print("Conteggio delle occorrenze delle parole:")
for parola, conteggio in risultato.items():
    print(f"{parola}: {conteggio}")

