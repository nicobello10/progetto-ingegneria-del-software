from Implementazione.Generali.Utente import Utente

class GestoreUtente():
    collectionUtenti=[]

    def inserisciUtente(Utente):
        GestoreUtente.collectionUtenti.append(Utente)

    def visualizzaListaUtenti():
        print(GestoreUtente.collectionUtenti)