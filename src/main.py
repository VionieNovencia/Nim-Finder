import src.search as search

def Search(user_input):
    suku_kata = user_input.split()
    int_input = []
    str1_input = []
    db = []

    for i in suku_kata:
        try:
            tes = int(i)
            int_input.append(i)
            int_found = True
        except:
            str1_input.append(i)

    if len(int_input) ==0:
        angkatan = None
        nim = None
    elif len(int_input) == 1:
        angkatan = int_input[0]
        nim = None
    else:
        if len(int_input[0]) == 2:
            angkatan = int_input[0]
            nim = int_input[1]
        elif len(int_input[1]) == 2:
            angkatan = int_input[1]
            nim = int_input[0]

    if str1_input == []:
        db = search.NimSearch(int_input[0])

    elif int_input == []:
        db = search.JurusanSearch(user_input)
        if db ==[]:
            for i in str1_input:
                db = search.JurusanSearch(i)
                if db != []:
                    break
        if db == []:
            db = search.NameSearch(user_input)
    else:
        db = search.JurusanAngkatanSearch(user_input)
        if db == []:
            db = search.CompleteSearch(angkatan, nim, str1_input)
    return db
