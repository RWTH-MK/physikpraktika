import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.odr import ODR, Model, RealData


def odr_fit(gleichung, x_uarray, y_uarray, guess):
    """Nimmt einen scipy.odr Fit vor an Daten im uarray-Format.
    Sollte ein Problem auftreten, die uarrays als [x_uarray] und [y_uarray] übergeben

    Parameters
    ----------
    gleichung : Python-Funktion nach scipy Schema
        Diese Funktion muss gemäß scipy Doku aufgebaut sein: https://docs.scipy.org/doc/scipy/reference/odr.html
        (Basic Usage, Punkt 1). Hinweis: Kann als lambda-Funktion übergeben werden
    x_uarray : uarray
        Ggf. als [x_uarray] in den Funktionsaufruf schreiben
    y_uarray : uarray
        Ggf. als [y_uarray] in den Funktionsaufruf schreiben
    guess : [float]
        Liste der Schätz-Paramter

    Returns
    -------
    odr.fit
        ein komplexer Datentyp. Nützlich allerdings zur graphischen Darstellung: Recycle die Funktion für <gleichung>:
        plt.plot(unp.nominal_values(x_uarray), <gleichung>(fit.beta, unp.nominal_values(x_uarray)))
    """

    x_wert, x_fehler = *unp.nominal_values(x_uarray), *unp.std_devs(x_uarray)
    y_wert, y_fehler = *unp.nominal_values(y_uarray), *unp.std_devs(y_uarray)

    fit_modell = Model(gleichung)
    daten = RealData(x=x_wert, sx=x_fehler, y=y_wert, sy=y_fehler)
    collage = ODR(daten, fit_modell, beta0=guess)
    return collage.run()


def fit_to_uarray(fit_para):
    """
    Parameters
    ----------
    fit_para : odr_fit.return
        Der Rückgabewert des scipy ODR-Fit Laufs
    Returns
    -------
    uarray
        Die Fitparameter mit ihren Fehlern
    """
    schleife = len(fit_para)
    ergebnis = unp.uarray(np.zeros(schleife), np.zeros(schleife))
    for i in range(schleife):
        ergebnis[i] = ufloat(fit_para.beta[i], fit_para.sd_beta[i])
    return ergebnis
