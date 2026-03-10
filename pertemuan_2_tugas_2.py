class User:
    def __init__(self, nama_depan, nama_belakang, umur, email, kota):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.umur = umur
        self.email = email
        self.kota = kota
        self.login_attempts = 0   
        
    def describe_user(self):
        print("Nama Lengkap :", self.nama_depan, self.nama_belakang)
        print("Umur :", self.umur)
        print("Email :", self.email)
        print("Kota :", self.kota)

    def greet_user(self):
        print("Halo", self.nama_depan + ", selamat datang!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Naufal", "Kurnia", 19, "naufal@email.com", "Pekanbaru")

user1.describe_user()
user1.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Jumlah percobaan login :", user1.login_attempts)

user1.reset_login_attempts()

print("Jumlah percobaan login setelah reset :", user1.login_attempts)