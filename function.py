def my_function():
    print("This my first function on python")

my_function()

#arbitrary multi arguments
def nama_lengkap(fname, lname):
    print(fname + " " +lname)

nama_lengkap("iyus","simatupang")

def anak(*args):
    print("Nama anak pertama" + " " +args[2])

anak("iyus","dedi","putra")

#arbitrary multi keyword arguments
def ortu(**kwargs):
    print("Nama ayah/ibu" + " " + kwargs["nama_ibu"])

ortu(nama_ayah="labuan",nama_ibu="dora")

def fungsi_rujak(buah):
    for x in buah:
        print(x)

buah=["mangga","kedondong","nanas"]

fungsi_rujak(buah)