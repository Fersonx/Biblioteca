class Livro:
    def __init__(self, titulo, autor, ano, copias):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias = copias

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Cópias Disponíveis: {self.copias}"

    def emprestar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False

    def devolver(self):
        self.copias += 1

class Usuario:
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.identificacao}, Contato: {self.contato}"

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = {} # {titulo_livro: [id_usuario1, id_usuario2]}

    def cadastrar_livro(self, titulo, autor, ano, copias):
        if titulo in self.livros:
            print(f"Erro: O livro '{titulo}' já está cadastrado na biblioteca.")
        else:
            novo_livro = Livro(titulo, autor, ano, copias)
            self.livros[titulo] = novo_livro
            print(f"Livro '{titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, nome, identificacao, contato):
        if identificacao in self.usuarios:
            print(f"Erro: Usuário com ID '{identificacao}' já está cadastrado.")
        else:
            novo_usuario = Usuario(nome, identificacao, contato)
            self.usuarios[identificacao] = novo_usuario
            print(f"Usuário '{nome}' (ID: {identificacao}) cadastrado com sucesso.")

    def emprestar_livro(self, usuario_id, titulo_livro):
        if usuario_id not in self.usuarios:
            print(f"Erro: Usuário com ID '{usuario_id}' não encontrado.")
            return

        if titulo_livro not in self.livros:
            print(f"Erro: Livro '{titulo_livro}' não encontrado.")
            return

        livro = self.livros[titulo_livro]
        if livro.emprestar():
            if titulo_livro not in self.emprestimos:
                self.emprestimos[titulo_livro] = []
            self.emprestimos[titulo_livro].append(usuario_id)
            print(f"Livro '{titulo_livro}' emprestado para o usuário ID '{usuario_id}' com sucesso.")
        else:
            print(f"Erro: O livro '{titulo_livro}' não possui cópias disponíveis para empréstimo.")

    def devolver_livro(self, usuario_id, titulo_livro):
        if usuario_id not in self.usuarios:
            print(f"Erro: Usuário com ID '{usuario_id}' não encontrado.")
            return

        if titulo_livro not in self.livros:
            print(f"Erro: Livro '{titulo_livro}' não encontrado.")
            return

        if titulo_livro not in self.emprestimos or usuario_id not in self.emprestimos[titulo_livro]:
            print(f"Erro: O usuário ID '{usuario_id}' não possui o livro '{titulo_livro}' emprestado.")
            return

        livro = self.livros[titulo_livro]
        livro.devolver()
        self.emprestimos[titulo_livro].remove(usuario_id)
        if not self.emprestimos[titulo_livro]: # Se não há mais usuários com este livro
            del self.emprestimos[titulo_livro]
        print(f"Livro '{titulo_livro}' devolvido pelo usuário ID '{usuario_id}' com sucesso.")

    def consultar_livro(self, criterio, valor):
        encontrados = []
        for titulo, livro in self.livros.items():
            if criterio.lower() == "titulo" and valor.lower() in titulo.lower():
                encontrados.append(livro)
            elif criterio.lower() == "autor" and valor.lower() in livro.autor.lower():
                encontrados.append(livro)
            elif criterio.lower() == "ano" and str(valor) == str(livro.ano):
                encontrados.append(livro)

        if encontrados:
            print(f"\n--- Livros encontrados por {criter}: '{valor}' ---")
            for livro in encontrados:
                print(livro)
            print("------------------------------------------")
        else:
            print(f"Nenhum livro encontrado por {criter}: '{valor}'.")

    def relatorio_livros_disponiveis(self):
        print("\n--- Relatório de Livros Disponíveis ---")
        disponiveis = False
        for titulo, livro in self.livros.items():
            if livro.copias > 0:
                print(livro)
                disponiveis = True
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
        print("---------------------------------------")

    def relatorio_livros_emprestados(self):
        print("\n--- Relatório de Livros Emprestados ---")
        if not self.emprestimos:
            print("Nenhum livro emprestado no momento.")
            return

        for titulo, usuarios_ids in self.emprestimos.items():
            livro = self.livros[titulo]
            print(f"Livro: {livro.titulo} ({livro.autor})")
            for user_id in usuarios_ids:
                usuario = self.usuarios[user_id]
                print(f"  - Emprestado para: {usuario.nome} (ID: {usuario.identificacao})")
        print("---------------------------------------")

    def relatorio_usuarios(self):
        print("\n--- Relatório de Usuários Cadastrados ---")
        if not self.usuarios:
            print("Nenhum usuário cadastrado no momento.")
            return

        for identificacao, usuario in self.usuarios.items():
            print(usuario)
        print("------------------------------------------")


def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Biblioteca ---")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Consultar Livro")
    print("6. Relatório de Livros Disponíveis")
    print("7. Relatório de Livros Emprestados")
    print("8. Relatório de Usuários")
    print("9. Sair")
    print("---------------------------------------------")

def main():
    biblioteca = Biblioteca()

    # Dados de exemplo para teste
    biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis", 1899, 3)
    biblioteca.cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 5)
    biblioteca.cadastrar_usuario("Ana Silva", "12345", "ana@email.com")
    biblioteca.cadastrar_usuario("Bruno Costa", "67890", "bruno@email.com")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == '1':
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = int(input("Ano de publicação: "))
                copias = int(input("Número de cópias: "))
                biblioteca.cadastrar_livro(titulo, autor, ano, copias)
            elif opcao == '2':
                nome = input("Nome do usuário: ")
                identificacao = input("ID do usuário: ")
                contato = input("Contato do usuário: ")
                biblioteca.cadastrar_usuario(nome, identificacao, contato)
            elif opcao == '3':
                usuario_id = input("ID do usuário: ")
                titulo_livro = input("Título do livro a emprestar: ")
                biblioteca.emprestar_livro(usuario_id, titulo_livro)
            elif opcao == '4':
                usuario_id = input("ID do usuário: ")
                titulo_livro = input("Título do livro a devolver: ")
                biblioteca.devolver_livro(usuario_id, titulo_livro)
            elif opcao == '5':
                criterio = input("Consultar por (titulo/autor/ano): ").lower()
                valor = input(f"Digite o {criterio} para consulta: ")
                biblioteca.consultar_livro(criterio, valor)
            elif opcao == '6':
                biblioteca.relatorio_livros_disponiveis()
            elif opcao == '7':
                biblioteca.relatorio_livros_emprestados()
            elif opcao == '8':
                biblioteca.relatorio_usuarios()
            elif opcao == '9':
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção de 1 a 9.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico quando solicitado (ano, número de cópias).")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()