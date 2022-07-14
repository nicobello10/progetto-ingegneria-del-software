class Prova():
    def __init__(self,nome,cognome):
        self.nome=nome
        self.cognome=cognome

    def stampa(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"


ogg=Prova("ivan","pacenti")
print(ogg.stampa())