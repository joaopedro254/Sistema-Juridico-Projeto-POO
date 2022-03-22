class Audiencia:
    def __init__(self, data, recomendacao, duracao):
        self._data_da_audiencia = data
        self._recomendacao = recomendacao
        self._duracao = duracao
    
    @property
    def data_da_audiencia(self):
        return self._data_da_audiencia

    @data_da_audiencia.setter
    def data_da_audiencia(self, nova_data_de_audiencia):
        self._data_da_audiencia = nova_data_de_audiencia

    @property
    def recomendacao(self):
        return self._recomendacao

    @recomendacao.setter
    def recomendacao(self, nova_recomendacao):
        self._recomendacao = nova_recomendacao

    @property
    def duracao(self):
        return self._duracao
    
    @duracao.setter
    def duracao(self, nova_duracao):
        self._duracao = nova_duracao

    def __str__(self):
        return "data: {}, recomendação: {}, duração: {}".format(self._data_da_audiencia, self._recomendacao, self._duracao)