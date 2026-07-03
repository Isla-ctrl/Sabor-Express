# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])

# Já as tuplas são apropriadas quando se deseja garantir que os elementos não sejam alterados após a criação. Isso é útil para dados que devem permanecer constantes ao longo do tempo. Como as tuplas são imutáveis, elas podem ter um desempenho ligeiramente melhor em operações de leitura e acesso a elementos.