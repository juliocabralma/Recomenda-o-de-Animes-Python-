import csv, sys
nome_ficheiro = 'rating_complete.csv'
j=0
k=0
l=0
##Guarda os ids dos animes dos quais o id do usuário deu nota maior que 9
gente = dict()
##Guarda todo o arquivo em um dicionário separado pelo id do usuário, de animes e as notas
ocorrencias = dict()
##Guarda todos ids dos usuários que deram nota maior que 9 pros animes que o usuário deu nota boa também, 
## tendo repetição nos ids guardados
melhoresAvaliacoes = dict()

print()
print("Digite o id do usuário que você deseja receber recomendação de animes: ")
ida = input()
ida = int(ida)
print()

with open(nome_ficheiro, 'rt') as ficheiro:
	reader = csv.reader(ficheiro)
	header = True
	try:
		i=0
		for linha in reader:
			if header:
				header = False
				continue			
			user_id = int(linha[0])
			anime_id = int(linha[1])
			rating = int(linha[2])
			##Armazenando todo o arquivo no dicionário ocorrencias
			ocorrencias[k] = [user_id, anime_id, rating]
			k=k+1
			##Testando se o id pego no teclado é o mesmo que o id que tô lendo da linha no momento,
			##e se a nota for maior que 9, se sim eu armazeno os ids dos animes no dicionário gente
			if ida==user_id and rating >9: 
					gente[j] = anime_id
					j = j+1
			if user_id>10000: break

	except csv.Error as e:
		sys.exit('ficheiro %s, linha %d: %s' % (nome_ficheiro, reader.line_num, e))
ficheiro.close()

##Percorro todo o arquivo que tá armazenado em ocorrencias e comparo com os ids de animes que tão armazenados
##em gente, se se o id de ocorrencias for igual ao de gente e se a nota for maior que 9 eu armazeno todos
##os ids dos usuários em MelhoresAvaliacoes
for i in ocorrencias.values():
	for j in gente.values():
		if(i[1]==j and i[2]>9 and i[0]!=ida):
			melhoresAvaliacoes[l] = i[0]
			l=l+1

chavedef=0
maior=0

##Agora eu procuro pegar o usuário que tem maior número de ocorrências em MelhoresAvaliacoes, afim de que
##ele possa ser mais parecido com o id que o usuário digitou no teclado, depois que eu pego o id de usuário
##que mais se repete eu armazeno na variável chavedef para servir de parâmetro de busca depois
for i in melhoresAvaliacoes.values():
	contador=0
	for j in melhoresAvaliacoes.values():
		if(i==j):
			contador=contador+1
	if(contador>maior):
		maior=contador
		chavedef=i

contador = 0
aux=-1
##Por último ando a ocorrencias que tem todo o arquivo armazenado e comparo com os ids de animes que estão
##em gente, eu comparo o id de ocorrencias com o id do usuário que mais se repetiu anteriormente armazenado
##em chavedef e testo se se o id do anime que eu vou pegar é diferente do que o usuário do começo tinha
##dado, pois para recomendar um anime tem que ser diferente de um que ele tenha votado e uso um padrão de
##nota acima de 8 para que seja recomendado, basicamente esse foi o sistema de recomendação que eu fiz
for i in ocorrencias.values():
	for j in gente.values():
		if(i[0]==chavedef and i[1]!=j and i[2]>=8 and i[1]!=aux and contador<3):
			contador=contador+1	
			aux = i[1]
			resposta = 'O anime número ' + repr(contador) + ' indicado é o anime de id: ' + repr(i[1])
			print(resposta)
		if(contador==3):
			break
	if(contador==3):
		break

