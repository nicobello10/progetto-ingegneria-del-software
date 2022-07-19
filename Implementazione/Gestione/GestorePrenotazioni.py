from Implementazione.Generali.Campo import Campo
import datetime

from Implementazione.Generali.Prenotazione import Prenotazione
from Implementazione.Generali.Utente import Utente


class GestorePrenotazioni():
    giorno = datetime.date.today().timetuple().tm_yday
    noncoperto = range(80, 264)
    if giorno in noncoperto:
        copertura = False
    else:
        copertura = True
    # campo con copertura fissa tutto l'anno
    terraRossa_1 = Campo(True, "Terra Rossa Coperto", "Tennis")
    # campi con copertura variabile a seconda della stagione
    terraRossa_2 = Campo(copertura, "Terra Rossa", "Tennis")
    erbaSintetica = Campo(copertura, "Erba sintetica", "Tennis")
    # campo all'aperto
    paddle = Campo(False, "Paddle", "Paddle")
    utente=Utente("ivan"," "," "," "," "," ")
    prova = Prenotazione("PyQt5.QtCore.QDate(2022, 7, 20)", "16:00",paddle,utente)
    collectionPrenotazioni=[]
    collectionPrenotazioni.append(prova)

    def inserisciPrenotazione():
        print("sto ins")

    def modificaPrenotazione(self):pass

    def eliminaPrenotazione(self):pass



