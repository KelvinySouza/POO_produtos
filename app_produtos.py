from MODELS.Produtos_Model import Produtos

def main():
    novoProduto = Produtos('Notebook', 2000, 10)
    print(novoProduto.consultar_preco('Notebook', 2000))
    print(novoProduto.exibir_quantidade(10))
    print(novoProduto.exibir_informacoes('Notebook', 2000, 10))

if __name__ == '__main__':
    main()