import streamlit as st
from PIL import Image

grafico1 = Image.open(r'grafico1.png')
grafico2 = Image.open(r'grafico2.png')
grafico3 = Image.open(r'grafico3.png')
grafico4 = Image.open(r'grafico4.png')
grafico5 = Image.open(r'grafico5.png')
grafico6 = Image.open(r'grafico6.png')
grafico7 = Image.open(r'grafico7.png')
grafico8 = Image.open(r'grafico8.png')
grafico9 = Image.open(r'grafico9.png')
grafico10 = Image.open(r'grafico10.png')
grafico11 = Image.open(r'grafico11.png')
grafico12 = Image.open(r'grafico12.png')
grafico13 = Image.open(r'grafico13.png')
grafico14 = Image.open(r'grafico14.png')
grafico15 = Image.open(r'grafico15.png')
international_trade = Image.open(r'international_trade.png')
main_wine_exporters = Image.open(r'main_wine_exporters.png')
main_wine_exporters2 = Image.open(r'main_wine_exporters2.png')
market_index = Image.open(r'market_index.png')
wine_consumption = Image.open(r'wine_consumption.png')
wine_consumption2 = Image.open(r'wine_consumption2.png')
wine_consumption3 = Image.open(r'wine_consumption3.png')
wine_production = Image.open(r'wine_production.png')



# CONFIGURA A TELA PARA TIPO WIDE COM O INTUITO DE AMPLIAR AS TABELAS E GRÁFICOS
st.set_page_config(layout='wide')

st.title("- Apresentação da empresa")
st.header("A vinícola Vineyard dreams, sediada em Bento Gonçalves, no estado do Rio Grande do Sul foi criada em 1987 por Antonio Garibaldi com o intuito de pruduzir e comercializar vinhos de diversas qualidades para o comércio local. Devido a grande aceitação dos produtos a empresa se expandiu, primeiramente para outras cidades e depois para outros estados do Brasil. A partir de 1999 a empresa começou sua atuação no comércio exterior e hoje atende países de diversas partes do mundo.")

st.title("- Reunião coma diretoria e objetivos traçados")
st.header("No dia  1 de abril de 2024, o atual presidente da vinícola, sr. Astolfo Garibaldi solicitou uma reunião de emergencia juntamente com os demais acionistas e diretores. Segundo o presidente, desde 2020 a Vinicola Garibaldi vem apresentando uma constante queda nas receitas e isso vem afetando fortemente o resultado financeiro da companhia. O diretor financeiro, sr. Roberto Soares acrescentou que a alta do dolar e consequentemente a inflação vem pressionando os custos operacionais. Portanto, aumentar a exportação é crucial para a sobrevivência da vinícola. Além disso, como há limitados recursos financeiros, o diretor de Marketing, sr. Felipe Kothler ressaltou a necessidade de concentrar esforços em determinados países/regiões. ")

st.header('Após intensas discussões foi marcada uma nova reunião em 28/05/2024 e ficou definido que a equipe de analise de dados, liderada pela diretora  Sra. Laura Antonieta precisaria apresentar os seguintes dados: ')
st.header('1 - Faça um panorama do comércio mundial de vinhos')
st.header('2 - Faça uma análise das exportações de vinhos do Rio Grande do sul')
st.header('3 - Quais as prospecções futuras e possíveis ações para uma melhoria nas exportações?')

st.title("- Apresentação da equipe de Analistas de Dados")
st.header('Após diversas análise e pesquisas, concluimos nosso estudo conforme solicitação da diretoria da vinicola Vineyard. Esse estudo se subdivide em 3 partes: 1 - Panorama do mercado mundial de vinhos. 2 - Análise de exportações de vinhos do Rio Grande do sul, que representa mais de 90% dos vinhos nacionais. 3 - Conclusão')

st.title("1 - Panorama do mercado mundial de vinhos")
st.header('No site da International Organization of Vine and Wine "www.oiv.int" encontramos uma pesquisa feita por Pau Roca, Diretor geral da OIV, publicada em 20 de abril de 2023, no qual extraimos informações que utilizamos como base para as informações seguintes. ')

st.title('-- Produção de vinho')
st.image(wine_production, width=1200)
st.header('Considerando esse gráfico, observamos que apenas 3 países (Itália, França e Espanha) concentram mais de 50% da produção mundial de vinhos. Países próximos do Brasil, como Argentina e Chile se destacam como grandes produtores se enquadrando no top 8, que concentram 78% da produção. ')

