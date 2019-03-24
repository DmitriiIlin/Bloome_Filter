import bitarray as ba
massive=ba.bitarray([False]*10)
print(massive)

def hash_culc(str1,const):
    #рассчитывает хеш функции
    str1=str(str1)
    output_hash=None
    j=0
    while j<=len(str1)-1:
        if j==0:
            output_hash=ord(str1[j])%43
        else:
            output_hash=(output_hash*const+ord(str1[j]))%43
        j+=1
    return output_hash

z="wert767fddd"
print(hash_culc(z,3))
