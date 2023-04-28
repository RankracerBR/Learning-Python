casos = int(input())
sons = ['PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY','SALT','ANSWER!','RAR?','WIFI ANTENNAS']

for i in range(casos):
    x,y = map(int, input().split())
    print(sons[x+y])