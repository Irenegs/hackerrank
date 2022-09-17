import string

def print_rangoli(size):
    '''    #alphabets_in_lowercase=[]
    #for i in range(97,123):
    #alphabets_in_lowercase.append(chr(i))
    #letters=['a','b',c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]#g=chr(45)
    ch=string.ascii_lowercase
    L=[]#para guardar las líneas de la parte inferior
    for i in range(1,size+1):
        border='-'*(2*size-2*i)
        central=ch[size-i]
        for j in range(1,i):
            central=ch[size-i+j]+'-'+central+'-'+ch[size-i+j]
        l=border+central+border
        print(l)
        if i<size:
            L.append(l)
    for i  in range(len(L)):
        print(L[len(L)-(i+1)])'''
    ch=string.ascii_lowercase
    L=[]
    for i in range(1,size+1):
        border='-'*(2*size-2*i)
        central=ch[size-i]
        for j in range(1,i):
            central=ch[size-i+j]+'-'+central+'-'+ch[size-i+j]
        l=border+central+border
        L.insert(i-1,l)
        if i!=size:
            L.insert(len(L)-(i-1),l)
    s='\n'.join(L)
    print(s)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
