from Implementazione.Generali.Campo import Campo


class Prenotazione():
    def __init__(self, data, oraInizio, campo, utente):
        self.data = data
        self.oraInizio = oraInizio
        self.campo = campo
        self.utente = utente