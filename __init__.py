from .fehler_uarrays import *
from .mittelwerte import *
from .multimeter import *
from .odr_fit import *
from .peak import *

e = 1.602176634e-19  # C
c = 299792458  # m/s
h = 6.62607015e-34  # Js


class PlotParameter:
    """Sammelt typische Angaben, um Plots zu beschriften und anzufertigen

    Parameters
    ----------
    titel : string
        Optional
    x_achse : (raw) string
        raw strings können LaTeX codiert sein, z.B. x_achse=r'Wellenlänge ~$\lambda [nm]$'
    y_achse : (raw) string
    datei : string
        Im Dateinamen können -pfad und -format enthalten sein, z.B. datei='Plots/odr_plot.svg' (svg ist eine
        Vektorgrafik. Diese können endlos skaliert werden, ohne unscharf zu werden).
    x_faktor : int, float
        Optional. Falls die Werte skaliert werden sollen, z.B. x_faktor=1e9, um eine nano-Größe aufzutragen
    y_faktor : int, float
    """
    def __init__(self, titel, x_achse, y_achse, datei, x_faktor=1, y_faktor=1):
        self.titel = titel
        self.x_achse = x_achse
        self.y_achse = y_achse
        self.x_faktor = x_faktor
        self.y_faktor = y_faktor
        self.datei = datei
