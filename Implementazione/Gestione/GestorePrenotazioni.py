from Implementazione.Generali.Campo import Campo
import datetime

from Implementazione.Generali.Prenotazione import Prenotazione
from Implementazione.Generali.Utente import Utente
from Implementazione.Gestione.GestoreUtenti import GestoreUtenti


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
    utente = Utente("Ivan", " ", " ", " ", " ", " ")
    prova = Prenotazione("2022, 7, 20", "16:00", paddle, utente)
    collectionPrenotazioni = []
    collectionPrenotazioni.append(prova)

    def inserisciPrenotazione(data, riga, colonna,idUtente):
        if (riga == 0): orario = "08:00"
        if (riga == 1): orario = "09:00"
        if (riga == 2): orario = "10:00"
        if (riga == 3): orario = "11:00"
        if (riga == 4): orario = "12:00"
        if (riga == 5): orario = "13:00"
        if (riga == 6): orario = "14:00"
        if (riga == 7): orario = "15:00"
        if (riga == 8): orario = "16:00"
        if (riga == 9): orario = "17:00"
        if (riga == 10): orario = "18:00"
        if (riga == 11): orario = "19:00"
        if (riga == 12): orario = "20:00"
        if (riga == 13): orario = "21:00"
        if (riga == 14): orario = "22:00"
        if (colonna == 0): campo = GestorePrenotazioni.terraRossa_1
        if (colonna == 1): campo = GestorePrenotazioni.terraRossa_2
        if (colonna == 2): campo = GestorePrenotazioni.erbaSintetica
        if (colonna == 3): campo = GestorePrenotazioni.paddle
        if(GestoreUtenti.utenteConnesso.isAdmin==False): prenotazione = Prenotazione(data, orario, campo, GestoreUtenti.utenteConnesso)
        else: prenotazione = Prenotazione(data, orario, campo, GestoreUtenti.collectionUtenti[idUtente])
        GestorePrenotazioni.collectionPrenotazioni.append(prenotazione)



    def eliminaPrenotazione(data, riga, colonna):
        prenotazione = GestorePrenotazioni.cercaPrenotazione(data, riga, colonna)
        if(prenotazione!=None):
            GestorePrenotazioni.collectionPrenotazioni.remove(prenotazione)
            return True
        else: return False

    def cercaPrenotazione(data, riga, colonna):
        if (riga == 0): orario = "08:00"
        if (riga == 1): orario = "09:00"
        if (riga == 2): orario = "10:00"
        if (riga == 3): orario = "11:00"
        if (riga == 4): orario = "12:00"
        if (riga == 5): orario = "13:00"
        if (riga == 6): orario = "14:00"
        if (riga == 7): orario = "15:00"
        if (riga == 8): orario = "16:00"
        if (riga == 9): orario = "17:00"
        if (riga == 10): orario = "18:00"
        if (riga == 11): orario = "19:00"
        if (riga == 12): orario = "20:00"
        if (riga == 13): orario = "21:00"
        if (riga == 14): orario = "22:00"
        if (colonna == 0): campo = GestorePrenotazioni.terraRossa_1
        if (colonna == 1): campo = GestorePrenotazioni.terraRossa_2
        if (colonna == 2): campo = GestorePrenotazioni.erbaSintetica
        if (colonna == 3): campo = GestorePrenotazioni.paddle
        for x in GestorePrenotazioni.collectionPrenotazioni:
            if(x.data==data and x.oraInizio==orario and x.campo==campo
                    and (x.utente==GestoreUtenti.utenteConnesso or GestoreUtenti.utenteConnesso.isAdmin==True)):
                return x
            else:pass