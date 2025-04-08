 #Coleta de Dados na Wikipedia
 Administrativo
 Este exercício pode ser feito em trios ou quartetos, não sendo possível realizar individual
mente. Apenas um dos integrantes deve submeter os arquivos do trabalho no moodle.
 Data de Entrega: 07/04/2024 (Turma 10)– 09/04/2024 (Turma 30)
 Forma de Entrega: O trabalho deve ser apresentado durante o período de aula. Não haverá
 uma aula de apresentação para este trabalho. O grupo deve marcar com o professor um horá
rio para realizar a apresentação. A apresentação consiste em mostrar o código e o programa
 em funcionamento para o professor. Poderão ser feitas perguntas sobre o funcionamento do
 trabalho para o grupo.
 Além disso, deve ser entregue no moodle:
 • Scripts Python ou Jupyter notebooks com o código que realiza as tarefas solicitadas.
 • Link para um repositório com os dados obtidos via scraping (páginas html) e com os
 dados extraídos (arquivos json)
 • Orientações sobre como executar os scripts (como comentário no código, arquivo README.txt
 ou células de texto em jupyter notebook). Incluir comentários sobre a configuração do
 ambiente de desenvolvimento necessário para rodar os scripts.
 Tarefa 1– Desenvolvendo um crawler
 Escreva um crawler para descobrir e coletar páginas da Wikipedia em Português. Seu pro
grama deve coletar 5.000 páginas de verbetes diferentes da Wikipedia, à partir da página
 inicial: https://pt.wikipedia.org. Não coletar páginas de outros sites e também não deve
 ser coletado páginas internas da Wikipedia que não são verbetes.
 Ocrawler deve funcionar da seguinte maneira:
 1. Obter uma página.
 2. Salvar a página como um arquivo html, chamado <titulo_verbete>.html
 3. Extrair todos os links que se encontram nessa página
 4. Filtrar os links, removendo os que não se referem à verbetes e os verbetes que já foram
 visitados
