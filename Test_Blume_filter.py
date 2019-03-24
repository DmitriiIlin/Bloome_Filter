import Blume_filter_mod, unittest,string,random,bitarray as ba

def massive_generator(massive_len=32):
    massive=ba.bitarray([False]*massive_len)
    return massive

def string_generator(size=10):
    chars=string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def data_massive(size=10):
    data=[]
    for i in range(size):
        data.append(str(string_generator())) 
    return(data)

def hash_culc(str1,const,filter_len):
    #рассчитывает хеш функции
    str1=str(str1)
    if len(str1)!=0:
        output_hash=None
        j=0
        while j<=len(str1)-1:
            if j==0:
                output_hash=ord(str1[j])%filter_len
            else:
                output_hash=(output_hash*const+ord(str1[j]))%filter_len
            j+=1
        return output_hash
    else:
        return None

class Blume_filter_Tests(unittest.TestCase):
    #Тесты для BloomFilter

    def test_add(self):
        #Тесты для метода add
        bloome_massive=Blume_filter_mod.BloomFilter()
        massive=massive_generator()
        data=data_massive()
        for i in range(0,len(data)):
            hash1=hash_culc(data[i],17,massive.length())
            hash2=hash_culc(data[i],223,massive.length())
            massive[hash1]=1
            massive[hash2]=1
        for i in range(0,len(data)):
            bloome_massive.add(data[i])
        for i in range(len(massive)):
            self.assertEqual(massive[i],bloome_massive.massive[i])
            print(massive[i],bloome_massive.massive[i])

    def test_is_value(self):
        #Тест для проверки наличия строки
        bloome_massive=Blume_filter_mod.BloomFilter()
        massive=massive_generator()
        data=data_massive()
        for i in range(0,len(data)):
            hash1=hash_culc(data[i],17,massive.length())
            hash2=hash_culc(data[i],223,massive.length())
            bloome_massive.add(data[i])
            self.assertEqual(bloome_massive.massive[hash1],bloome_massive.massive[hash2],bloome_massive.is_value(data[i]))


    


if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()

