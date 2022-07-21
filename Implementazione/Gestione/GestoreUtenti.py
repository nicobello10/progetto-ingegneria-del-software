from Implementazione.Generali.Utente import Utente

class GestoreUtenti():
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
    contaUtenti=5
    contaSoci=0


    def inserisciUtente(Utente):
        GestoreUtenti.collectionUtenti.insert(GestoreUtenti.contaUtenti, Utente)
        GestoreUtenti.contaUtenti+=1

    def modificaUtente(utente,utentemodificato):
        for index, item in enumerate(GestoreUtenti.collectionUtenti):
            if(item == utente):
                GestoreUtenti.collectionUtenti[index]=utentemodificato
                if(GestoreUtenti.utenteConnesso.isAdmin==False): GestoreUtenti.utenteConnesso=utentemodificato
                #print (f"{item} {utentemodificato}")


    def ricercaUtente(Utente):
        for x in GestoreUtenti.collectionUtenti:
            if (x==Utente): return x

    def visualizzaListaUtenti():
        print(GestoreUtenti.collectionUtenti)

    def setLoginEffettuato():
        GestoreUtenti.loginEffettuato=True
        #GestoreUtente.utenteConnesso=utente

    def setUtenteConnesso(utente):
        GestoreUtenti.utenteConnesso=utente

    def setLogoutEffettuato():
        GestoreUtenti.loginEffettuato = False

    def getUtenteConnesso(self):
        return GestoreUtenti.utente

    def creaTesseramento(email,codiceFiscale,tipoTesseramento):
        GestoreUtenti.utenteConnesso.tesseramento(email, codiceFiscale, tipoTesseramento)
        GestoreUtenti.contaSoci+=1

    def getCollectionUtenti():
        return GestoreUtenti.collectionUtenti