
import shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Projetos/globallabs/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()
    
    def atualizar_arquivo(nome_arquivo, texto):
        arquivo = open('teste.txt', 'a')
        arquivo.write(texto)
        arquivo.close()
    def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)

    def media_notas(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        aluno_nota = arquivo.read()
        print(aluno_nota)
        aluno_nota = aluno_nota.split('\n')
        print(aluno_nota)
        lista_media = []
        for x in aluno_nota:
            lista_notas = x.slipt(',')
            aluno = lista_notas[0]
            lista_notas.pop(0)
            print(lista_notas)
            #print(sum(lista_notas))
            media = lambda notas: sum([i for i in notas]) / 4
            print(media(lista_notas))
            lista_media.append({aluno: media(lista_notas)})
            return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C/Projetos/globallabs/')

def move_arquivo(nome_arquivo)
    shutil.move(nome_arquivo, 'C:/Projetos/globallabs')
if __name__ == '__main__':
     move_arquivo('notas.txt')
     #copia_arquivo('notas.txt')
     #escrever_arquvo('Primeira linha. \n')
    #aluno = '\nRafael,10,10,5,5\n'
     #atualizar_arquivo('notas.txt', aluno)   