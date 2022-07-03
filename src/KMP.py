txt = "abacaabaccabacabaabb"
pat = "abacab"

def KMP(text,pat):
    n = len(text)
    m = len(pat)

    i=0
    j=0

    array = jump(pat,m)
    while(i<n):
        #print("text[" + str(i) +"]" + text[i] + "="+ "pat[" + str(j) + "]" + pat[j]+"\n")
        if text[i] == pat[j]:
            if j==m-1:
                return True
            i+=1
            j+=1
        elif j>0:
            j = array[j]
        else:
            i+=1
    return False

            
            
# mencari banyak preffix = suffix           
def jump(pat,size):
    array = [ 0 for i in range(size)]
    j=2
    for j in range(size):
        a = j//2
        
        while a>0 :
            head = pat[0: a]
            tail = pat[j - a : j]

            if(head == tail):
                array[j] = len(head)
                break
            a -= 1
            
    return array

# print(jump(txt,len(pat)))
# print(KMP(txt,pat))










