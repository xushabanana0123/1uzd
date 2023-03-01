import datetime as time


class Rekins:
    def __init__(self, client: str, dedication: str, size: list, material: float):
        self.creation_time = time.datetime.now()
        self.client = client
        self.dedication = dedication
        self.size = size
        self.material = material

        # method has to be booted on initialization
        self.total = self.aprekins()

        # all data to print out
        self.properties = {
            "time": self.creation_time,
            "client": self.client,
            "dedication": self.dedication,
            "size": self.size,
            "material": self.material,
            "total": self.total,
        }

    def print(self):
        print(self.properties, sep="\n")
        return None

    def aprekins(self):
        
        return 0


if __name__ == '__main__':
    a = input("name: ")
    b = input("dedication:")
    c = []
    for i in range(1, 4):
        c.append(input(f"size{i} (int): "))
    d = float(input("material (float): "))
    instance = Rekins(a, b, c, d)
    instance.print()