import numpy as np

class matrix:

    def inmatrix(x,y):
        array = []
        matriks = []
        for i in range(x):
            for j in range(y):
                a = int(input("Masukkan baris ke {} dan kolom ke {} :".format(j,i)))
                array.append(a)
            matriks.append(array)
            array = []
        return np.asarray(matriks)

    def perkalianDuaMatriks():

        try:

            baris_m1 = int(input("Masukkan baris matriks 1 : "))
            kolom_m1 = int(input("Masukkan kolom matriks 1 : "))
            baris_m2 = int(input("Masukkan baris matriks 2 : "))
            kolom_m2 = int(input("Masukkan kolom matriks 2 : "))

            if kolom_m1 != baris_m2 : 
                print("Ordo yang anda masukkan tidak sesuai")
            else : 
                print("Masukkan matriks 1 : ")
                matriks1 = inmatrix(kolom_m1, baris_m1)
                print("Masukkan matriks 2 : ")
                matriks2 = inmatrix(kolom_m2, baris_m2)
                print(np.dot(matriks1,matriks2))

        except ValueError:
            print("Harus ada isinya.")

    def perkalianSkalar():

        b = int(input("Masukkan bilangan : "))
        baris_m1 = int(input("Masukkan baris matriks 1 : "))
        kolom_m1 = int(input("Masukkan kolom matriks 1 : "))
        print("Masukkan matriks : ")
        matriks1 = inmatrix(kolom_m1, baris_m1)
        print(b*matriks1)

def main():
    try:
        userInput = input("1. Perkalian dua matriks \n2. Perkalian matriks skalar\nPILIHAN : ")
        if int(userInput) == 1 :
            matrix.perkalianDuaMatriks()    
        elif int (userInput) == 2:
            matrix.perkalianSkalar()
        else : 
            print("anda bodoh")
    except ValueError:
        print("Hanya bisa dimasukkan angka saja")


if __name__ == "__main__": 
    main()