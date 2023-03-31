


def soz_tanla(sozlar):
    
    #List ichidagi tasadifiy elementni qiymatini qaytaruvchi funksiya
    from random import choice
    soz = choice(sozlar)
    return soz

def harflarga_ajrat(ixtiyoriy_soz):

    #Ixtiyoriy string tipidagi qiymatni yani so'zni harflarga ajratib \nlistga joylab beruvchi funksiya
    harflar = []
    for harf in ixtiyoriy_soz:
        harflar.append(harf)
    return harflar

def yangi_list(harfli_list):
    #Argumentida turgan listga teng uzunlikga ega yangi list yaratadi
    uzunlik = len(harfli_list)
    
    new_list = []

    n = 0
    while n < uzunlik:
        n += 1
        new_list.append('-')
        
    return new_list





    

