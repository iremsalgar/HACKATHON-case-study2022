# kutuphaneyi import et
import hashlib 
# datetima kutuphanesinden datetime ve date import et
from datetime import datetime, date
import key.py
#kolaylık olması icin bir case olusturuldu 
print("Hash olusturma icin = 1")
print("Hash Kontrol icin = 2")
class Block:
	def __init__(self, eski_hash='0'):
		self.veri = self.veri_olustur = [input("Hash oluşturmak icin input giriniz :")] 
		self.zaman = datetime.now()
		self.onceki_hash = eski_hash
		self.hash = self.yeni_hash()

	def veri_olustur(self, urun):
		self.urun = urun
		return (urun)

	def yeni_hash(self):
		veri = '-'.join(map(str,self.veri))
		hashable_data = (veri + self.zaman.isoformat() + self.onceki_hash).encode()
		block_hash = veri_sifrele(hashable_data)
		return block_hash.hexdigest()
	
	def çalıştır(self):
		print(self.hash)
		a = self.hash
		f = open("d.txt", "a") # open =  dosya acma 'a' dosyaya veri ekleme
		f.write(a+ " " +"\n") # dosyaya veri eklenen yer 
		f.close() #dosyadan cikmak icin 
class Test:
	def inp(self, inp):
		return getattr(self, ('case_' + str(inp)))()# icine yazılan paremetre ile birleştiyor 
	def case_1(self):
		block = Block()
		a = block.çalıştır()
	def case_2(self):# ------SUAN BU FONKSIYON CALISMIYOR----
		f = open("d.txt", "r") # 'r' read 
		kontrol = f.readline()
		#print(kontrol)
		inputhash = input("Lutfen kontrol etmek istediginiz Hash kodunu giriniz :")
		if kontrol == inputhash:
			print("Hash tanımlı")
		else:
			print("HATA")
		f.close()
		#--------------------------------------------------------
	def case_3(self):
		veri_coz(veri, private_key)

# main dosyası 
if __name__ == '__main__':
	case = Test()
	case.inp(input(""))
