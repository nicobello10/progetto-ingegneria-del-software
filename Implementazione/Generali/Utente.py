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
        
    