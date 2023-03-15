class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    # metodos especiales __???__
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Instancia eliminada")

mi_cd = CD("Pink Floyd", "The Wall", 24)

print(mi_cd)
print(len(mi_cd))
# con del, elimino una instacia
del mi_cd
