def compress_nocross(tab):
    """
    Compresser un tableau d'entiers chaque élément est contenu dans un entier séparé
    Arguments:
    - tab (List[int]) : Tableau d'entiers à compresser
    Sortie:
    - List[int] : Tableau d'entiers compressés sans chevauchement
    """
    lnmax = max(e.bit_length() for e in tab)  # Nombre de bits nécessaires pour chaque entier
    nbrep = 32 // lnmax  # Nombre d'entiers pouvant tenir dans un seul bloc de 32 bits
    res = [lnmax, len(tab)]  # Ajouter lnmax et le nombre d'éléments au début
    for i in range(0, len(tab), nbrep):#compresser bloc par bloc
        current_block = ''.join(bin(tab[i+j])[2:].zfill(lnmax) for j in range(nbrep) if i+j < len(tab))
        current_block = current_block.ljust(lnmax * nbrep, '0')  # padding
        res.append(int(current_block, 2))  # Ajouter le bloc compressé à la liste
    return res


def decompress_nocross(tab):
    """
    Décompresser un tableau d'entiers compressés sans croisement
    Entrée:
    - tab (List[int]) : Tableau d'entiers compressés
    Sorrtie:
    - List[int] : Tableau d'entiers décompressés
    """
    lnmax = tab[0]  # Extraire lnmax à partir du premier élément
    nbrep = 32 // lnmax  # Calculer combien d'entiers sont compressés par bloc
    lnbloc = lnmax * nbrep  # Calculer la longueur d'un bloc de compression
    res = []
    for e in tab[2:]:  # Ignorer les deux premiers éléments (lnmax et count)
        current_block = bin(e)[2:].zfill(lnbloc)  # Convertir l'entier compressé en binaire
        for i in range(nbrep):
            if len(res) < tab[1]:  # Vérifier que il ne s'agit pas du padding
                res.append(int(current_block[i * lnmax: (i + 1) * lnmax], 2))  # Extraire chaque élément
    return res


def nocross_get(tab, i):
    """
    Accèder au ieme élément  dans le tableau compressé
    Entrée:
    - tab (List[int]) : Tableau d'entiers compressés.
    - i (int) : Index de l'élément à récupérer (1-indexé)
    Sortie:
    - int : L'élément récupéré du tableau compressé
    """
    lnmax = tab[0]
    nbrep = 32 // lnmax
    indice_case = (i - 1) // nbrep + 2  # Trouver l'indice du bloc
    indice_dans_la_case = ((i - 1) % nbrep) * lnmax  # Trouver la position dans le bloc
    lnbloc = lnmax * nbrep
    res_bin = bin(tab[indice_case])[2:].zfill(lnbloc)[indice_dans_la_case:indice_dans_la_case + lnmax]    # Extraire le bloc de bits correspondant et convertir en entier
    return int(res_bin, 2)


# Exemple
original = [1,4,0,16,19,478963,45,31,4]
compressed = compress_nocross(original)
decompressed = decompress_nocross(compressed)
print("Original     :", original)
print("Compressé    :", compressed)
print("Décompressé  :", decompressed)
res=[]
for i in range(len(original)):
    res.append(nocross_get(compressed,i+1))
print("fonction get :",res)