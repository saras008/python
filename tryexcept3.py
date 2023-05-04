try:
    f=open("test.txt")
    try:
        f.write("Testing nulis text ke file test.txt")
    except NameError:
        print("Tidak bisa menulis ke file")
    finally:
        f.close
except:
    print("something wrong went opening the file")