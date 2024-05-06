class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)
    
    def __repr__(self):
        return f"{self.name} {self.height} {self.weight:.1f}"

people = [Person(*input().split()) for _ in range(5)]

print('name')
for person in sorted(people, key= lambda x:x.name):
    print(person)

print()

print('height')
for person in sorted(people, key= lambda x:-x.height):
    print(person)