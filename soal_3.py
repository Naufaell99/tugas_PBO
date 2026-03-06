class User:
    def __init__(self, nama_depan, nama_belakang, umur, email, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.email = email
        self.kota = kota

    def describe_user(self):
        print("Nama Lengkap :", self.nama_depan, self.nama_belakang)
        print("Umur :", self.umur)
        print("Email :", self.email)
        print("Kota :", self.kota)

    def greet_user(self):
        print("Halo", self.nama_depan + ", selamat datang!\n")

user1 = User("Naufal", "Kurnia", 19, "naufal@email.com", "Pekanbaru")
user2 = User("juliasafitri", "julia", 20, "julia@email.com", "Medan")
user3 = User("Siti", "Aisyah", 21, "siti@email.com", "Jakarta")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
