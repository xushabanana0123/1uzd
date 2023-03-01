import csv
import datetime

class Rekins:
  def __init__(self, klients, veltijums, izmers, materials): 
    self.klients = klients
    self.veltijums = veltijums
    self.izmers = izmers
    self.materials = materials
    self.laiks = datetime.datetime.now()
    self.summa = self.aprekins()

  def izdrukat(self):
    print("=== Rekins ===")
    print(f"klients: {self.klients}")
    print(f"Veltijums: {self.veltijums}")
    print(f"Izmers: {self.izmers}")
    print (f"Materials: {self.materials}")
    print(f"Laiks: {self.laiks}")
    print (f"Summa: {self.summa}")

  def aprekins(self):
    return 42.0

  def saglabat (self):
    filename = f"{self.klients}_ {self.laiks.date()}.csv"
    with open(filename, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Klients", "Veltijums", "Izmers", "Materials", "Laiks", "Summa"])
      writer.writerow([self.klients, self.veltijums, self.izmers, self.materials, self.laiks, self.summa])

#
print("=== Izveidojam jaunu saskaitu ===")
klients = input("Klients: ")
veltijums = input ("Veltijums: ")
izmers = input("Izmers (3 veseli skaitli, atdaliti ar komatiem): ")
izmers = [int(x.strip()) for x in izmers.split(",")]
materials = float (input("Materials: "))
saskaita_objekts = Rekins(klients, veltijums, izmers, materials)
saskaita_objekts.saglabat()
saskaita_objekts.izdrukat()