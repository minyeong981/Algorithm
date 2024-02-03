alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S = input()

for ele in alph :
    if ele in S :
        print(S.index(ele), end =' ')
    else :
        print(-1, end = ' ')