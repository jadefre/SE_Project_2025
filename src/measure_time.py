import time

def measure_time(func):
    """
    Mesure le temps d'exécution d'une fonction.
    ArgumeEntréents:
    - func (Callable) : Fonction dont le temps d'exécution doit être mesuré
    - *args : Arguments à passer à la fonction
    Sortie:
    - result : Résultat de la fonction
    - exec_time (float) : Temps d'exécution en seconde
    """
    start_time = time.perf_counter()  # Début de l'enregistrement du temps
    result = func     # Exécuter la fonction
    end_time = time.perf_counter()   # Fin de l'enregistrement du temps
    exec_time = end_time - start_time  # Calculer le temps d'exécution
    return  exec_time



def avg_time(func,n=1000):
    """
    Mesure le temps moyen d'exécution d'une fonction.
    ArgumeEntréents:
    - func (Callable) : Fonction dont le temps d'exécution doit être mesuré
    - *args : Arguments à passer à la fonction
    - n : nb de test effectués
    Sortie:
    - result : Résultat de la fonction
    - exec_time (float) : Temps d'exécution en seconde
    """
    total=0
    for i in range (n):
        total += measure_time(func)
    res = total  /n
    return res