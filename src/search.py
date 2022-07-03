import json
from KMP import *

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
    
    jurusan = x.split()[0].upper()
    angkatan = x.split()[1]
    kjurusan=[]
    if jurusan in data_kf:
        kjurusan.append(data_kf[jurusan])
    elif jurusan in data_kj:
        kjurusan.append(data_kj[jurusan])
    else:
        keys_j = list(data_lj.keys())
        for i in keys_j:
            if KMP(data_lj[i],jurusan):
                kjurusan.append(i)
        # keys_f = list(data_lf.keys())
        # for i in keys_f:
        #     if KMP(data_lf[i],jurusan):
        #         kjurusan.append(i)
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

def JurusanSearch(jurusan):
    db = []
    kjurusan=[]
    keys_j = list(data_lj.keys())
    for i in keys_j:
        if KMP(data_lj[i],jurusan.upper()):
            kjurusan.append(i)
    # keys_f = list(data_lf.keys())
    # for i in keys_f:
    #     if KMP(data_lf[i],jurusan):
    #         kjurusan.append(i)

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
            if KMP(item[0],nama):
                try:
                    mahasiswa = [item[0],item[1],item[2],data_lf[item[1][0:3]],data_lj[item[2][0:3]]]
                except:
                    mahasiswa = [item[0],item[1],"-",data_lf[item[1][0:3]],"-"]
                if mahasiswa not in db:
                    db.append(mahasiswa)
    return db
