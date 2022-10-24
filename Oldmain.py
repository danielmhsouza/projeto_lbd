class Conta:

    def __init__(self, id, banco, numero_banco, numero_conta, chave_pix, operacao, agencia):
        self.id = id
        self.banco = banco
        self.numero_banco = numero_banco
        self.numero_conta = numero_conta
        self.chave_pix = chave_pix
        self.opercao = operacao
        self.agencia = agencia


class Produto:

    def __init__(self, id, nome, preco, desc, url_video, arquivo):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.desc = desc
        self.url_video = url_video
        self.arquivo = arquivo

class Usuario:


    def __init__(self, id, nome, cpf, telefone, email, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.conta = None
        self.produto_comprado = []
        self.produto_venda = []

    def addProdutoVenda(self, id, nome, preco, desc, url_video, arquivo):
        self.produto_venda.append(Produto(id, nome, preco, desc, url_video, arquivo))

    def editProduto(self, id, nome, preco, desc, url_video, arquivo):
        if(nome):
            self.produto_venda[id].nome = nome
        if(preco):
            self.produto_venda[id].preco = preco
        if (desc):
            self.produto_venda[id].desc = desc
        if (url_video):
            self.produto_venda[id].url_video = url_video
        if (arquivo):
            self.produto_venda[id].arquivo = arquivo

    def removeProduto(self, id):
        self.produto_venda.remove(id)

    def comprarProduto(self, produto):
        self.produto_comprado.append(produto)

    def addConta(self, id, banco, numero_banco, numero_conta, chave_pix, operacao, agencia):
        self.conta = Conta( id, banco, numero_banco, numero_conta, chave_pix, operacao, agencia)


usuario1 = Usuario(1, 'Daniel', '999.999.999-99', '12944444444', 'email@email.com', 'senha123')
usuario1.addConta(usuario1.id, 'CAIXA', '104', '123456789', usuario1.telefone, '13', '0000')
usuario1.addProdutoVenda(1, 'curso de PHP', 2.50, 'cursinho bala pra arrasar', 'https://www.youtube.com/watch?v=R3yqKpMiG2Q&ab_channel=CanalInacredit%C3%A1vel', './arquivos/usuarios/1/arquivo.pdf')
usuario1.addProdutoVenda(1, 'Planilha de Investimentos', 2.50, 'cursinho bala pra arrasar', 'https://www.youtube.com/watch?v=R3yqKpMiG2Q&ab_channel=CanalInacredit%C3%A1vel', './arquivos/usuarios/1/arquivo.pdf')


usuario2: Usuario = Usuario(2, 'Sara', '999.999.999-99', '12944444444', 'email@email.com', 'senha123')
usuario2.addProdutoVenda(2, 'Instensivo de SQL', 580, 'cursinho bala pra arrasar na balada', 'https://www.youtube.com/watch?v=R3yqKpMiG2Q&ab_channel=CanalInacredit%C3%A1vel', './arquivos/usuarios/2/arquivo.pdf')

usuario2.comprarProduto(usuario1.produto_venda[1])

usuario1.comprarProduto(usuario2.produto_venda[0])

print('Usuario1 se chama: ' + usuario1.nome)
for i in usuario1.produto_venda:
    print('Usuario1 vende: ' + i.nome)
for i in usuario1.produto_comprado:
    print('Usuario1 comprou: ', i.nome)

print('Usuario1 pix: ' + usuario1.conta.chave_pix)

print('\nUsuario2 se chama: ' + usuario2.nome)

for i in usuario2.produto_venda:
    print('Usuario2 vende: ' + i.nome)
for i in usuario2.produto_comprado:
    print('Usuario2 comprou: ', i.nome)

print('Usuario2 acessou o link: ', usuario2.produto_comprado[0].url_video)

