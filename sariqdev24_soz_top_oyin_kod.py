from uzwords import words
import sariqdev24_soz_top_oyin as funksiya
print("SO'Z TOPISH O'YINI\n")
sikl1 = True
while sikl1:
    soz = funksiya.soz_tanla(words)
    harflar = funksiya.harflarga_ajrat(soz)
    uzunlik = len(harflar)
    yangi_list = funksiya.yangi_list(harflar)
    foydalanilgan=[]
    print(f"\nMen {uzunlik} harifli so'z o'yladim topishga harakat qiling")
    #print(harflar)

    yangi_list[0] = harflar[0]
    yangi_list[-1] = harflar[-1]


    def displey(list):
        sikl1_1 = 0
        while sikl1_1 < (len(list)):
            sikl1_1 += 1
            print(list[sikl1_1-1], end=' ')
            
    displey(harflar)
    print("\n")
    displey(yangi_list)

    n = 0
    sikl1_2 = True
    sikl1_3 = 0
    while sikl1_2:
        harf = input(f"\nHarf kiriting>>")
        n += 1

        harf = harf.lower()
        foydalanilgan.append(harf)
        if harf in harflar:
            index_harf = 0
            for h in harflar:
                if harf == h:
                    yangi_list[index_harf] = harf
                    sikl1_3 += 1

                index_harf += 1
        else:
            print(f"Siz kiritgan {harf} so'zda qatnashmagan")

        print("Foydalanilgan harflar:", end=" ")
        displey(foydalanilgan)
        print("\n")
        displey(yangi_list)


        
        if uzunlik == sikl1_3 + 2  :

            print(f"\nsiz {n} urinishda sozni topdingiz")
            sikl1_2 = False

    

    
    
    
    
    sikl1=False        

    
        
