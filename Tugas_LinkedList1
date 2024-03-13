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
