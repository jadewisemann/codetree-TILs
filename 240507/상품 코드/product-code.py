class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def __repr__(self):
        return(
            f"product {self.code} is {self.name}"
        )

print(product1:=Product("codetree", "50"))
print(prodcut2:=Product(*input().split()))