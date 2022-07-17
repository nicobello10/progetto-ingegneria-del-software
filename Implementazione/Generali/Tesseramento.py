class Tesseramento():
    def __init__(self, email,codiceFiscale,tipoTesseramento):
        self.email=email
        self.codiceFiscale=codiceFiscale
        self.tipoTesseramento=tipoTesseramento


    def getTipoTesseramento(self):
        return self.tipoTesseramento