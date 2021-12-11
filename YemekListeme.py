
def Lİstele():
    with open("Liste.txt", "r") as FILEYemek:
        for yemekler in FILEYemek:
            print(yemekler)


def YemekEkle():
    yemekad = input("Yemek Adi Gir: ")
    with open("Liste.txt", "a") as FILEYemek:
        FILEYemek.write(yemekad + '\n')



def MalzemeEkle():
    malzemeler = input('Malzemeleri Gir: ')

    with open("Liste.txt", "a") as FILEYemek:
        FILEYemek.write(malzemeler + '\n')


while True:
    Food = input('1- Listele \n 2- Yemek Ekle \n 3-Malzeme Ekle \n 4- Exit\n')

    if Food == '1':
        Lİstele()
    elif Food == '2':
        YemekEkle()
    elif Food == '3':
        MalzemeEkle()
    else:
        break

