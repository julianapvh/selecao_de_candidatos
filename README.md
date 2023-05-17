# selecao_de_candidatos
Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade de um candidato com uma vaga de acordo com seu resultado nas etapas do processo seletivo.


Neste projeto, utilize-se a função 'busca_candidatos' para encontrar candidatos que atendam aos critérios mínimos de notas em cada uma das categorias solicitadas pela empresa: a entrevista, o teste teórico, o teste prático e a avaliação de soft skills.

A função percorre a lista de candidatos fornece como argumento e adiciona o número do candidato a uma lista chamada 'candidatos_encontrados', caso as notas em todas as categorias atendam aos critérios mínimos. A função retorna a lista 'candidatos_encontrados'.

No entanto, caso o usuário digite notas que não se encaixam com as notas da base de dados, o programa retorna que não foi encontrado nenhum resultado para a sua pesquisa.


README - Programa de Busca de Candidatos

Este programa em Python permite buscar candidatos com base em critérios específicos de notas mínimas em entrevista, teste teórico, teste prático e avaliação de soft skills. Ele fornece uma lista dos candidatos que atendem aos requisitos estabelecidos.

Funcionalidades
O programa oferece as seguintes funcionalidades:

Laço de repetição: O programa possui um laço de repetição while True, o que permite que o programa continue aberto após cada pesquisa, possibilitando ao usuário realizar múltiplas buscas sem precisar reiniciar o programa.

Função de busca de candidatos: A função busca_candidatos recebe uma lista de candidatos e as notas mínimas estabelecidas para a entrevista, teste teórico, teste prático e avaliação de soft skills. Ela percorre a lista de candidatos e retorna uma lista com os nomes dos candidatos que atendem aos requisitos.

Lista de candidatos: O programa já possui uma lista pré-definida de candidatos com suas respectivas notas em cada categoria. Essa lista pode ser modificada para se adequar às necessidades do usuário.

Entrada do usuário: O usuário é solicitado a fornecer as notas mínimas desejadas para a entrevista, teste teórico, teste prático e avaliação de soft skills. Essas informações são inseridas pelo usuário durante a execução do programa.

Exibição dos resultados: O programa exibe os nomes dos candidatos que atendem aos critérios de busca. Se nenhum candidato for encontrado, uma mensagem indicando isso será exibida.

Como usar
Certifique-se de ter o Python instalado em seu computador.

Abra um ambiente de desenvolvimento Python de sua escolha.

Copie o código-fonte fornecido e cole-o em um arquivo Python.

Execute o programa.

Será solicitado que você insira as notas mínimas desejadas para cada categoria (entrevista, teste teórico, teste prático e avaliação de soft skills). Digite os valores solicitados e pressione Enter.

O programa exibirá os nomes dos candidatos que atendem aos critérios estabelecidos. Se nenhum candidato for encontrado, uma mensagem será exibida informando isso.

Após a exibição dos resultados, o programa continuará aberto para que você possa realizar novas buscas. Basta fornecer novas notas mínimas e pressionar Enter para obter os resultados atualizados.

Observações
Certifique-se de que o Python esteja configurado corretamente em seu ambiente de desenvolvimento.

A lista de candidatos fornecida é apenas um exemplo e pode ser modificada de acordo com suas necessidades. Certifique-se de seguir a mesma estrutura ao adicionar ou remover candidatos da lista.

Os resultados são exibidos no terminal ou console do seu ambiente de desenvolvimento Python.

Certifique-se de fornecer notas mínimas válidas e coerentes para cada categoria. Caso contrário, os resultados podem não ser precisos.

Lembre-se de utilizar as boas práticas de programação ao modificar ou estender o código, como a validação de entrada do usuário e o tratamento de erros.

Sinta-se à vontade para personalizar ou adaptar o código de acordo com suas necessidades específicas.

Juliana Gomes
Busca de Candidatos
