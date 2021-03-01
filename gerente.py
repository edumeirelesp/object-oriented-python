from funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qts_gerenciados):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qts_gerenciados = qts_gerenciados

    def autentica(self, senha):
        if self._senha == senha:
            print('acesso permitido')
            return True

        else:
            print('acesso negado')
            return False

    def get_bonificacao(self):
        return self._salario * 0.15

    def to_string(self):
        return f'~~~~GERENTE~~~~\n{super().to_string()}\nSenha: XXXXXX\nQuantos Gerenciados:{self._qts_gerenciados}'