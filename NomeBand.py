#!/usr/bin/env python3

def genera_nome_band():
    print("Benvenuto nel generatore di nomi per band!")
    
    # Chiedi all'utente la città di origine
    citta = input("Inserisci la città di origine: ").strip()
    
    # Chiedi all'utente il nome del proprio animale domestico
    animale = input("Inserisci il nome del tuo animale domestico: ").strip()
    
    # Genera il nome della band combinando i due input
    nome_band = f"{citta} {animale}"
    
    # Mostra il nome della band
    print(f"Il nome della tua band potrebbe essere: {nome_band}")


# Esegui la funzione
genera_nome_band()
