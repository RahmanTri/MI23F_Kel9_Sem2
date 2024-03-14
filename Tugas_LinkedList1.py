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
# membuat looping program agar dapat mengambil pesanan secara berulang 
while True:
    order = input("\nSilakan ketik pesanan Anda: ")
    if order == "done":
        break
    print("======")
    print("||>>", order, "sudah ditambahkan ke keranjang <<||")
    print("======")
    # untuk mencari daftar menu yang telah dipesan
    temp = head
    while temp is not None:
        if temp.NamaMenu == order: # jika pesanan ditemukan dalam linked list, maka
            pesanan[Jml_Pesanan] = temp.NamaMenu # nama pesanan akan dimasukkan ke list
 pesanan dan
            harga[Jml_Pesanan] = temp.Harga
            Jml_Pesanan += 1
            totalHarga += temp.Harga
            break
        temp = temp.next
# membuat total harga dan daftar menu yang dipesan
print("\n|| Pesanan Anda ||")
for i in range(Jml_Pesanan): # menggunakan perulangan for untuk mengambil daftar
pesanan dan harga melalui list daftar pesanan dan harga
    print(pesanan[i], "Rp.", harga[i])
# membuat pesan penutup berupa total harga

print("\nTotal harga pesanan Anda: Rp.", totalHarga)
print("\n------Terima Kasih telah E-Order di Warung Kami------")
