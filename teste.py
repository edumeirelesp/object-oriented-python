from atualizador_de_contas import AtualizadorDeContas
from cliente import Cliente
from conta import Conta
from conta_corrente import ContaCorrente
from conta_investimento import ContaInvestimento
from conta_poupanca import ContaPoupanca
from contas import Contas
from controle_bonificacoes import ControleDeBonificacoes
from funcionario import Funcionario
from gerente import Gerente
from tkinter import *

from manipulador_tributaveis import ManipuladorDeTributaveis
from seguro_de_vida import SeguroDeVida
from tributavel import Tributavel

if __name__ == '__main__':
    cliente1 = Cliente("Eduardo", "Meireles", 9887887)
    cliente2 = Cliente("Manoel", "Souza", 767676)
    cliente3 = Cliente("José", "Assis", 776556)

    '''cc = ContaCorrente('121.1', cliente1, 234, 2000)
    cp = ContaPoupanca('122.2', cliente2, 540, 1000)

    adc = AtualizadorDeContas(0.01)

    adc.roda(cc)

    adc.roda(cp)
    # cliente1 = Cliente("Eduardo", "Meireles", 9887887)
    # conta1 = Conta(4344, cliente1, 324.43, 1000)

    ge = Gerente("José", "222222222-22", 5000.0, '1234', 0)
    fun = Funcionario('João', '111111111-11', 2000.0)
    print(f"bonificação de gerente:{ge.get_bonificacao()}\nbonificação de funcionarios:{fun.get_bonificacao()}")

    controle = ControleDeBonificacoes()

    controle.registrar(fun)
    controle.registrar(ge)

    print(f'Total:{controle.total_bonificacoes}')

    contaIn = ContaInvestimento('123-6', cliente1, 767, 1000)

    contaIn.deposita(1000.0)

    contaIn.atualiza(0.1)

    #print(contaIn.saldo())
    help(Label)'''

    def dados_cliente(entrada):  # ATTETION TYPEERROR -> gabiarra
        if entrada == "cliente1":
            return cliente1
        elif entrada == "cliente2":
            return cliente2
        else:
            return cliente3


    import csv

    contas = Contas()
    arquivo = open('contas.txt', 'r')
    leitor = csv.reader(arquivo)
    for linha in leitor:
        valor = float(linha[2])
        limite = float(linha[3])
        conta = ContaCorrente(linha[0], dados_cliente(linha[1]), valor, limite)
        contas.append(conta)
    arquivo.close()

    print("Saldo atualizado - Imposto")
    for i in contas:
        i.atualiza(0.01)
        print(f'   {i.saldo():.2f}          {i.get_valor_imposto():.2f}')

    '''cc2 = ContaCorrente('123-4', cliente2, 564, 1000.0)
    cp1 = ContaPoupanca('123-6', cliente3, 562, 1000.0)
    ci = ContaInvestimento('143-7', cliente3, 552, 1000.0)
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')
    Tributavel.register(ContaInvestimento)
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    lista_tributaveis = []
    #lista_tributaveis.append(cp1)
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    lista_tributaveis.append(ci)
    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)
    try:
        cc2.saca(-200)
    except ValueError as e:
        print(f"Error no sistema: {e}")

    print()'''
