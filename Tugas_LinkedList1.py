# Mendefinisikan class menu item untuk linked list pada program
class MenuItem:
    def __init__(self, NamaMenu, Harga):
        self.NamaMenu = NamaMenu
        self.Harga = Harga
        self.next = None

# mendefinisikan bahwa head dan tail linked list masih kosong
head = None
tail = None

# membuat fungsi untuk menambahkan menu dalam program ke class MenuItem
def addMenuItem(NamaMenu, Harga):
    global head, tail
    newItem = MenuItem(NamaMenu, Harga)
    if head is None:
        head = newItem
        tail = newItem
    else:
        tail.next = newItem
        tail = newItem

# membuat fungsi untuk tampilan program
def DisplayMenu():
    print("""\n
          =============================================
          == Selamat Datang di E-Order Warung D4 MIE ==
          =============================================
           Ice cream dan mie pedas tersedia disini!!
          =============================================
          
Berikut merupakan menu kami :
=============================""")
    temp = head
    while temp is not None:
        print(temp.NamaMenu, "Rp.", temp.Harga)
        temp = temp.next
    print("""=============================
Ketik menu yang akan dipesan, dan ketik "done" jika merasa cukup.""")
    
# Menambahkan menu dalam program
addMenuItem("Mixue Ice Cream", 5000)
addMenuItem("Boba Shake", 16000)
addMenuItem("Mi Sundae", 14000)
addMenuItem("Mie Ganas", 11000)
addMenuItem("Creamy Mango Boba", 22000)

# mendefinisikann variabel untuk daftar pesanan
totalHarga = 0
max_pesanan = 10
pesanan = [""] * max_pesanan
harga = [0] * max_pesanan
Jml_Pesanan = 0

# mulai menjalankan program
DisplayMenu()
