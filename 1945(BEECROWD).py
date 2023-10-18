v1,v2 = dict(), 0
while True:
    try:
        s = input().replace('+',':=').split(' := ')
        if len(s)==2:
            v1[s[0]]=int(s[1]);v2=int(s[1])
        else:
            try:
                soma = v1[s[1]]
            except:
                soma = int(s[1])
            
            try:
                soma2 = v1[s[2]]
            except:
                soma2 = int(s[2])
            
            v1[s[0]], v2 = soma + soma2, soma + soma2
    except EOFError:
        print(v2);break