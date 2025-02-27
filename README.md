# Otimização do Calendário da Temporada de 2025 da Fórmula 1

Este projeto foi criado por um fã de automobilismo para otimizar o calendário de corridas da Fórmula 1, calendário este que é alvo de inúmeras críticas, tanto pela suposta "desorganização", quanto pela poluição gerada pelas viagens. O objetivo era melhorar o planejamento de viagem dos pilotos, equipes e até dos fãs, minimizando a distância percorrida entre os GPs (Grand Prix). Para isso, tentei aplicar alguns algoritmos clássicos de otimização: **Dijkstra**, **TSP (Problema do Caixeiro Viajante)** e o cálculo de distâncias usando a fórmula **Haversine**. Como fã, queria que as corridas acontecessem de forma que os GPs mais próximos estivessem no calendário de forma eficiente, mas também levando em conta a realidade de viagens de avião e fusos horários.

## Como Funciona 

O processo é dividido em duas etapas principais:

1. **Otimização do Calendário**: A ideia é criar uma rota que minimize a distância entre as corridas. Para isso, usei o algoritmo de **Dijkstra** para encontrar o caminho mais curto entre os GPs. No entanto, como o TSP (Problema do Caixeiro Viajante) tenta encontrar a melhor ordem de visita entre todos os pontos, ele acaba sendo bem mais complexo (**O(n!)**) e difícil de resolver para um grande número de GPs.

2. **Cálculo de Distâncias**: Em vez de usar apenas distâncias simples entre pontos geográficos, também apliquei a **fórmula de Haversine**, que leva em consideração a curvatura da Terra para calcular distâncias mais realistas entre as cidades. Isso ajuda a ter uma ideia mais precisa do quanto os pilotos e equipes viajariam de um GP para outro.

## Algoritmos Usados 

### Dijkstra
A primeira tentativa foi usar o **algoritmo de Dijkstra**, que é ótimo para encontrar o caminho mais curto em grafos. A ideia era tratar cada GP como um nó e as distâncias entre eles como arestas. A vantagem do Dijkstra é que ele sempre encontra o caminho mais curto de um ponto a outro, mas, como cada GP tem um custo (distância para o próximo GP), a coisa se complica quando temos que tratar de múltiplos pontos e otimizar tudo ao mesmo tempo. Mesmo assim, ele deu uma boa base para começar a trabalhar na otimização.

### TSP - Problema do Caixeiro Viajante
O problema é simples de entender: a ideia é encontrar a menor rota possível que passe por todos os pontos uma única vez e retorne ao ponto inicial. Eu até tentei resolver isso aqui, mas o TSP é pesado para muitas cidades. Para você ter uma ideia, o número de combinações possíveis cresce rapidamente com o número de cidades, então a solução exata se torna impraticável quando o número de GPs é grande demais. Tentei rodar esse algoritmo, mas ele ficou super lento, então pensei em algo mais realista usando a combinação de Dijkstra com outras heurísticas.

### Haversine
Para garantir que as distâncias fossem precisas, usei a fórmula de **Haversine**, que calcula a distância entre dois pontos na superfície da Terra levando em consideração a curvatura. Não é a solução mais rápida para calcular distâncias geográficas, mas, para esse projeto, ela foi bem útil para simular viagens reais entre os GPs e entender melhor o problema. A fórmula usa as coordenadas de latitude e longitude para determinar a distância entre dois pontos em linha reta, o que é ótimo para simular viagens de avião.

A versão final do código integra diferentes abordagens para otimizar o calendário de corridas. A estratégia foi começar com a aplicação do **algoritmo de Dijkstra** para calcular as rotas mais curtas entre os GPs. Contudo, como o número de GPs é grande, o código precisava de uma alternativa mais prática para lidar com essa quantidade de dados. 

### Metodologia final

1. **Leitura dos Dados**: Primeiro, o código lê os dados de um arquivo CSV que contém informações sobre cada GP, como nome, localização, latitude, longitude e a distância para o próximo circuito. Os dados são armazenados em um DataFrame do **pandas**.

2. **Construção do Grafo**: O próximo passo foi construir um grafo onde cada GP é representado como um nó, e as distâncias entre eles (calculadas usando a fórmula de Haversine) são as arestas.

3. **Aplicação de Dijkstra**: Usei o algoritmo de **Dijkstra** para calcular as rotas mais curtas entre os GPs, considerando as distâncias reais entre eles. O algoritmo foi implementado para buscar o menor caminho a partir de um GP inicial, mas sem garantir a ordem ótima de todas as corridas (o que seria um problema típico do TSP).

4. **Heurísticas para Otimização do TSP**: Como o TSP é computacionalmente caro, apliquei heurísticas simples para tentar otimizar a ordem dos GPs no calendário. Em vez de calcular a solução exata, usei uma abordagem mais prática que tenta agrupar os GPs mais próximos, buscando minimizar o número de distâncias grandes entre corridas consecutivas.

5. **Resultado**: O código então retorna um calendário otimizado, onde as corridas são organizadas de forma mais eficiente, levando em conta a distância e a viabilidade de viagem entre elas.


### Conclusão 🏁
Esse projeto é um primeiro passo para otimizar o calendário da Fórmula 1, mas a solução real precisaria de muito mais ajustes, incluindo simulações de voo, questões de fuso horário e outras variáveis logísticas. Ainda assim, é um ótimo exercício pra quem quer explorar como otimizar algo que parece simples, mas é bastante complexo na prática!
