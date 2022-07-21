from Implementazione.Generali.Tesseramento import Tesseramento


class Utente():
    contatore=2
    def __init__(self, nome, cognome, dataNascita, cellulare, password,nomeUtente):
        self.nomeUtente = nomeUtente
        self.password = password
        self.nome=nome
        self.cognome=cognome
        self.dataNascita=dataNascita
        Utente.contatore+=1
        self.ID=Utente.contatore
        self.cellulare=cellulare
        self.tesserato=False
        self.isAdmin=False
        self.isCustode=False
        
    def tesseramento(self, email,codiceFiscale,tipoTesseramento):
        self.tesseramento=Tesseramento(email,codiceFiscale,tipoTesseramento)
        self.tesserato=True


    def getTesseramento(self):
        if self.tesserato:
            return True
        else:
            return False

    def getTipoTesseramento(self):
        return self.tesseramento.getTipoTesseramento()

    def setAdmin(self):
        self.isAdmin=True

    def setCustode(self):
        self.isCustode=True