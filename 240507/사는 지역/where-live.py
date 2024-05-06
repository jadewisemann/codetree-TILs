class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city
    def __repr__(self):
        return f"name {self.name}\naddr {self.addr}\ncity {self.city}"
    
people = (Person(*input().split()) for _ in range(int(input())))
print(sorted(people, key= lambda x: x.name)[-1])