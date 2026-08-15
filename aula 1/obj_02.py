class Produto:
    def __init__(self, codigo: int, descricao: str, preco: float) -> None:
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade_estoque = 0

    def entrada_estoque(self, quantidade: float) -> None:
        self.__quantidade_estoque += quantidade

    def saida_estoque(self, quantidade: float) -> None:
        self.__quantidade_estoque -= quantidade

    def visualizar_quantidade_em_estoque(self) -> None:
        print(f"A quantidade em estoque do produto {self.__descricao} eh {self.__quantidade_estoque}.")

if __name__ == "__main__":
    print("Executando no modelo Orientado a Objetos...")


    produto1 = Produto(1, 'Notebook', 3500.00)
    produto1.visualizar_quantidade_em_estoque()
    produto1.entrada_estoque(15)
    produto1.visualizar_quantidade_em_estoque()

    print(produto1._Produto__preco)