import bitarray as ba

class BloomFilter:

    def __init__(self, f_len=32):
        # создаём битовый массив длиной f_len ...
        self.filter_len = f_len
        self.massive=ba.bitarray([False]*self.filter_len)
    
    def hash_culc(self,str1,const):
        #рассчитывает хеш функции
        str1=str(str1)
        if len(str1)!=0:
            output_hash=None
            j=0
            while j<=len(str1)-1:
                if j==0:
                    output_hash=ord(str1[j])%self.filter_len
                else:
                    output_hash=(output_hash*const+ord(str1[j]))%self.filter_len
                j+=1
            return output_hash
        else:
            return None

    def hash1(self, str1):
        # 17
        return self.hash_culc(str1,17)

    def hash2(self, str1):
        # 223 
        return self.hash_culc(str1,223)

    def add(self, str1):
        # добавляем строку str1 в фильтр
        hash1=self.hash1(str1)
        hash2=self.hash2(str1)
        self.massive[hash1]=True
        self.massive[hash2]=True



    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        str1=str(str1)
        if len(str1)!=0:
            index1=self.hash1(str1)
            index2=self.hash2(str1)
            if self.massive[index1]==True and self.massive[index2]==True:
                return True 
            else:
                return False
        else:
            return None

"""a=BloomFilter()
print(a.massive)
a.add("ertyQWEEDFf")
print(a.massive)
print(a.is_value("ertyQWEDFf"))"""