st.title('-- Consumo de vinho')
st.image(wine_consumption, width=1200)
st.header('Em se tratando de consumo, observamos uma tendencia de queda no consumo mundial desde 2018, que segundo esse estudo se deve em parte pela queda no consumo Chinês. Após uma pequena retomada em 2020 devido a pandemia da Covid-19 no qual favoreceu esse mercado, voltou a cair em 2022 devido a inflação mundial causada por crise energetica e falta de materia prima. Isso pressionou o poder de compra dos consumidores causando a queda no consumo.')

st.image(wine_consumption2,  width=1200)
st.header('Nesse gráfico observamos os países que mais consomem vinhos no mundo, se destaca o fato de 5 países (EUA, França, Italia, Alemanha e Reino Unido) serem responsáveis por 50% do consumo mundial.')

st.image(wine_consumption3, width=1200)
st.header('Importante analisar essa comparação dos países que mais consomem vinho com o consumo per capta, pois esse último ressalta de forma mais real a tendência da população em consumir o produto.')

st.title('-- Comercio internacional')
st.image(international_trade, width=1200)
st.header('Comparando esses 2 graficos, podemos observar no primeiro uma estagnação na exportação por volume, porém, devido a elevação do preço médio vendido, no segundo gráfico a tendencia já é de crescimento no comércio mundial.')

st.image(main_wine_exporters, width=1200)
st.header('Nesses gráficos identificamos os principais exportadores e consequentemente grandes concorrentes do Brasil no comercio mundial de vinhos, tanto em volume, quanto em valores(EUROS). Um destaque interessante é a expressiva participação do Chile e da Argentina no comércio mundial. Uma vez que ambos estão localizados relativamente próximos do Brasil.')

st.image(main_wine_exporters2, width=1200)
st.header('Esses gráficos são muito importantes pois representam os grandes importadores mundiais, por volume e valor(EURO) respectivamente. Destacam-se com certa relevancia: EUA, Alemanha e Reino Unido como os maiores importadores. Vale ressaltar que os EUA, além de serem identificados como o maior importador em volume e em valor, apresentam boas taxa de crescimento. Um mercado que não pode ser ignorado!')

st.image(market_index, width=1200)
st.header('Por último, mas não menos importante, a representação gráfica do percentual do consumo de vinhos que são importados. Nesse caso, apesar de uma queda entre 2021/2022, vemos uma tendecia de crescimento mundial, que em 2022 demonstra que 46% do vinho consumido no mundo foram importados. Dado que obviamente favorece quem está visando a exportação.')

st.title('2 - Análise de exportações de vinhos do Rio Grande do sul')
st.header('Para analisar dados referente a exportação de vinhos no Brasil, encontramos através do site da EMBRAPA "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01" esses dados que são provenientes do estado do Rio Grande do Sul, que representa mais de 90% da produção nacional de produtos da vitivinicultura.')

st.title('-- Evolução nas exportações de vinho do Brasil nos últimos 15 anos')
st.image(grafico1,  width=1200)
st.header('Considerando esse primeiro gráfico, foi apurado o montante total de exportações, em Valor(Dolar) x Quantidade(litros). Porém nos chamou bastante atenção os anos 2009 e 2013, pois as linhas aparentemente fujiram do padrão. Resolvemos averiguar essa questão.')

st.title('-- Análise gráfica considerando a Rússia como outlier em 2009 e 2013')

c1, c2 = st.columns(2)

with c1:
    st.image(grafico2,  width=1200)
with c2:
    st.image(grafico3, width=1200)
st.header('Baseado nesses 2 graficos (valor e litros) que consideram apenas os 5 paíes de maior exportação observa-se a discrepancia dos valores da Russia em 2009 (grafico de quantidade) e  2013 (grafico de valores). Sendo que após 2013 a Russia não mais se descata dos demais. Após uma pesquisa na internet mais detalhada não foi encontrado informações relevantes o que nos fez descartar a Russia da análise desses dados a principio para que não "polua" os gráficos apresentados.') 

st.title('-- Evolução nas exportações de vinho do Brasil desconsiderando a Rússia')
st.image(grafico4, width=1200)
st.header('Evolução das exportações desconsiderando a Rússia ao longo dos 15 anos, observa-se uma dinâmica mais "natural" no gráfico de linhas após esse ajuste. Um destaque para esse gráfico é o forte crescimento nas exportações de 2015 a 2021 apresentando um desquecimento nos ultimos 2 anos em se tratando de volume.') 

st.title('- Análise Cambial')

