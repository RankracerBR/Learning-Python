C = int(input())

while C > 0:
    C -= 1
    R = int(input())
    vetor = []
    
    for i in range(R):
        if i % 2==0:
            vetor.append(1)
        else:
            vetor.append(-1)
    print(sum(vetor))