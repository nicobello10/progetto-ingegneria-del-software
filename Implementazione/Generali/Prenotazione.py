from Implementazione.Generali.Campo import Campo


class Prenotazione():
    def __init__(self, data, oraInizio, campo, utente):
        self.data = data
        self.oraInizio = oraInizio
        self.campo = campo
        self.utente = utente
        self.collectionPartite=[]

    def aggiungiPartita(self,partita):
        self.collectionPartite.append(partita)
        print(self.collectionPartite)

    def modificaPartita(self,rigapartita,partitamodificata):
        self.collectionPartite[rigapartita]=partitamodificata

    def getStatistiche(self):
        vittorie=0
        for partita in self.collectionPartite:
            if(partita.punteggiouno>partita.punteggiodue): vittorie+=1
        if(vittorie==0):percentuale=0
        else:percentuale=vittorie/len(self.collectionPartite)*100
        #toglie i decimali inutili
        return "{:.2f}".format(percentuale)+" %"
