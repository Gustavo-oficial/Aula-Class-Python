from datetime import date, datetime
from pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    while True:
        lista_PessoasFisicas : PessoaFisica = []
        lista_PessoasJuridicas = []
        opcao = int(input("Escolha opçao: 1 -Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_Pf = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Fisicas / 0 - Voltar menu anterior"))

                if opcao_Pf == 1:
                    novapf = PessoaFisica()
                    novo_endereco_pf = Endereco()

                    novapf.nome = str(input("Digite o nome da pessoa fisica: "))
                    novapf.cpf = str(input("Digite o CPF da pessoa fisica: "))
                    novapf.rendimento = float(input("Digite o rendimento da pessoa fisica: "))
                    
                    data_nascimento = input("Digite a data de nascimento da pessoa fisica: ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()

                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade < 18:
                        print("A pessoa tem menos de 18 anos. Retornando ao menu")
                        continue
                    
                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                    novo_endereco_pf.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                    novo_endereco_pf.logradouro = input("Digite o logradouro da pessoa fisica: ")
                    novo_endereco_pf.numero = input("Digite o numero da pessoa fisica: ")
                    
                    novapf.endereco = novo_endereco_pf

                    lista_PessoasFisicas.append(novapf)

                    print("Cadastro realizado")
                elif opcao_Pf == 2:
                    if lista_PessoasFisicas:
                        for pessoaFisica in lista_PessoasFisicas:
                            enderecoPessoaFisica = pessoaFisica.endereco

                            print(
                                "Nome:", pessoaFisica.nome, 
                                "CPF:", pessoaFisica.cpf, 
                                "Data de Nascimento:", pessoaFisica.dataNascimento,
                                "Rendimento:", pessoaFisica.rendimento,
                                "Imposto a ser pago:", pessoaFisica.calcular_imposto(pessoaFisica.rendimento),
                                "Logradouro:", enderecoPessoaFisica.logradouro,
                                "Número:", enderecoPessoaFisica.logradouro
                            )
                    else:
                        print("Lista vazia")
                elif opcao_Pf == 0:
                    print("Retornando ao menu")
                    break
                else:
                    print("Opçao invalida")
                    break
        elif opcao == 2:
            while True:
                opcao_Pj = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Juridica / 0 - Voltar menu anterior"))

                if opcao_Pj == 1:
                    novaPJ = PessoaJuridica()
                    novo_endereco_pj = Endereco()

                    novaPJ.nome = str(input("Digite o nome da pessoa juridica: "))
                    novaPJ.cnpj = str(input("Digite o CNPJ da pessoa juridica: "))
                    novaPJ.rendimento = float(input("Digite o rendimento da pessoa juridica: "))
                    
                    novo_endereco_pj.logradouro = input("Digite o logradouro da pessoa juridica: ")
                    novo_endereco_pj.numero = input("Digite o numero da pessoa juridica: ")
                    
                    novaPJ.endereco = novo_endereco_pj

                    lista_PessoasJuridicas.append(novaPJ)

                    print("Cadastro realizado")
                elif opcao_Pj == 2:
                    if lista_PessoasJuridicas:
                        for pessoaJuridica in lista_PessoasJuridicas:
                            enderecoPessoaJuridica = pessoaJuridica.endereco

                            print(
                                "Nome:", pessoaJuridica.nome, 
                                "CNPJ:", pessoaJuridica.cnpj, 
                                "Rendimento:", pessoaJuridica.rendimento,
                                "Logradouro:", enderecoPessoaJuridica.logradouro,
                                "Número:", enderecoPessoaJuridica.logradouro
                            )
                    else:
                        print("Lista vazia")
                elif opcao_Pj == 0:
                    print("Retornando ao menu")
                    break
                else:
                    print("Opçao invalida")
                    break
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()