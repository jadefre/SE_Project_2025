from BitPacking import * 
from measure_time import *  



if __name__ == "__main__":
    tab = [12, 85, 9652, 32, 46712596,1,1,1,1,1,1,11,1,1,11,1,1,1,1,1,11,1,1,1213131]
    
    
    print("-------------cross--------------")
    b = BitPacking("cross", tab)
    print(f"Mode: {b.mode}")
    print(f"Original: {b.tab}")
    compressed = b.compress()
    avg_compress_time=avg_time(b.compress())
    print(f"Compressé: {compressed}")
    print(f"Temps compression: {avg_compress_time}s")
    b_compressed = BitPacking("cross", compressed) 
    decompressed = b_compressed.decompress()
    avg_decompress_time=avg_time(b_compressed.decompress())
    print(f"Temps decompression: {avg_decompress_time} s")
    print(f"Decompressé: {decompressed}")
    print(f"Element 3: {b_compressed.get(3)}")
    
    
    print("-------------nocross--------------")
    b = BitPacking("nocross", tab)
    print(f"Mode: {b.mode}")
    print(f"Original: {b.tab}")
    compressed = b.compress()
    print(f"Compressé: {compressed}")
    avg_compress_time=avg_time(b.compress())
    print(f"Temps compression: {avg_compress_time} s")
    b_compressed = BitPacking("nocross", compressed) 
    decompressed = b_compressed.decompress() 
    print(f"Decompressé: {decompressed}")
    avg_decompress_time=avg_time(b_compressed.decompress())
    print(f"Temps decompression: {avg_decompress_time} s")
    print(f"Element 3: {b_compressed.get(3)}")
    
    print("-------------overflow--------------")
    b = BitPacking("overflow", tab)
    print(f"Mode: {b.mode}")
    print(f"Original: {b.tab}")
    compressed = b.compress()
    print(f"Compressé: {compressed}")
    avg_compress_time=avg_time(b.compress())
    print(f"Temps compression: {avg_compress_time} s")
    b_compressed = BitPacking("overflow", compressed) 
    decompressed = b_compressed.decompress() 
    print(f"Decompressé: {decompressed}")
    avg_decompress_time=avg_time(b_compressed.decompress())
    print(f"Temps decompression: {avg_decompress_time} s")
    print(f"Element 3: {b_compressed.get(3)}")
    
    