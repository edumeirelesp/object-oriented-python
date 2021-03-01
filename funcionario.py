import abc


class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        # return self._salario * 0.10
        pass

    def to_string(self):
        return f"Nome:{self._nome}\nCPF:{self._cpf}\nSalario:{self._salario}"
