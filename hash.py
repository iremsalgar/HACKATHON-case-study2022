# kutuphaneyi import etttik 
import hashlib 
# datetima kutuphanesinden datetime ve date import et 
from datetime import datetime, date

class Block:
	def __init__(self, eski_hash='0'):
		self.veri = self.veri_olustur = input("")
		self.zaman = datetime.now()
		self.onceki_hash = eski_hash
		self.hash = self.yeni_hash()

	def veri_olustur(self, urun):
		self.urun = urun
		return (urun)

	def yeni_hash(self):
		veri = '-'.join(map(str,self.veri))
		hashable_data = (veri + self.zaman.isoformat() + self.onceki_hash).encode()
		block_hash = hashlib.sha256(hashable_data)
		return block_hash.hexdigest()
	
	def çalıştır(self):
		print(self.hash)
		a = self.hash
		f = open("d.txt", "a")
		f.write(a+ " " +"\n")
		f.close()
class Test:
	def inp(self, inp):
		return getattr(self, ('case_' + str(inp)))()
	def case_1(self):
		block = Block()
		a = block.çalıştır()
	def case_2(self):
		f = open("d.txt", "r")
		kontrol = f.readline()
		#print(kontrol)
		inputhash = input("")
		if kontrol == inputhash:
			print("kullanıcı tanımlı")
		else:
			print("HATA")
		f.close()

if __name__ == '__main__':
	case = Test()
	case.inp(input(""))