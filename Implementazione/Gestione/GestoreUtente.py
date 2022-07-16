from Implementazione.Generali.Utente import Utente

class GestoreUtente():
    collectionUtenti=[]
    loginEffettuato=False


    def inserisciUtente(Utente):
        GestoreUtente.collectionUtenti.append(Utente)

    def visualizzaListaUtenti():
        print(GestoreUtente.collectionUtenti)

    def setLoginEffettuato():
        GestoreUtente.loginEffettuato=True

    def setUtenteConnesso(utente):
        GestoreUtente.utenteConnesso=utente
