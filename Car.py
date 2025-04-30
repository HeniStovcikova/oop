class Brand:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Car:
    def __init__(self, brand: Brand, color):
        """

        :param brand: is type Brand
        :param color:
        """
        self.brand = brand
        self.color = color

    def move(self, distance=100):
        print(f"{self.brand}: BrrrrmBrrrBrrmm {distance}")

b1 = Brand("Škoda", 1920)
b2 = Brand("Ferrari", 1890)

c1 = Car(b1, "red") # list() -> []
c2 = Car(b2, "green")
c3 = Car(b2, "green")

print(c1.brand)
print(c1.brand.name)

print()


print(c1.color)
print(c2.color)

print()
c2.color = "black"

print(c1.color)
print(c2.color)

c1.move()
c2.move()

print(c2 == c3)

print(type(c2))
print(type(c3))

print(c2)
print(c3)

print()
c4 = c3
print(c4 == c3)
print(c4)
print(c3)

c4.color = "pink"
print(c3.color)
print(c4.color)