class BitPackingOverflow:

    def compress(self, tab):
        bit_lengths = [x.bit_length() for x in tab]
        median_bits = sorted(bit_lengths)[len(tab)//2]  
        
        base_bits = median_bits
        overflow = []
        compressed = []
        
        for x in tab:
            if x.bit_length() <= base_bits:
                flag = '0'
                bits = bin(x)[2:].zfill(base_bits)
                compressed.append(flag + bits)
            else:
                flag = '1'
                index = len(overflow)
                overflow.append(x)
                bits = bin(index)[2:].zfill(base_bits)
                compressed.append(flag + bits)
        
        joined = ''.join(compressed)
        while len(joined) % 32 != 0:
            joined += '0'
        blocks = [int(joined[i:i+32], 2) for i in range(0, len(joined), 32)]
        
        return [base_bits, len(tab), len(overflow)] + overflow + blocks


    def decompress(self, tab):
        base_bits = tab[0]
        n = tab[1]
        overflow_count = tab[2]
        overflow = tab[3:3+overflow_count]
        blocks = tab[3+overflow_count:]
        
        joined = ''.join(bin(b)[2:].zfill(32) for b in blocks)
        element_bits = 1 + base_bits
        res = []
        
        for i in range(n):
            bits = joined[i*element_bits:(i+1)*element_bits]
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
