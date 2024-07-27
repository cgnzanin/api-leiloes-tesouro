from src.tesouroapi import APITesouro

# Instancia a classe da API
api = APITesouro()

# Exemplo 1: Obtendo benchmarks na segunda-feira da semana passada
benchmarks = api.get_benchmarks()
print("Benchmarks:", benchmarks)

# Exemplo 2: Obtendo comunicados na segunda-feira da semana passada
comunicados = api.get_comunicados()
print("Comunicados:", comunicados)

# Exemplo 3: Obtendo portarias com data específica
portarias = api.get_portarias(data_leilao='16/07/2024')
print("Portarias:", portarias)

# Exemplo 4: Obtendo resultados de leilões com data específica
resultados = api.get_resultados()
print("Resultados:", resultados)

# Exemplo 5: Obtendo dealers
dealers = api.get_dealers()
print("Dealers:", dealers)

# Exemplo 6: Obtendo calendário de leilões
calendario = api.get_calendario()
print("Calendário:", calendario)

# Exemplo 7: Obtendo homologações com data específica
homologacao = api.get_homologacao(data_leilao='16/07/2024')
print("Homologação:", homologacao)

# Exemplo 8: Obtendo trocas com data específica
troca = api.get_troca(data_leilao='16/07/2024')
print("Troca:", troca)
