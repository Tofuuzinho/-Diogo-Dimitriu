class ProdutoInexistenteError(Exception):  # Cria uma classe de erro personalizada para quando um produto não existe
    pass  # Classe vazia que herda comportamentos da classe Exception

class SaldoInsuficienteError(Exception):  # Cria uma classe de erro personalizada para quando o saldo é insuficiente
    pass  # Classe vazia que herda comportamentos da classe Exception

# Dicionário que guarda os produtos disponíveis da loja
produtos = {
    "1": {"nome": "Camisola", "preco": 20.0},  # Produto 1: Camisola com preço de 20€
    "2": {"nome": "Calças", "preco": 50.0},    # Produto 2: Calças com preço de 50€
    "3": {"nome": "Ténis", "preco": 100.0},    # Produto 3: Ténis com preço de 100€
    "4": {"nome": "Chapéu", "preco": 15.0},    # Produto 4: Chapéu com preço de 15€
}

# Funções principais
def exibir_produtos():  # Função que mostra todos os produtos disponíveis
    print("\nProdutos disponíveis:")  # Imprime um cabeçalho para a lista de produtos
    for codigo, info in produtos.items():  # repete através de cada produto no dicionário
        print(f"{codigo} - {info['nome']} - {info['preco']:.2f}€")  # Mostra o código, nome e preço formatado de cada produto

def adicionar_ao_carrinho(carrinho, produto, quantidade):  # Função para adicionar produtos ao carrinho
    if produto not in produtos:  # Verifica se o código do produto existe
        raise ProdutoInexistenteError("Produto não encontrado.")  # Lança uma exceção se o produto não existir
    if quantidade <= 0:  # Verifica se a quantidade é válida
        raise ValueError("A quantidade deve ser maior que zero.")  # Lança uma exceção se a quantidade for zero ou negativa
    if produto in carrinho:  # Verifica se o produto já existe no carrinho
        carrinho[produto] += quantidade  # Se já existe, incrementa a quantidade
    else:
        carrinho[produto] = quantidade  # Se não existe, adiciona o produto ao carrinho
    print(f"{quantidade}x {produtos[produto]['nome']} adicionado(s) ao carrinho.")  # Confirma a adição do produto

def calcular_total(carrinho):  # Função para calcular o valor total do carrinho
    total = 0  # Inicializa o total como zero
    for produto, quantidade in carrinho.items():  # Itera através de cada produto no carrinho
        total += produtos[produto]["preco"] * quantidade  # Adiciona o preço do produto multiplicado pela quantidade ao total
    return total  # Retorna o valor total

def simular_pagamento(carrinho, saldo):  # Função para simular o pagamento
    if not carrinho:  # Verifica se o carrinho está vazio
        raise ValueError("O carrinho está vazio.")  # Lança uma exceção se o carrinho estiver vazio
    total = calcular_total(carrinho)  # Calcula o valor total do carrinho
    if saldo < total:  # Verifica se o saldo é suficiente
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o pagamento.")  # Lança uma exceção se o saldo for insuficiente
    print(f"Pagamento de {total:.2f}€ realizado com sucesso!")  # Confirma o pagamento bem-sucedido
    return saldo - total  # Retorna o saldo atualizado após o pagamento

# Função principal
def main():  # Função principal que executa o programa
    carrinho = {}  # Inicializa o carrinho como um dicionário vazio
    saldo = 500.0  # Define um saldo inicial fictício

    while True:  # Inicia um loop infinito para o menu principal
        try:  # Inicia um bloco try-except para tratar erros
            print("\n1 - Exibir produtos")  # Mostra a opção 1 do menu
            print("2 - Adicionar ao carrinho")  # Mostra a opção 2 do menu
            print("3 - Ver carrinho e total")  # Mostra a opção 3 do menu
            print("4 - Pagamento")  # Mostra a opção 4 do menu
            print("5 - Sair")  # Mostra a opção 5 do menu
            opcao = int(input("Escolha uma opção: "))  # Solicita a entrada do utilizador para um número inteiro

            if opcao == 1:  # Se a opção escolhida for 1
                exibir_produtos()  # Chama a função para exibir produtos
            elif opcao == 2:  # Se a opção escolhida for 2
                exibir_produtos()  # Mostra os produtos disponíveis
                produto = input("Coloca o código do produto: ")  # Solicita o código do produto
                quantidade = int(input("Coloca a quantidade: "))  # Solicita e converte a quantidade para um número inteiro
                adicionar_ao_carrinho(carrinho, produto, quantidade)  # Chama a função para adicionar ao carrinho
            elif opcao == 3:  # Se a opção escolhida for 3
                print("\nCarrinho:")  # Imprime um cabeçalho para o carrinho
                for produto, quantidade in carrinho.items():  # Itera através de cada item no carrinho
                    print(f"{quantidade}x {produtos[produto]['nome']} - {produtos[produto]['preco'] * quantidade:.2f}€")  # Mostra quantidade, nome e preço total de cada item
                print(f"Total: {calcular_total(carrinho):.2f}€")  # Mostra o valor total do carrinho
            elif opcao == 4:  # Se a opção escolhida for 4
                saldo = simular_pagamento(carrinho, saldo)  # Simula o pagamento e atualiza o saldo
                carrinho.clear()  # Limpa o carrinho após o pagamento
                print(f"Saldo restante: {saldo:.2f}€")  # Mostra o saldo restante
            elif opcao == 5:  # Se a opção escolhida for 5
                print("ACABOU!")  # Mostra uma mensagem de término
                break  # Sai do loop infinito, terminando o programa
            else:  # Se for escolhida uma opção inválida
                print("Opção inválida.")  # Mostra uma mensagem de erro
        except ProdutoInexistenteError as e:  # Captura a exceção de produto inexistente
            print(f"Erro: {e}")  # Mostra a mensagem de erro
        except SaldoInsuficienteError as e:  # Captura a exceção de saldo insuficiente
            print(f"Erro: {e}")  # Mostra a mensagem de erro
        except ValueError as e:  # Captura erros de valor (entradas inválidas)
            print(f"Erro: Entrada inválida. {e}")  # Mostra a mensagem de erro
        except Exception as e:  # Captura qualquer outro tipo de exceção não tratada
            print(f"Erro inesperado: {e}")  # Mostra a mensagem de erro
        finally:  # Bloco que é executado sempre, independentemente de ocorrer uma exceção ou não
            print("\nOperação finalizada.")  # Mostra uma mensagem de finalização da operação

main()  # Chama a função principal para iniciar o programa