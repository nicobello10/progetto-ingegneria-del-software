from Implementazione.Generali.Utente import Utente

class GestoreUtente():
    admin=Utente("Amministratore"," "," "," ","admin","admin")
    admin.isAdmin=True
    custode = Utente("Custode", " ", " ", " ", "custode", "custode")
    custode.isCustode = True
    utente1 = Utente("Ivan", "Pacenti", " ", " ", "asd", "asd")
    utente2 = Utente("Nicola", "Picciafuoco", " ", " ", "asd2", "asd2")
    utente3 = Utente("Giada", "Remedia", " ", " ", "asd3", "asd3")
    collectionUtenti=[]
    collectionUtenti.append(utente1)
    collectionUtenti.append(utente2)
    collectionUtenti.append(utente3)
    collectionUtenti.append(admin)
    collectionUtenti.append(custode)
    loginEffettuato=False
    contaUtenti=0
    contaSoci=0


    def inserisciUtente(Utente):
        GestoreUtente.collectionUtenti.insert(GestoreUtente.contaUtenti,Utente)
        GestoreUtente.contaUtenti+=1
        print(len(GestoreUtente.collectionUtenti))

    def modificaUtente(utente,utentemodificato):
        for index, item in enumerate(GestoreUtente.collectionUtenti):
            if(item == utente):
                GestoreUtente.collectionUtenti[index]=utentemodificato
                #print (f"{item} {utentemodificato}")


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
        GestoreUtente.contaSoci+=1

    def getCollectionUtenti():
        return GestoreUtente.collectionUtenti