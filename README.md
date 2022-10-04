# projeto_lbd

Descrição:

Plataforma para vender suas playlists de cursos do youtube, podendo monetizar seus vídeos sem a necessidade de visualizações na plataforma.

O usuário pode assumir 3 funções:
vendedor, comprador e administrador.

neste momento, serão tratados apenas usuários como comprador e vendedor, porem existirá uma coluna com o nome "permissão" na entidade usuário. A permissão é diferente apenas para usuários administradores.


Regras de negócio:

*Usuários podem fazer upload de vários produtos;

*O usuário tem acesso aos seus uploads, que direcionam para o produto;

*Usuários recebem pagamento pela venda de seus produtos;

*Usuários podem atualizar seus produtos;

*A atualização deve ser explicita para os usuários compradores, algo como "ultima atualização em...";

*Usuários podem comprar produtos;

*Ao comprar recebem um item de acesso que direciona ao produto comprado;

*Cada produto tem seu próprio conteúdo;

*O conteúdo se divide em arquivos disponibilizados pelo autor e a url da playlist privada contendo os vídeos;
