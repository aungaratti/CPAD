# Coleta de Dados na Wikipedia

Tarefa 1 – Desenvolvendo um crawler

      Escreva um crawler para descobrir e coletar páginas da Wikipedia em Português. 
    Seu programa deve coletar 5.000 páginas de verbetes diferentes da Wikipedia, à partir da página
    inicial: https://pt.wikipedia.org. Não coletar páginas de outros sites e também não deve 
    ser coletado páginas internas da Wikipedia que não são verbetes.

  O crawler deve funcionar da seguinte maneira:
  
    1. Obter uma página.
    2. Salvar a página como um arquivo html, chamado <titulo_verbete>.html
    3. Extrair todos os links que se encontram nessa página
    4. Filtrar os links, removendo os que não se referem à verbetes e os verbetes que já foram visitados;
    5. Guardar esses links em uma lista
    6. Escolher um link não visitado para ser a próxima página.
    7. Voltar ao passo inicial
    
      As páginas de verbetes coletadas deverão ser salvas como arquivos com a extensão .html.
    Lembre-se de tomar cuidado para não estressar o servidor com requisições em excesso.

 Tarefa 2 – Extraindo informações de Infoboxes

      A segunda tarefa consiste em identificar as páginas que possuem infoboxes, que são usadas
    para resumir as informações de um artigo na Wikipédia. Veja na figura a seguir um exemplo
    de página que contém um infobox (ele está destacado em vermelho na imagem).
    Infoboxes estruturam informações de diversas maneiras, por isso é difícil conseguir extrair
    todos os seus elementos de forma fácil. Portanto, focaremos nossos esforços em extrair apenas
    alguns elementos. 
    
    São eles:

     1. Título: toda infobox possui um título que fica no topo da caixa. No exemplo da figura,
     o título é Alan Turing
     2. Pares chave– valor: esses pares são identificados por uma chave que está associada a
     um único valor. Por exemplo, na figura temos a chave “Nome completo” e o valor “Alan
     Mathison Turing”.
     3. Pares chave– lista: nesse tipo de item, uma chave está associada a uma lista de valores.
     
       Na figura de exemplo são pares de chave–lista os campos: Conhecido(a) por, Alma
     mater, Orientado(a)(s), Instituições e Campos

       Sua tarefa consiste em extrair o conteúdo das infoboxes de todas as páginas que foram 
     extraídas no exercício anterior. Seu programa deve identificar quando uma página possui uma
     infobox, realizar a extração das informações e salvá-las em um arquivo .json cujo nome é o
     título da infobox.
     
       Para fins de teste, será fornecido um conjunto de páginas juntamente com a saída esperada
     para cada uma delas.
