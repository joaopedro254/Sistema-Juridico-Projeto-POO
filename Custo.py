class Custo:
    def __init__(self, data, descricao, valor):
        self._data = data
        self._descricao = descricao
        self._valor = valor

    @property
    def data(self):
        return self._data
    @property
    def descricao(self):
        return self._descricao
    @property
    def valor(self):
        return self._valor
    @data.setter
    def data(self, newData):
        self._data = newData
    @descricao.setter
    def descricao(self, newDescricao):
        self._descricao = newDescricao
    @valor.setter
    def valor(self, newValor):
        self._valor = newValor

    def __str__(self):
        return f'Data: {self._data}, Descrição: {self._descricao}, Valor: {self._valor}'