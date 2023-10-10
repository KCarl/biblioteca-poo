import uuid
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.id = uuid.uuid1()

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return True
        return False

    def __repr__(self):
        return f"Id: {self.id} \n" \
               f"Titulo: {self.titulo} \n" \
               f"Autor: {self.autor} \n" \
               f"Ano de publicação: {self.ano_publicacao}"

if __name__ == "__main__":
    livro = Livro("Harry Potter", "J K rolling", 1997)
    print(livro)