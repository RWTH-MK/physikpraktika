import numpy as np
from uncertainties import unumpy as unp


def _multimeter_fehler(daten, messbereich, einheitenpotenz, grundgenauigkeit, dgts, counts):
    """ Eine allgemeine Funktion für Multimeterfehler. Gibt die Daten samt Fehler in Basiseinheit zurück

    Parameters
    ----------
    daten : array_like
        Der Datensatz, der vermessen wurde
    messbereich : int
        Der Messbereich der Daten ohne Faktor (200mA Messbereich -> 200)
    einheitenpotenz : float
        Der Vorfaktor der Messgröße, z. B. milli -> 1e-3
    grundgenauigkeit : float
        Prozentuale Abweichung lt. Hersteller
    dgts : integer
        Anzahl der Digits lt. Hersteller
    counts : integer
        Counts lt. Hersteller

    Returns
    -------
    uarray
        Die Messwerte mit Fehler in Basiseinheit, z. B. wird aus Milliampere -> Ampere
    """
    schleife = len(daten)
    fehler_liste = np.empty(schleife)
    fehlerD = messbereich / counts * dgts
    for i in range(schleife):
        fehlerG = daten[i] * grundgenauigkeit / 100
        fehler_liste[i] = (fehlerD + fehlerG) * einheitenpotenz
    daten_konvert = np.array(daten)*einheitenpotenz
    return unp.uarray(daten_konvert, fehler_liste)


def voltcraft220_2Vgleich(daten):
    """Gibt einen uarray zurück mit den Messwerten und den Fehlern des Voltcraft 220 für den Messbereich 2V Gleichstrom.
    Herstellerangaben entnommen aus (06.05.24):
    https://www.manualslib.de/manual/349243/Voltcraft-Vc-220.html?page=14#manual

    Parameters
    ----------
    daten : array_like
        Liste oder Array der Messwerte

    Returns
    -------
    uarray
    """
    return _multimeter_fehler(daten, 2, 1, 0.6, 5, 2000)
def voltcraft220_20Vgleich(daten):
    return _multimeter_fehler(daten, 20, 1, 0.6, 5, 2000)
def voltcraft220_20mA(daten):
    return _multimeter_fehler(daten, 20, 1e-3, 1, 2, 2000)
