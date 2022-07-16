from Implementazione.Generali.Utente import Utente

class GestoreUtente():
    collectionUtenti=[]
    loginEffettuato=False
    IDUtenteLoggato=0


    def inserisciUtente(Utente):
        GestoreUtente.collectionUtenti.append(Utente)

    def modificaUtente(utente,utentemodificato):
        for index, item in enumerate(GestoreUtente.collectionUtenti):
            if(item == utente):
                GestoreUtente.collectionUtenti[index]=utentemodificato
                print (f"{item} {utentemodificato}")


    def ricercaUtente(Utente):
        for x in GestoreUtente.collectionUtenti:
            if (x==Utente): return x

    def visualizzaListaUtenti():
        print(GestoreUtente.collectionUtenti)

    def setLoginEffettuato(ID):
        GestoreUtente.loginEffettuato=True
        GestoreUtente.IDUtenteLoggato=ID

    def setUtenteConnesso(utente):
        GestoreUtente.utenteConnesso=utente

    def getUtenteConnesso(self):
        return GestoreUtente.utente
