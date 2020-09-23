#sintaxe de uma função em python.
  #não botar em letra maicusla, se for composto usar letra maiuscula na proxima palavra
def inicio():
    print("Primeira função")
#necessario chamar a função para executar ela 
#inicio()

def passandoParametro(nome):
    print("meu nome é", nome)

#passando string
passandoParametro("Artur")
#passando boolean
passandoParametro(True)
#passando float
passandoParametro(1.58)

#pode colocar varios parametros, e os argumentos tem que terem a mesma quantidade dos parametros
def passandoParametro(nome, sobrenome):
    print("o nome dele é", nome, sobrenome)

#passando string
passandoParametro("Jorge", "Silva")
#passando boolean
passandoParametro(True, False)
#passando float
passandoParametro(1.58, 3)

#criar uma função com quantidade de parametros indefiinda
#o valor da variavel fica em forma de tulpa (por isso é necessario botar igual uma lista.)
def passandoParametroIndefinido(*nome):
    print("o nome dela é:", nome[0], nome[1], nome[2])

passandoParametroIndefinido("aaaaa", "aaaaaa", "da aaaaa")

#passando parametro definido com chave, não importa a ordem dos parametros e argumentos
def passandoParametroChave(nome, idade, cpf):
    print("meu nome é", nome, "tenho", idade, "anos e meu cpf é", cpf)

passandoParametroChave(nome="Artur,", idade="16", cpf="000000000000000")

#passsando parametro indefinido com chave
def passandoParametroIndefinidoChave(**dados):
    print("Informações pessoais:", dados["idade"], dados["nome"] )

passandoParametroIndefinidoChave(nome="Artur,", idade="16 anos,", cpf="000000000")

#passando parametro definido com padrão
def passandoParametroComPadrao(nome = "sem nome"):
    print("bem vindo,", nome)

passandoParametroComPadrao("Artur")
passandoParametroComPadrao()

#passando lista por parametro

def passandoListaPorParametro(lista):
    for i in lista:
        print(i)

minhaLista = ['Artur', 'Fadbricio']

passandoListaPorParametro(minhaLista)

#se criar uma função vazia
def funcaoVazia():
    pass

#função com retorno
def retornaValor(nome):
    if nome == "Artur":
        return True
    else:
        return False

recebeRetorno = retornaValor("Aaaartur")

if recebeRetorno == True:
    print("é o aluno")
else:
    print("é não!")

print("é o aluno", retornaValor("Artur"))