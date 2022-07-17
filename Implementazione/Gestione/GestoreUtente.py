from Implementazione.Generali.Utente import Utente

class GestoreUtente():
    collectionUtenti=[]
    loginEffettuato=False


    def inserisciUtente(Utente):
        GestoreUtente.collectionUtenti.append(Utente)
        print(len(GestoreUtente.collectionUtenti))

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

    def setLoginEffettuato():
        GestoreUtente.loginEffettuato=True
        #GestoreUtente.utenteConnesso=utente

    def setUtenteConnesso(utente):
        GestoreUtente.utenteConnesso=utente

    def setLogoutEffettuato():
        GestoreUtente.loginEffettuato = False

    def getUtenteConnesso(self):
        return GestoreUtente.utente

    def creaTesseramento(email,codiceFiscale,tipoTesseramento):
        GestoreUtente.utenteConnesso.tesseramento(email,codiceFiscale,tipoTesseramento)
        print(GestoreUtente.utenteConnesso.getTipoTesseramento())

    def getCollectionUtenti():
        return GestoreUtente.collectionUtenti