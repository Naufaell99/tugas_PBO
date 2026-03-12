class Restaurant:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.number_served = 0  

    def deskripsikan_restoran(self):
        print("Nama Restoran :", self.nama_restoran)
        print("Jenis Masakan :", self.jenis_masakan)

    def buka_restoran(self):
        print(self.nama_restoran, "sekarang buka!\n")

    def set_number_served(self, jumlah):
        self.number_served = jumlah

    def increment_number_served(self, tambahan):
        self.number_served += tambahan


restaurant = Restaurant("Sanama", "Masakan Padang")


print("Jumlah pelanggan yang telah dilayani :", restaurant.number_served)

restaurant.number_served = 10
print("Jumlah pelanggan setelah diubah :", restaurant.number_served)


restaurant.set_number_served(25)
print("Jumlah pelanggan setelah set_number_served :", restaurant.number_served)

restaurant.increment_number_served(15)
print("Jumlah pelanggan setelah increment :", restaurant.number_served)