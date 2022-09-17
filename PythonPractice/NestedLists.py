if __name__ == '__main__':
    datos=[]
    scores=[]
    Names=[]
    for k in range(int(input())):
        name = input()
        score = float(input())
        datos.append([name, score])
        scores.append(score)
    scoreset=set(scores)
    sortedscore=sorted(scoreset)
    SC=sortedscore[1]
    for k in range(len(scores)):
        if datos[k][1]==SC:
            Names.append(datos[k][0])
    sortednames=sorted(Names)
    for k in range(len(Names)):
        print(sortednames[k])
