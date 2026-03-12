class Restaurant:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print("Nama Restoran :", self.nama_restoran)
        print("Jenis Masakan :", self.jenis_masakan)

    def buka_restoran(self):
        print(self.nama_restoran, "sekarang buka!\n")

restaurant = Restaurant("Sanama", "Masakan Padang")

print("Nama Restoran :", restaurant.nama_restoran)
print("Jenis Masakan :", restaurant.jenis_masakan)
print()

restaurant.deskripsikan_restoran()
restaurant.buka_restoran()

restaurant1 = Restaurant("rendang", "Masakan Padang")
restaurant2 = Restaurant("kokek", "Masakan Melayu")
restaurant3 = Restaurant("dendeng", "Masakan Jawa")

restaurant1.deskripsikan_restoran()
print()

restaurant2.deskripsikan_restoran()
print()

restaurant3.deskripsikan_restoran()
print()