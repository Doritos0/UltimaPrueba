class Compra:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        compra = self.session.get("compra")
        if not compra:
            self.session["compra"]={}
            self.compra = self.session["compra"]
        else:
            self.compra= compra

    def agregar(self, producto):
        id = str(producto.nom_prod)
        if id not in self.compra.keys():
            self.compra[id]={
                "nom_prod":producto.nom_prod,
                "precio":producto.precio,
                "Unidades":1,

            }
        else:
            self.compra[id]["Unidades"]+=1
            self.compra[id]["precio"]+=producto.precio
        
        self.guardar_compra()
    
    def guardar_compra(self):
        self.session["compra"] = self.compra
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.nom_prod)
        if id in self.compra:
            del self.compra[id]
            self.guardar_compra()
    
    def restar(self, producto):
        id = str(producto.nom_prod)
        if id in self.compra.keys():
            self.compra[id]["Unidades"]-=1
            self.compra[id]["precio"]-=producto.precio
            
            self.guardar_compra()

            if self.compra[id]["Unidades"]<=0:
                self.eliminar(producto)
            
                self.guardar_compra()
        
    def limpiar (self):
        self.session["compra"]={}
        self.session.modified= True

    def agregar_tradicional (self):
        id = str('Tradicional')

        if id not in self.compra.keys():
            self.compra[id]={
                "nom_prod":"Tradicional",
                "precio":5990,
                "Unidades":1,

            }
        else:
            self.compra[id]["Unidades"]+=1
            self.compra[id]["precio"]+=5990
        
        self.guardar_compra()

    def restar_tradicional (self):
        id = str('Tradicional')

        if id  in self.compra.keys():
            self.compra[id]["Unidades"]-=1
            self.compra[id]["precio"]-=5990
            self.guardar_compra()

            if self.compra[id]["Unidades"]<=0:
                    self.eliminar_tradicional()
                
                    self.guardar_compra()
        
    def eliminar_tradicional(self):
        id = str('Tradicional')
        if id in self.compra:
            del self.compra[id]
            self.guardar_compra() 
        
    def agregar_vegana (self):
        id = str('Vegana')

        if id not in self.compra.keys():
            self.compra[id]={
                "nom_prod":"Vegana",
                "precio":6990,
                "Unidades":1,

            }
        else:
            self.compra[id]["Unidades"]+=1
            self.compra[id]["precio"]+=6990
        
        self.guardar_compra()

    def restar_vegana (self):
        id = str('Vegana')

        if id  in self.compra.keys():
            self.compra[id]["Unidades"]-=1
            self.compra[id]["precio"]-=6990
            self.guardar_compra()

            if self.compra[id]["Unidades"]<=0:
                    self.eliminar_vegana()
                
                    self.guardar_compra()

    def eliminar_vegana(self):
        id = str('Vegana')
        if id in self.compra:
            del self.compra[id]
            self.guardar_compra() 