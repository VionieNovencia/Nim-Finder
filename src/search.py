import json
from KMP import *
import helper

#open file
with open('data/data_13_21.json') as f1:
    data1 = json.load(f1)
with open('data/list_fakultas.json') as f2:
    data_lf = json.load(f2)
with open('data/list_jurusan.json') as f3:
    data_lj = json.load(f3) 
with open('data/kode_fakultas.json') as f4:
    data_kf = json.load(f4)
with open('data/kode_jurusan.json') as f5:
    data_kj = json.load(f5)

def NimSearch(x):
    db = []         
    for i in range(len(data1)):
        item = data1[i]
        found = KMP(item[1],x)
        if not found:
            try:
                found = KMP(item[2],x)
            except:
                pass
        if found:
            try:
                mahasiswa = [item[0],item[1],item[2],data_lf[item[1][0:3]],data_lj[item[2][0:3]]]
            except:
                mahasiswa = [item[0],item[1],"-",data_lf[item[1][0:3]],"-"]
            db.append(mahasiswa)   
        i += 1
    return db

def JurusanAngkatanSearch(x):
    db = []         
    x = x.split()
    jur = x[0:len(x)-1]
    jurusan = " ".join(jur)
    angkatan = x[len(x)-1]
    
    kjurusan = getKodeJurusan(jurusan.capitalize())
    if kjurusan == []:
        kjurusan = getKodeJurusan(jurusan)

    for a in kjurusan:
        NIM = a+angkatan
        db1 = NimSearch(NIM)
        if db == []:
            db = db1
        else:
            for item in db1:
                if item not in db:
                    db.append(item)        
    return db

def getKodeJurusan(jurusan):
    kjurusan=[]
    keys_j = list(data_lj.keys())
    keys_kj = list(data_kj.keys())
    keys_kf = list(data_kf.keys())

    if jurusan.upper() in keys_kj:
        kjurusan.append(data_kj[jurusan.upper()])
    if kjurusan == [] and jurusan.upper() in keys_kf:
        kjurusan.append(data_kj[jurusan.upper()])
    
    if kjurusan == [] :
        for i in keys_j:
            if KMP(data_lj[i],jurusan.capitalize()):
                kjurusan.append(i)

    kjurusan = helper.unique(kjurusan)
    return kjurusan

def JurusanSearch(jurusan):
    db = []
    kjurusan = getKodeJurusan(jurusan.capitalize())
    if kjurusan == []:
        kjurusan = getKodeJurusan(jurusan)
    for NIM in kjurusan:
        for item in data1:
            if item[1][0:3] == NIM:
                try:
                    mahasiswa = [item[0],item[1],item[2],data_lf[item[1][0:3]],data_lj[item[2][0:3]]]
                except:
                    mahasiswa = [item[0],item[1],"-",data_lf[item[1][0:3]],"-"]
                db.append(mahasiswa)
            else:
                try:
                    if item[2][0:3] == NIM:
                        mahasiswa = [item[0],item[1],item[2],data_lf[item[1][0:3]],data_lj[item[2][0:3]]]
                        db.append(mahasiswa)
                except:
                    pass
    return db

def NameSearch(name):
    db = []
    try:
        list = name.split()
    except:
        list = [name]
    for nama in list:
        for item in data1:
            if KMP(item[0].lower(),nama.lower()):
                try:
                    mahasiswa = [item[0],item[1],item[2],data_lf[item[1][0:3]],data_lj[item[2][0:3]]]
                except:
                    mahasiswa = [item[0],item[1],"-",data_lf[item[1][0:3]],"-"]
                if mahasiswa not in db:
                    db.append(mahasiswa)
    return db

def CompleteSearch(angkatan, nim, str_input):
    db1 = [] #pencarian nim
    db2 = [] #pencarian nama
    result = []

    list_jurusan = helper.powerset(str_input)
    for item in list_jurusan:
        kode_jurusan = getKodeJurusan(item)
        if kode_jurusan != []:
            for kode in kode_jurusan:
                try: 
                    NIM = kode+angkatan+nim
                except:
                    NIM = kode+angkatan
                tes = NimSearch(NIM)
                for element in tes:
                    if element not in db1:
                        db1.append(element)
    
    db2 = NameSearch(" ".join(str_input))
    result = helper.intersection(db1,db2)
    result = helper.unique(result + db1 + db2)
    return result
                
        


    



# db = CompleteSearch("Tito IF 19  007")
# if db == []:
#     print("No results found")
# else:
#     for i in range(5):
#         print("Nama: " + db[i][0])
#         print("NIM Fakultas: " + db[i][1])
#         print("NIM Jurusan: " + db[i][2])
#         print("Fakultas: " + db[i][3])
#         print("Jurusan: " + db[i][4])
#         print()

