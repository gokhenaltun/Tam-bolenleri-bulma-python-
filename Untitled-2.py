sayi = int(input("Tam Bölenlerini Bulmak İstediğiniz Sayı : "))
print("Girdiğin Sayının Tam Bölenleri:")
for i in range(1,(sayi+1)):
        if(sayi % i == 0):
            print(i)