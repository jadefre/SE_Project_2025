import time

def measure_time(func, *args):
    """
    Mesure le temps d'exécution d'une fonction.
    ArgumeEntréents:
    - func (Callable) : Fonction dont le temps d'exécution doit être mesuré
    - *args : Arguments à passer à la fonction
    Sortie:
    - result : Résultat de la fonction
    - exec_time (float) : Temps d'exécution en seconde
    """
    start_time = time.time()  # Début de l'enregistrement du temps
    result = func(*args)     # Exécuter la fonction
    end_time = time.time()   # Fin de l'enregistrement du temps
    exec_time = end_time - start_time  # Calculer le temps d'exécution
    return result, exec_time
