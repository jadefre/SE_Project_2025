from BitPacking import * 
    
    
class BitPackingCross: 
    
    
    def compress(self,tab):
        """
        Compresser un tableau d'entiers en codant chaque entier sur un nb minimum de bit
        Les éléments peuvent êrre coder deux entiers consécutifs
        Entrée:
        - tab (List[int]) : Tableau d'entiers à compresser
        Sortie:
        - List[int] : Tableau d'entiers compressés
        """
        lnmax = max(e.bit_length() for e in tab)  # nombre de bits nécessaire pour représenter l'élément le plus grand
        lnmax_bin = bin(lnmax)[2:].zfill(6)  # comme lnmax<=32 6 bits suffisent à le representer  
        count_bin = bin(len(tab))[2:].zfill(32)  # nombre d'éléments en binaire sur 32 bits
        totalstr = lnmax_bin + count_bin  # on veut transmettre le nb de bits utilisé par entier ainsi que le nb d'entier
        for e in tab:  #chaque entiere en b inaire sur  lnmax bits
            totalstr += bin(e)[2:].zfill(lnmax)
        padding_length = (32 - len(totalstr) % 32) % 32 # taille du padding
        totalstr += "0" * padding_length  # Ajout du padding
        return [int(totalstr[i:i+32], 2) for i in range(0, len(totalstr), 32)] # convertir en entier


    def decompress(self,tab):
        """
        Décompresser un tableau d'entiers compressés en utilisant la méthode bitpacking cross autorisé
        Entrée:
        - tab (List[int]) : Tableau d'entiers compressés
        Sortie:
        - List[int] : Tableau d'entiers décompressés
        """
        tab_bin = ''.join(format(e, '032b') for e in tab)   # Reconstruir la chaîne binaire complète à partir des entiers compressés
        lnmax = int(tab_bin[:6], 2)  # Taille en bits pour chaque entier
        count = int(tab_bin[6:38], 2)  # Nombre d'éléments dans le tableau
        data_bin = tab_bin[38:]  # Les bits des éléments compressés
        return [int(data_bin[i*lnmax:(i+1)*lnmax], 2) for i in range(count)]    # Décoder chaque entier 


    def get(self,tab, i):
        """
        Accèder au iéme élément dans le tableau compressé 
        Entrée:
        - tab (List[int]) : Tableau d'entiers compressés
        - i (int) : Index de l'élément à récupérer 
        Sortie:
        - int : L'élément récupéré du tableau compressé
        """
        lnmax = int(format(tab[0], "032b")[:6], 2)     # lnmax à partir des 6 premiers bits
        indice_bin = (i - 1) * lnmax + 38  #position dans la chaine de caractere 
        indice_tab = indice_bin // 32  # entier du tableau ou est coder l'entier cible
        indice_dans_la_case = indice_bin % 32  # place dans l'entier
        dec_case = format(tab[indice_tab], "032b") #chaine de carcatere corespondant à la case
        if indice_dans_la_case + lnmax > 32:  # Si l'élément est codé sur 2 entiers ajouter le prochain entier
            dec_case += format(tab[indice_tab + 1], "032b")
        res_bin = dec_case[indice_dans_la_case:indice_dans_la_case + lnmax]#partie de la chaine de caractere qui corespond à l'entier cible
        return int(res_bin, 2) #converir le resulat en decimal
        
                 