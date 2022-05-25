class Programa:
    def __init__(self, nome, ano):   # def: Atributos / __init__: Inicializador
        self._nome = nome.title()    # As classes "Filme" e "Serie" irão conter informações da classe "Programa", sendo assim aplicado o conceito de Herança. Isso é uma vantagem pois todas as subclasses tem acesso aos métodos criados na superclasse e a herança faz com que o código não fique duplicado, reduzindo os pontos de falha.
        self.ano = ano               # O inicializador __init__ sempre receberá self, e também passaremos outros atributos: nome e ano. Com estes dois devemos preencher os dois valores do objeto na nossa instancia. Por isso usamos self.nome e self.ano.
        self._likes = 0              # A vantagem de criar uma classe com construtor __init__ é que fica mais fácil criar com o inicializador, já que informamos os argumentos.
                                     # Sem o construtor nós precisaríamos definir os atributos depois de instanciar, teríamos o trabalho de descobrir quais atributos definir. 

    @property                        # Para definir algo que será modificado posteriormente, e que não será definido no momento da criação do objeto devemos ter um método para inserir a informação
    def likes(self):                 # e modificar seu estado recém criado. Usaremos isso para a aplicação dos likes.
        return self._likes           # Usaremos o @property para dar essa funcionalidade aos métodos para fazer com que ajam como getters e setters

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)                     # A função super() chama qualquer método ou atributo da classe mãe. Ele usa em parte o comportamento da superclasse e adiciona alguma nova funcionalidade.
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():                           # É necessario criar uma classe pra representar as diferentes playlists.
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):            # Duck Typing: (__getitem__): Permite que a classe seja considerada um objeto iterável. Este método define algo que é iterável e, no caso, precisaremos receber um item para que este seja repassado à lista interna que estamos utilizando, isto é, "programas".
        return self._programas[item]        # Indica ao Python que a classe poderia ser usada para um for in, ou um in, para verificar se o item está contido em uma determinada lista, e também poderíamos acessar um item específico por meio do seu índice.

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')
# Dentro de {} incluiremos o atributo que queremos imprimir.