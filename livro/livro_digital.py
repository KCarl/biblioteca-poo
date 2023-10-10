from livro import Livro

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, formato):
        super().__init__(titulo, autor, ano_publicacao)
        self.formato = formato
if __name__ == "__main__":
    livroD = LivroDigital("Harry Potter", "J K Rolling",
                          1997, "PDF")
    print(livroD)

