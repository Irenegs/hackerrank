for i in range(int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    #print(*[i]*i, sep='')
    #print(str(i)*i)
    #print((i*(10**10+10**9+10**8+10**7+10**5+10**4+10**3+100+10+1))%10**i)#Triangle Quest 1
	print(pow(10,i)*(i+1)+sum(map(lambda x:(pow(10,x)+pow(10,2*i-x))*(x+1), range(i))))#TRiangleQuest2 - palindromic 
