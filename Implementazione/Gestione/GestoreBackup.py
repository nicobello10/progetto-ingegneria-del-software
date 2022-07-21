import pickle
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti
from Implementazione.Gestione.GestorePrenotazioni import GestorePrenotazioni
from Implementazione.Generali.Utente import Utente
from Implementazione.Generali.Prenotazione import Prenotazione
from Implementazione.Generali.Campo import Campo
from Implementazione.Generali.Prenotazione import Prenotazione
from Implementazione.Generali.Tesseramento import Tesseramento
from Implementazione.Generali.Partita import Partita
class GestoreBackup():

    def salvaDati():
        #with open('backupPrenotazioni.pkl', 'wb') as outp:
            pickle.dump(GestorePrenotazioni.collectionPrenotazioni,open( "backupPrenotazioni.p", "wb" ))
        #with open('backupUtenti.pkl', 'wb') as outp:
            pickle.dump(GestoreUtenti.collectionUtenti, open( "backupUtenti.p", "wb" ))

    def caricaDati():
        #with open('backupPrenotazioni.pkl', 'rb') as inp:
            GestorePrenotazioni.collectionPrenotazioni = pickle.load(open( "backupPrenotazioni.p", "rb" ))
        #with open('backupUtenti.pkl', 'rb') as inp:
            GestoreUtenti.collectionUtenti = pickle.load(open( "backupUtenti.p", "rb" ))
