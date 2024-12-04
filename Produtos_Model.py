class Produtos:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def consultar_preco(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
        return f'Nome: {self.__nome}, Preco: {self.__preco}'

    def exibir_quantidade(self, quantidade):
        self.__quantidade = quantidade
        return f'Quantidade: {self.__quantidade}'
    
    def  exibir_informacoes(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco        
        self.__quantidade = quantidade
        return f'Nome: {self.__nome}, Preco: {self.__preco}, Quantidade: {self.__quantidade}'