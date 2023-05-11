import fire

class Kalkulator(object):
    #this is calculator using fire module

    def kuadrat(self,angka):
        return angka*angka
    
    def kali(self,angka1,angka2):
        return angka1 * angka2
    
if __name__ == '__main__':
    fire.Fire(Kalkulator)