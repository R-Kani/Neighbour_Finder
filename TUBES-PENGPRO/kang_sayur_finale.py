dict_ganjil = {}
dict_genap = {}

def nomor_rumah(nama): # fungsi untuk cek nama penghuni dan return key
    for key,value in dict_ganjil.items():
        if value == nama:
            return key
    
    for key,value in dict_genap.items():
        if value == nama:
            return key
    return "tidak tahu"

def penghuni_rumah(nomor): #fungsi untuk cek nomor rumah dan return penghuni
    for key,value in dict_ganjil.items():
        if key == nomor:
            return value
    
    for key,value in dict_genap.items():
        if key == nomor:
            return value 
    return "tidak tahu"

def genap_test(nomor): #fungsi untuk cek nomor rumah genap
    return nomor % 2 == 0
 
def update_dict(x,pos,arah,a,b): #fungsi untuk update dictionary
    m = nomor_rumah(a)
    n = genap_test(m)
    if pos == 'seberang':
        if n:
           m -= 1
        else:
            m += 1
    if arah == 'kiri':
        m -= 2*x
    else:
        m += 2*x

    if genap_test(m):
        dict_genap[m] = b
    else:
        dict_ganjil[m] = b

f = open("Data_Rumah.txt", 'r')
variable = f.readline()
x,y = str(variable).split()
dict_ganjil[int(x)] = 'anda'
f.close()     

with open("Data_Rumah.txt") as f: #untuk membuka file text
    for line in range(1):
        next(f)
    for line in f:
        c, d, e, f, g, h, i, j, k, l = str(line).split()
        update_dict(int(c), e, f, h, l)

def main_proram():
    print("23. GOSIP KANG SAYUR ; (1301213269)")
    print("-")
    print("Dictionary yang diperoleh adalah sbb.")
    print("Rumah Ganjil", dict_ganjil)
    print("Rumah Genap ", dict_genap)
    print("-")
    print('''Pilihlah program yang ingin dijalankan:
[1] Mencari Nomor Rumah Penghuni
[2] Mencari Nama Penghuni Rumah
[3] End Program
 ''')
    input_user = int(input())
    while input_user != 3:
        if input_user == 1:
            command1 = input("/?/ Input Nama Keluarga: ")
            print(command1, "tinggal di rumah No.",nomor_rumah(command1))
            
        if input_user == 2:
            command2 = int(input("/?/ Input Nomor Rumah: "))
            print("Nomor rumah", command2, "dihuni oleh keluarga", penghuni_rumah(command2))

        print("")
        print(">>>")
        input_user = int(input("Pilih kembali program: "))
        
main_proram()






