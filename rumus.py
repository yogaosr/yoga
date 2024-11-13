def luas_segitiga(): #soal no 2
    alas = float(input('Masukan alas segitiga: '))
    tinggi = float(input("Masukan tinggi segitiga: "))
    luas = 1 / 2 * alas * tinggi
    print("Luas segitiga : ", luas)
    return luas

def keliling_segitiga():
    s1 = float(input("Masukan sisi 1 segitiga: "))
    s2 = float(input("Masukan sisi 2 segitiga: "))
    s3 = float(input("Masukan sisi 3 segitiga: "))
    keliling = s1 + s2 + s3 
    print("Keliling Segitiga : ", keliling)
