import requests
from typing import Optional, List, Dict

class APITesouro:
    """
    Classe para interagir com a API de leilões do Tesouro Nacional.

    Esta classe fornece métodos para acessar os diferentes endpoints da API pública 
    para consulta dos dados de leilões de títulos públicos.

    Atributos:
        base_url (str): URL base da API.
    
    Métodos:
        __init__: Inicializa a classe com a URL base.
        get_benchmarks: Retorna a lista de benchmarks de referência dos leilões.
    """
    
    def __init__(self):
        self.base_url = 'https://apiapex.tesouro.gov.br/aria'
    
    def get_benchmarks(self, incluir_historico: Optional[str] = 'N') -> List[Dict]:
        """
        Retorna a lista de benchmarks de referência dos leilões do Tesouro Nacional.

        Por padrão, o endpoint retorna apenas os benchmarks atualmente ofertados 
        pelo Tesouro Nacional (on-the-run). Alternativamente, o endpoint pode retornar 
        todos os benchmarks cadastrados (on-the run e off-the-run) informando o parâmetro 
        incluir_historico com o valor "S".

        Parâmetros:
            incluir_historico (str): Identificador de Histórico. Parâmetro Opcional. 
                                     Valor Padrão: "N". Determina se a lista de benchmarks 
                                     retornará apenas os benchmarks em uso (valor: "N") ou 
                                     todo o histórico de benchmarks cadastrados (valor: "S").

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre os benchmarks.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/benchmarks'
        params = {'incluir_historico': incluir_historico}
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_comunicados(self) -> List[Dict]:
        """
        Retorna a lista de comunicados publicados pela Secretaria do Tesouro Nacional
        relacionados à gestão da Dívida Pública Federal.

        O retorno inclui o título do comunicado e o link para download.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre os comunicados.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/comunicados'
        response = requests.get(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_portarias(self, data_leilao: Optional[str] = None) -> List[Dict]:
        """
        Retorna as informações das quantidades ofertadas no dia por benchmark.

        Utilizando o parâmetro opcional "data_leilao", é possível consultar as ofertas passadas. 
        Os dados da oferta do dia estarão disponíveis de forma simultânea à divulgação da portaria 
        no sítio do Tesouro Nacional, tipicamente a partir das 10h30 do dia do leilão.

        Parâmetros:
            data_leilao (str): Data de referência no formato 'DD/MM/YYYY'. Caso não informado, 
                            retornará as portarias do dia.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre as portarias.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/portarias'
        params = {'data_leilao': data_leilao} if data_leilao else {}
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_resultados(self, ano: Optional[int] = None, anoinicial: Optional[int] = 2015, 
                    dataleilao: Optional[str] = None, titulo: Optional[str] = None) -> List[Dict]:
        """
        Retorna as informações de data de liquidação, oferta, quantidade aceita, taxa de corte e volume emitido 
        para o Banco Central do Brasil a partir de uma data desejada, ano ou papel específico.

        Todos os parâmetros são opcionais e podem ser livremente combinados.

        Parâmetros:
            ano (int): Ano desejado. Retorna todos os resultados para o ano informado.
            anoinicial (int): Ano inicial desejado. Retorna todos os resultados a partir do ano informado. 
                            Valor padrão: 2015.
            dataleilao (str): Data desejada no formato 'DD/MM/YYYY'. Retorna todos os resultados para a data informada.
            titulo (str): Título desejado. Filtra os resultados retornados apenas para o título informado.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre os resultados dos leilões.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/resultados'
        params = {
            'ano': ano,
            'anoinicial': anoinicial,
            'dataleilao': dataleilao,
            'titulo': titulo
        }
        # Remove parâmetros que são None para não enviar ao servidor
        params = {k: v for k, v in params.items() if v is not None}
        
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_dealers(self, ano: Optional[int] = None, cnpj: Optional[str] = None, 
                    dealer: Optional[str] = None) -> List[Dict]:
        """
        Retorna a relação das instituições financeiras habilitadas como dealers na Secretaria do Tesouro Nacional.

        Parâmetros:
            ano (int): Ano do período desejado. Parâmetro opcional.
            cnpj (str): CNPJ da instituição financeira. Parâmetro opcional.
            dealer (str): Nome (ou parte do nome) da instituição financeira. Parâmetro opcional.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre os dealers.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/dealers'
        params = {
            'ANO': ano,
            'CNPJ': cnpj,
            'DEALER': dealer
        }
        # Remove parâmetros que são None para não enviar ao servidor
        params = {k: v for k, v in params.items() if v is not None}
        
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_calendario(self) -> List[Dict]:
        """
        Retorna o calendário com a previsão de oferta de títulos públicos de acordo com o calendário
        divulgado pela Secretaria do Tesouro Nacional.

        O retorno inclui a data de realização do leilão, o título ofertado, a data de vencimento, 
        a referência do título e o tipo de oferta.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre o calendário de leilões.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/calendario'
        response = requests.get(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_homologacao(self, data_leilao: Optional[str] = None) -> List[Dict]:
        """
        Retorna as informações sobre a homologação dos leilões de títulos públicos.

        Utilizando o parâmetro opcional "data_leilao", é possível consultar as homologações 
        para uma data específica. Caso não informado, retornará as homologações do dia.

        Parâmetros:
            data_leilao (str): Data de referência no formato 'DD/MM/YYYY'. 
                            Caso não informado, retornará as homologações do dia.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre a homologação dos leilões.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/homologacao'
        params = {'data_leilao': data_leilao} if data_leilao else {}
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_troca(self, data_leilao: Optional[str] = None) -> List[Dict]:
        """
        Retorna as informações sobre os leilões de troca de títulos públicos.

        Utilizando o parâmetro opcional "data_leilao", é possível consultar as informações 
        dos leilões de troca para uma data específica. Caso não informado, retornará as 
        informações dos leilões de troca do dia.

        Parâmetros:
            data_leilao (str): Data do leilão desejado no formato 'DD/MM/YYYY'. 
                            Caso não informado, retornará as informações dos leilões 
                            de troca do dia.

        Retorno:
            List[Dict]: Lista de dicionários com informações sobre os leilões de troca.
        """
        endpoint = f'{self.base_url}/v1/api-leiloes-pub/custom/troca'
        params = {'DATA_LEILAO': data_leilao} if data_leilao else {}
        response = requests.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
