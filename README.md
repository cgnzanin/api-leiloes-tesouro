
# API de Leilões do Tesouro Nacional

## Estrutura do Diretório
- **`assets/`**: Armazena todos os recursos como bases de dados e outros arquivos.
  - **`raw_data/`**: Contém as bases de dados cruas, não modificadas.
  - **`processed_data/`**: Contém as bases de dados que foram limpas ou processadas.
- **`src/`**: Código-fonte principal do projeto. Contém módulos e pacotes reutilizáveis.
- **`main.py`**: Script Python principal que executa a análise de dados e gera visualizações.

## Descrição do Projeto
Este projeto é uma API pública para consulta de dados referentes aos leilões de títulos públicos da Dívida Pública Mobiliária Federal interna (DPMFi). A API permite acessar informações sobre benchmarks, comunicados, portarias, resultados de leilões, dealers, calendário de leilões e homologações.

## Endpoints Implementados
- **Benchmarks**: Retorna a lista de benchmarks de referência dos leilões do Tesouro Nacional.
- **Comunicados**: Lista de comunicados publicados pela Secretaria do Tesouro Nacional.
- **Portarias**: Informações das quantidades ofertadas no dia por benchmark.
- **Resultados**: Informações sobre data de liquidação, oferta, quantidade aceita, taxa de corte e volume emitido.
- **Dealers**: Relação das instituições financeiras habilitadas como dealers.
- **Calendário**: Previsão de oferta de títulos públicos.
- **Homologação**: Informações sobre a homologação dos leilões.
- **Troca**: Informações sobre leilões de troca de títulos.

## Como Usar
1. Clone o repositório para sua máquina local.
2. Instale as dependências necessárias.
3. Use os métodos da classe `APITesouro` para interagir com a API.

## Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias ou correções.