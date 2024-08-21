from datetime import date, datetime
from pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    while True:
        lista_PessoasFisicas : PessoaFisica = []
        lista_PessoasJuridicas = []
        opcao = int(input("Escolha opçao: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair "))

        if opcao == 1:
            while True:
                opcao_Pf = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Fisicas / 3 - Remover cpf / 4 - Atualizar / 0 - Voltar menu anterior "))

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
                                "Número:", enderecoPessoaFisica.numero
                            )
                    else:
                        print("Lista vazia")
                elif opcao_Pf == 3:
                    cpf_Remover = input("Digite o cpf da pessoa que deseja remover")
                    pessoa_encontrada = False

                    for pessoa_pf in lista_PessoasFisicas:
                        if pessoa_pf.cpf == cpf_Remover:
                            lista_PessoasFisicas.remove(pessoa_pf)
                            pessoa_encontrada = True
                            print("Pessoa removida")
                            break
                            
                        if not pessoa_encontrada:
                            print("Pessoa nao encontrada")
                elif opcao_Pf == 4:
                    if(len(lista_PessoasFisicas) == 0):
                        print("\nLista está vazia, volte ao menu para cadastrar\n")
                        continue
                    
                    pessoa_encontrada = False
                    cpf_pessoa = input("Digite o cpf da pessoa que deseja atualizar ")
                    
                    
                    for pessoa_pf in lista_PessoasFisicas:
                        if pessoa_pf.cpf == cpf_pessoa:
                            item = int(input("Digite qual item deseja atualizar: 1 - Nome, 2 - Rendimento, 3 - CPF, 4 - Endereco "))
                            if item != 4:
                                new_value = input("Digite o novo valor ")

                            match item:
                                case 1:
                                    pessoa_pf.nome = new_value
                                case 2:
                                    pessoa_pf.rendimento = new_value
                                case 3:
                                    pessoa_pf.cpf = new_value
                                case 4:
                                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                                    pessoa_pf.endereco.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                                    pessoa_pf.endereco.logradouro = input("Digite o logradouro da pessoa fisica: ")
                                    pessoa_pf.endereco.numero = input("Digite o numero da pessoa fisica: ")
                                case _:
                                    print("\nSeleçao Invalida\n")
                                    break

                            pessoa_encontrada = True
                            print("\nItem atualizado\n")
                            break

                    if not pessoa_encontrada:
                        print("\nPessoa nao encontrada\n")

                elif opcao_Pf == 0:
                    print("Retornando ao menu")
                    break
                else:
                    print("Opçao invalida")
                    break
        elif opcao == 2:
            while True:
                opcao_Pj = int(input("Escolha uma opçao: 1 - Cadastrar / 2 - Listar Pessoas Juridica / 3 - Remover / 4 - Atualizar / 0 - Voltar menu anterior "))

                if opcao_Pj == 1:
                    novaPJ = PessoaJuridica()
                    novo_endereco_pj = Endereco()

                    novaPJ.nome = str(input("Digite o nome da pessoa juridica: "))
                    novaPJ.cnpj = str(input("Digite o cnpj da pessoa juridica: "))
                    novaPJ.rendimento = float(input("Digite o rendimento da pessoa juridica: "))

                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                    novo_endereco_pj.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                    novo_endereco_pj.logradouro = input("Digite o logradouro da pessoa fisica: ")
                    novo_endereco_pj.numero = input("Digite o numero da pessoa fisica: ")
                    
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
                                "Imposto a ser pago:", pessoaJuridica.calcular_imposto(pessoaJuridica.rendimento),
                                "Logradouro:", enderecoPessoaJuridica.logradouro,
                                "Número:", enderecoPessoaJuridica.numero
                            )
                    else:
                        print("\nLista vazia\n")
                elif opcao_Pj == 3:
                    cnpj_Remover = input("Digite o cnpj que deseja remover")
                    pessoa_encontrada = False

                    for pessoa_Pj in lista_PessoasJuridicas:
                        if pessoa_Pj.cnpj == cnpj_Remover:
                            lista_PessoasJuridicas.remove(pessoa_Pj)
                            pessoa_encontrada = True
                            print("Pessoa removida")
                            break
                            
                        if not pessoa_encontrada:
                            print("\nPessoa nao encontrada\n")
                elif opcao_Pj == 4:
                    if(len(lista_PessoasJuridicas) == 0):
                        print("\nLista está vazia, volte ao menu para cadastrar\n")
                        continue
                    
                    pessoa_encontrada = False
                    cnpj_pessoa = input("Digite o cnpj da pessoa que deseja atualizar ")
                    
                    for pessoa_pj in lista_PessoasJuridicas:
                        if pessoa_pj.cnpj == cnpj_pessoa:
                            item = int(input("Digite qual item deseja atualizar: 1 - Nome, 2 - Rendimento, 3 - CNPJ, 4 - Endereco "))
                            if item != 4:
                                new_value = input("Digite o novo valor ")

                            match item:
                                case 1:
                                    pessoa_pj.nome = new_value
                                case 2:
                                    pessoa_pj.rendimento = new_value
                                case 3:
                                    pessoa_pj.cnpj = new_value
                                case 4:
                                    endereco_Comercial = input("Este endereço é comercial? S/N: ")
                                    pessoa_pj.endereco.endereco_Comercial = endereco_Comercial.strip().upper() == 'S'
                                    pessoa_pj.endereco.logradouro = input("Digite o logradouro da pessoa juridica: ")
                                    pessoa_pj.endereco.numero = input("Digite o numero da pessoa juridica: ")
                                case _:
                                    print("\nSeleçao Invalida\n")
                                    break

                            pessoa_encontrada = True
                            print("\nItem atualizado\n")
                            break

                    if not pessoa_encontrada:
                        print("\nPessoa nao encontrada\n")

                elif opcao_Pj == 0:
                    print("\nRetornando ao menu\n")
                    break
                else:
                    print("\nOpçao invalida\n")
                    break
        elif opcao == 0:
            print("\nObrigado por utilizar o nome sistema!\n")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()