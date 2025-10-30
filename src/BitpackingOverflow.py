from BitPacking import * 


class BitPackingOverflow:


    def compress(self, tab):
        """
        Compresser un tableau d'entiers en codant chaque entier avec le nb moyen de bits
        Les éléments plus longs sont ajputer à nla fin du tableau 
        Entrée:
        - tab (List[int]) : Tableau d'entiers à compresser
        Sortie:
        - List[int] : Tableau d'entiers compressés
        """
        ln_int = [x.bit_length() for x in tab]
        lnmean = sorted(ln_int)[len(tab)//2]  
        overflow = []
        compressed = []
        for e in tab:
            if e.bit_length() <= lnmean:
                flag = '0'
                e_compressed = bin(e)[2:].zfill(lnmean)
                compressed.append(flag + e_compressed)
            else:
                flag = '1'
                index = len(overflow)
                overflow.append(e)
                e_compressed = bin(index)[2:].zfill(lnmean)
                compressed.append(flag + e_compressed)
        totalstr = ''.join(compressed)
        while len(totalstr) % 32 != 0:
            totalstr += '0'
        blocks = [int(totalstr[i:i+32], 2) for i in range(0, len(totalstr), 32)]
        return [lnmean, len(tab), len(overflow)] + overflow + blocks


    def decompress(self, tab):
        """
        Décompresser un tableau d'entiers compressés en utilisant la méthode bitpacking overflow autorisé
        Entrée:
        - tab (List[int]) : Tableau d'entiers compressés
        Sortie:
        - List[int] : Tableau d'entiers décompressés
        """
        lnmean = tab[0]
        n = tab[1]
        overflow_count = tab[2]
        overflow = tab[3:3+overflow_count]
        blocks = tab[3+overflow_count:]
        totalstr = ''.join(bin(b)[2:].zfill(32) for b in blocks)
        element_bits = 1 + lnmean
        res = []
        for i in range(n):
            bits = totalstr[i*element_bits:(i+1)*element_bits]
            if bits[0] == '0':
                res.append(int(bits[1:], 2))
            else:
                index = int(bits[1:], 2)
                res.append(overflow[index])
        return res


    def get(self, tab, i):
        base_bits = tab[0]
        n = tab[1]
        overflow_count = tab[2]
        overflow = tab[3:3+overflow_count]
        blocks = tab[3+overflow_count:]
        joined = ''.join(bin(b)[2:].zfill(32) for b in blocks)
        element_bits = 1 + base_bits
        start = (i-1) * element_bits
        bits = joined[start:start+element_bits]
        if bits[0] == '0':
            return int(bits[1:], 2)
        else:
            index = int(bits[1:], 2)
            return overflow[index]
