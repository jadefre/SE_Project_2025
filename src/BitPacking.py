from BitPackingCross import * 
from BitPackingNoCross import * 
from BitpackingOverflow import * 

class BitPacking:
    def __init__(self, mode, tab):
        self.mode = mode
        self.tab = tab
        self.compressor = self._create_compressor()

    def _create_compressor(self):
        if self.mode == "cross":
            return BitPackingCross()
        elif self.mode=='nocross':
            return BitPackingNoCross()
        else:
            return BitPackingOverflow()

    def compress(self):
        return self.compressor.compress(self.tab)

    def decompress(self):
        return self.compressor.decompress(self.tab)

    def get(self, i):
        return self.compressor.get(self.tab, i)
    
    
    
    
         