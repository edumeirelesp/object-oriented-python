class ControleDeBonificacoes:
    def __init__(self, total_bonificacoes = 0):
        self._total_bonificacoes = total_bonificacoes

    def registrar(self, obj):
        try:   # jeito ducktyping
            self._total_bonificacoes += obj.get_bonificacao()
        except AttributeError as e:
            print(f"erro do tipo {e}, porque não implementa o método get_bonificação()")

        '''if hasattr(obj, "get_bonificacao"):    #jeito nao ducktyping
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print( f"instãncia de {self.__class__.__name__} não implementa o método get_bonificação()")'''

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes