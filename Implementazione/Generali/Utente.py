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
        self.tesserato=False
        
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