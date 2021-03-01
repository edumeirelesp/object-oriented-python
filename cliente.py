class Cliente:
    def __init__(self, nome, sobre_nome, cpf):
        self._nome = nome
        self._sobre_nome = sobre_nome
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_sobre_nome(self):
        return self._sobre_nome

    def set_sobre_nome(self, sobre_nome):
        self._sobre_nome = sobre_nome

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def to_string(self):
        return f"Nome: {self._nome}\nSobre nome: {self._sobre_nome}\nCPF: {self._cpf}"