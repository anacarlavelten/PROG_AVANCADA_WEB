def cria_produto(codigo: int, descricao: str, preco: float, quantidade_estoque: float) -> dict:
   return {
       "codigo": codigo,
       "descricao": descricao,
       "preco": preco,
       "quantidade_estoque": quantidade_estoque
   }
def entrada_estoque(produto: dict, quantidade: float) -> None:
   produto["quantidade_estoque"] += quantidade

def saida_estoque(produto: dict, quantidade: float) -> None:
   produto["quantidade_estoque"] -= quantidade

def vizualizar_quantidade_em_estoque(produto: dict) -> None:
   print(f"A quantidade em estoque do produto{produto['descricao']} eh: {produto['quantidade_estoque']}")

if __name__ == "__main__":
      print("executando como script principal...")

      produto1 = cria_produto(1, "Notebook", 3500.0, 10)
      vizualizar_quantidade_em_estoque(produto1)

      produto2 = cria_produto(2, "Celular", 2000.00, 5)
      vizualizar_quantidade_em_estoque(produto2)