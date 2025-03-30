class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor

class Estacionamento:
    def __init__(self):
        self.vagas_totais = 100
        self.vagas_ocupadas = []

    def entrada_veiculo(self, veiculo):
        if len(self.vagas_ocupadas) < self.vagas_totais:
            self.vagas_ocupadas.append(veiculo)
            print(f'Veículo {veiculo.placa} entrou.')
        else:
            print('Estacionamento cheio.')

    def saida_veiculo(self, placa):
        for veiculo in self.vagas_ocupadas:
            if veiculo.placa == placa:
                self.vagas_ocupadas.remove(veiculo)
                print(f'Veículo {placa} saiu.')
                return
        print('Veículo não encontrado.')

    def listar_veiculos(self):
        if self.vagas_ocupadas:
            print('Veículos estacionados:')
            for veiculo in self.vagas_ocupadas:
                print(f'Placa: {veiculo.placa}, Modelo: {veiculo.modelo}, Cor: {veiculo.cor}')
        else:
            print('Nenhum veículo estacionado.')

if __name__ == "__main__":
    estacionamento = Estacionamento()

    while True:
        print("\n1. Entrada de veículo")
        print("2. Saída de veículo")
        print("3. Listar veículos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa: ")
            modelo = input("Digite o modelo: ")
            cor = input("Digite a cor: ")
            veiculo = Veiculo(placa, modelo, cor)
            estacionamento.entrada_veiculo(veiculo)
        elif opcao == "2":
            placa = input("Digite a placa do veículo a sair: ")
            estacionamento.saida_veiculo(placa)
        elif opcao == "3":
            estacionamento.listar_veiculos()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
