from datetime import date


class Tesseramento():
    def __init__(self, email,codiceFiscale,tipoTesseramento):
        self.email=email
        self.codiceFiscale=codiceFiscale
        self.tipoTesseramento=tipoTesseramento
        self.dataTesseramento=date.today()


    def getTipoTesseramento(self):
        return self.tipoTesseramento