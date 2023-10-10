from livro.livro import Livro

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano_publicacao, num_paginas):
        super().__init__(titulo, autor, ano_publicacao)
        self.num_paginas = num_paginas

if __name__ == "__main__":
    livrof = LivroFisico("Harry potter", "J K Rolling", 1997, 300)
    print(livrof)