st.header('Considerando o fato das exportações estarem cotadas em dolar mas a empresa se encontrar no Brasil, resolvemos fazer uma análise em reais, considerando a evolução cambial ao longo desses 15 anos. ') 

st.image(grafico7, width=1200)

st.header('Observa-se nesse gráfico uma situação bastante favoravel para exportações brasileiras devido a constante desvalorização do real ao longo desses anos, com o dolar rondando atualmente entre 5 e 5.50. ') 

st.title('-- Evolução nas exportações de vinho do Brasil Reais x Dolar x Litros')

st.image(grafico8, width=1200)

st.header('Fazendo a conversão das exportações em reais, fica bastante nítido nesse gráfico o quão favorável está sendo a alta do dolar para a exportação das vinícolas. Ressaltando a importância em explorar o mercado externo.') 

st.title('-- 20 maiores importadores em U$ e Litros')

c1, c2 = st.columns(2)

with c1:
    st.image(grafico5,  width=900)
with c2:
    st.image(grafico6, width=900)

st.header('Analisando bem esses dois gráficos, ordenados de acordo com os 20 maiores importadores do Brasil. O primeiro referente ao montante total exportado por países nos ultimos 15 anos em dolar e o segundo em volume/litros, podemos extrair insights bastante interessantes: 1 - Destaque para o Paraguai nas expotações considerando os 2 gráficos, com volume muito superior ao segundo colocado. 2 - Os Estados Unido, Reino Unido e Alemanha, corroborando com nosso estudo referente ao panorama do mercado mundial, considerando países que mais consomem vinho no mundo e os maiores importadores. 3 - A Espanha, que apesar de ser um dos principais produtores e exportadores se encontra entre os maiores importadores de vinho brasileiro. 4 - Diversos países do continente americano, além do Paraguai e EUA: Uruguai, Canadá, Bolívia, Curaçao, Cuba e Venezuela.  ') 

st.title('-- Exportação nos ultimos 5 anos e 2023')

c1, c2 = st.columns(2)

with c1:
    st.image(grafico9, width=900)
with c2:
    st.image(grafico10, width=900)

st.header('Para efeito comparativo, resolvemos fazer uma análise em um espaço de tempo mais curto, incluindo a Rússia novamente devido ao fato de estar em datas fora da que consideramos como outliers. Ao analizar os países nos ultimos 5 anos e isoladamente do ultimo ano desse estudo (2023) observamos que o Paraguai continua como nosso grande comprador. Países como Estados Unidos, China e Reino Unido também continuam como grandes importadores. Chama a atenção o Haiti e Uruguai, que passaram a figurar no top 5 do gráfico. ') 

st.title('-- Crescimento e declínio nas exportações nos ultimos 5 anos')


st.image(grafico11, width=1200)
st.header('Nesse gráfico de barras foi feita uma análise da taxa crescimento das exportações por países no últimos 5 anos. podemos destacar, além do forte crescimento da Turquia, a dominancia de países da América latina. E serve como alerta a queda dessas taxas para os EUA, China e reino Unido, que são grandes mercados consumidores e importadores.') 

st.title('-- Valor em dolar por litro e reais por litro ao longo de 15 anos')

c1, c2 = st.columns(2)

with c1:
    st.image(grafico12, width=850)
with c2:
    st.image(grafico13, width=850)

st.header('Esses dois graficos representam a divisão do valor exportado pelo volume/litros. Extraindo o valor médio por litro a cada ano.   No primeiro grafico, o calculo foi feito em Dolar e no segundo em reais. Observa-se no primeiro a tendencia de queda nos valores a partir de 2014, provavelmente devido a desvalorização do Real as vinicolas reduziram seus preços para se tornarem mais competitivas no mercado internacional. E mesmo assim, quando analisamos o segundo gráfico em reais, observamos uma tendencia de preços com valores acima da média. ') 

st.title('-- Maiores e menores importadores por valor agregado')

c1, c2 = st.columns(2)

with c1:
    st.image(grafico14, width=850)
with c2:
    st.image(grafico15, width=850)

st.header('Essa análise representa 2 extremos. O grafico 1 representa os 20 países com maior valor agregado, ou seja, maior valor em dolar por litro vendido. O segundo representa o oposto, os 20 países com menor valor. Vale ressaltar que para chegar nesses valores selecionamos países com dados em pelo menos 4 anos e preferimos utilizar a mediana com a finalidade de descartar outliers. Importante observar essa divergncia no sentindo de raciocionar onde o MIX de produtos da Vinícola Vineyard se encaixa melhor, uma vez que países Europeus representam um grande mercado consumidor mas tem forte tendencia por qualidade considerando produtos de alto valor agregado. Já no extremo oposto, produtos mais baratos com maior custo benefício considerando o historico médio U$ 2.10/litro nos ultimos 15 anos.') 


