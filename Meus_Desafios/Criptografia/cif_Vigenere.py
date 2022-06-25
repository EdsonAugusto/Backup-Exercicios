from string import ascii_lowercase  # Biblioteca de caracteres


def gerador_lista (palavra): #funcao que transforma palavra em lista, recebe um parametro
	palavra, list_secreta = palavra.lower(), [] # torna palavra secreta totalmente minuscula
	for i in range(len(palavra)): #transforma palavra em lista
		list_secreta.append(palavra[i])
	return list_secreta # Devolve palavra secreta como lista

def lista_criptografada (segredo): # funcao que realiza a criptografia, recebe um parametro
	lista_secreta, alfabeto = [], list(ascii_lowercase) # Variavel que armazena alfabeto secreto, Variavel alfabeto
	for i in range(len(segredo)):#Laço q cria quantidades de listas e dicionarios necessarios conforme o tamanho da palavra secreta
		lista_secreta.append([]); lista_secreta[i].append({}) # Adiciona uma lista na matriz e um dicionario nessa lista
		indice = alfabeto.index(segredo[i].lower()) # indice de ponto de partida p criptografia 
		for k in range(len(alfabeto)): # cria lista e dicionario criptografado conforme palavra chave  
			lista_secreta[i][0][alfabeto[k]] = alfabeto[indice] #Funcionamento da cripto:Adiciona no dicionario lista polialfabetica conforme secredo
			indice+=1 # Adiciona +1 a indice p troca de caracter na proxima rodada 
			if indice >= len(alfabeto): indice = 0 # controle para variavel indice não estoura range maximo do alfabeto
	return lista_secreta # retorna lista com dicionario criptografado

def lista_descriptografada (segredo): # funcao que realiza a descriptografia de forma aocontraria da função original
	lista_secreta, alfabeto = [], list(ascii_lowercase) # Variavel que armazena alfabeto secreto, Variavel alfabeto
	for i in range(len(segredo)):#Laço q cria quantidades de listas e dicionarios necessarios conforme o tamanho da palavra secreta
		lista_secreta.append([]); lista_secreta[i].append({})  # Adiciona uma lista na matriz e um dicionario nessa lista
		indice = alfabeto.index(segredo[i]) # indice de ponto de partida p descriptografia 
		for k in range(len(alfabeto)): # cria lista e dicionario descriptografado conforme palavra chave  
			lista_secreta[i][0][alfabeto[indice]] = alfabeto[k]
			indice+=1 # Adiciona +1 a indice p troca de caracter na proxima rodada 
			if indice >= len(alfabeto): indice = 0 #controle para variavel indice não estoura range maximo do alfabeto
	return lista_secreta # retorna lista com dicionario descriptografado

def crip_Vigenere (mensagem, palavra_secreta, func='cript'):#recebe 3 paramentros #func==Criptografa ou descriptografa
	mensagem, saidaCript = mensagem.lower(), '' #deixa mensagem minuscula pois dicionario não opera com caracteres maiuculos, Variavel de saida
	if func == 'cript': #Func com valor de para criptografa mensagem
		list_polialfabetica = lista_criptografada(gerador_lista(palavra_secreta))#dicionario cript
	elif func == 'descript': #Func com valor de para descriptografa mensagem
		list_polialfabetica = lista_descriptografada(gerador_lista(palavra_secreta))#dicionario descript
	ind = 0 #indice de controle (função principal intercalar nas lista polialfabetica)
	for i in range(len(mensagem)):# Array para percorer mensagem
		if mensagem[i] in list(ascii_lowercase):#Condição p/ verificar se caracter da mensagem consta dentro do alfabeto
			saidaCript += list_polialfabetica[ind][0][mensagem[i]]#saida cript adicionado um novo caracter em cada rodada do array 
		else: saidaCript += mensagem[i] # Caso caractere não esteja no alfabeto, o mesmo é replicado na mensagem sem alteração
		if ind >= len(list_polialfabetica)-1: ind = 0 #Condição para o indice não ultrapassar tamanho da matriz
		else: ind += 1 #Caso condição seja falsa adiociona mais um para o indice pois na proxima interração vai ser usado outro dicionario
	return saidaCript #retorna mensagem

######################### MODO LINHA DE COMANDO #########################
func, inter= ('cript' , 'descript'), ('Criptografada', 'Descriptografada')#Listas:uma devolve p/ função paramentro necessario/ Outra mensag terminal
execut = True
while execut:
	chave = input('Entre com a Palavra secreta: ') # Pede palavra secreta
	funcao = int(input('[0] Para Criptografa -- [1] Para Descifrar: ')) # Opção que será utilizada
	mensagem = input('Entre com a mensagem a ser {}: '.format(inter[funcao])) # Mensagem para ser criptografada ou descifrada
	print('Resultado abaixo:\n',crip_Vigenere(mensagem, chave, func[funcao]).capitalize()) ## Saida para Usuario
	execut = input('\nDeseja executar novamente? [s] Sim | [n] Não: ')
	if execut == 's' or execut == 'S': print('################################################## '); execut = True
	else: execut = False

######################### MODO EXECUÇÃO SCRIPT ######################### (Descomentar linha para usar)
#(Exemplo como usar) print(crip_Vigenere('MENSAGEM', 'PALAVRA SECRETA', 'cript' ou 'descript')) ## Abaixo exemplo de execução
#print(crip_Vigenere('a minha caixa de lapis e  vermelha', 'CANDEEIRO', 'cript')) # Para Criptografa
#print(crip_Vigenere('c zlrli qcikd hm zcpvv i  jgrzhpli', 'CANDEEIRO', 'descript')) # Para Descifrar


#Fonte de estudo: https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re