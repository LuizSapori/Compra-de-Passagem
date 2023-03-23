class Caneca:
    formato = "Cilindrico com alça lateral" # Algo estático que vai pertencer a todas as canecas.

    def __init__(self,nome,logo,cor):
        self.nome = nome # Os nomes dentro do self mudaram de caneca para caneca.
        self.logo = logo
        self.cor = cor
        self.status = "Cheia"

    def beber(self):
        self.status = "Vazia"
        return f" É da {self.nome} que eu estou bebendo."

    def encher(self):
        self.status = "Cheia"
        return f" Estou enchendo a  {self.nome}."

class CanecaLondrina(Caneca):
    def __init__(self):
        super().__init__("Caneca Londrina","Cidade de Londres","Branca")

    def extras(self):
        print("Como bônus você ganha uma colher.")

class CanecaBatman(Caneca):
    def __init__(self):
        super().__init__("Caneca Gotham","Batmam","Preta")

    def som(self):
        print('Im Batmam!!')

caneca_Londres = CanecaLondrina()
caneca_ByLearn = Caneca('Caneca ByLeaner','Foguete ByLeaner','Azul')
caneca_batman = CanecaBatman()

caneca_Londres.extras()
caneca_batman.som()