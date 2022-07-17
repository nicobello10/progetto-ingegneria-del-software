from Implementazione.Generali.Tesseramento import Tesseramento


class Utente():
    ID=0
    def __init__(self, nome, cognome, dataNascita, cellulare, password,nomeUtente):
        self.nomeUtente = nomeUtente
        self.password = password
        self.nome=nome
        self.cognome=cognome
        self.dataNascita=dataNascita
        self.ID+=1
        self.cellulare=cellulare
        
    def tesseramento(self, email,codiceFiscale,tipoTesseramento):
        self.tesseramento=Tesseramento(email,codiceFiscale,tipoTesseramento)


    def getTesseramento(self):
        if(self.tesseramento is None):
            return False
        else:
            return True

    def getTipoTesseramento(self):
        return self.tesseramento.getTipoTesseramento()