st.title('3 - Conclusão')
st.header("Após profunda análise dos dados coletados, a equipe chegou a uma lista de países com grande pontecial exportador. Muito importante deixar claro, antes das explicações a seguir que cada país tem sua peculiaridade. A américa latina e Estado Unidos demonstraram grande tendencia de consumo de vinhos mais baratos. Já os países Europeus e o Canadá já tendem a importar vinhos mais caros. Portanto esse estudo dá um norte apresentando essas oportunidades, a partir disso cabe ao departamento de marketing identificar dentro do mix de produtos da Vinicola Vineyard quais produtos se adequariam melhor dentro de cada um desses países analisados.")
st.header("1 - O comércio internacional de vinhos é enorme, mesmo com grandes e tradicionais produtores em outros países, há grandes oportunidades para vinhos brasileiros.")
st.header("2 - A atual cotação do dolar está beneficiando muito as exportadoras brasileiras. E segundo previsão do banco central do Brasil(Fonte: site do BACEN), a cotação continuará em torno de R$5,05 até 2025.")
st.header("3 - Para quais países exportar? ")

st.header(" * Considerando o volume exportado e o crescimento nas exportações nos últimos 5 anos observamos grandes oportunidades na América Latina. Primeiramente vale destacar os países do Mercosul: O Paraguai por estar isoladamente no topo do país que mais importa do Brasil, o Uruguai, pela análise feita nos ultimos 5 anos apresentante forte crescimento. Também podemos considerar a Argentina, por mais que não estaja na lista de nossos maiores compradores vem apresentando um crescimento interessante nos últimos anos e são um grande mercado consumidor. Além disso a esperada retomada economica com o novo governo pode favorecer o ramo de vinhos. Esses 3 países citados ainda tem a vantagem de estarem todos bem próximos do Rio Grande do Sul, facilitando a questão logistica.")
st.header(" * Outros 2 países latinos que merecem atenção especial são Cuba e Venezuela, que apresentaram bom volume de vendas figurando no top 20. Vale destacar que o comércio com esses países podem ser favorecidos devido a boa relação com o atual governo brasileiro. ")

st.header(" * Demais países da América latina como Haiti, Bolívia, Peru, Guiana e Curaçau também merecem atenção devido ao dados apresentados de volume vendidos e crescimento nos últimos anos. ")

st.header(" * Na América do norte temos os estados Unidos e o Canadá. Os EUA é um país que vale destaque. O maior consumidor de vinho e o maior importador do mundo, além de ser o segundo país que mais compra do Brasil. O canadá tembém figura entre os importadores mais relevantes, além de apresentar crescimento nesses dados nos ultimos 5 anos e comprar produtos de alto valor agregado. ")

st.header(" * Na Europa temos Reino Unido, Espanha, Países baixos, Alemanha, Bélgica, Suiça, França, Portugal e Polonia. Todos grandes consumidores e entre os maiores compradores do Brasil. Um ponto de alerta é que o Brasil vem perdendo mercado nesses países nos ultimos anos, que tem foco em produtos de alto valor agregado.")

st.header(" * Por fim, temos os países asiáticos: A China, como nosso terceiro maior comprador do setor e maior parceiro comercial do Brasil e o Japão, que também se destaca como grande comprador. Vale ressaltar que ambos também vem nos ultimos 5 anos reduzindo as importações de vinho do Brasil. Além de Hong Kong, com números expressivos nos últimos 5 anos.")

st.title('Quais os Riscos?')
st.header("Um alerta nesse estudo são os riscos e ameaças que a Vineyard pode enfrentar em se tratando de exportações. Primeiramente a questão cambial: Por mais que a previsão do BACEN é da cotação do dolar em torno de 5,05 até 2025 diversos fatores podem ocorrer nesse tempo que pode 'puxar' o dolar para baixo, desfavorecendo as empresas exportadoras. Outra questão importante é um erro de direcionamento de mercado. Ou seja, a empresa precisa estudar bastante as peculiaridades de cada país escolhido antes de escolher o mix de produtos que irá vender naquele local, um erro de marketing pode ser fatal. E por ultimo, a concorrencia. O mercado é grande mas ao mesmo tempo competitivo, os gestores tem que ficar sempre atento ao que está sendo oferecido no mercado mundial para que a Vineyard posse se sobressair e ter sucesso nas exportações.")



    
         


 



