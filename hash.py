# kutuphaneyi import et
from dataclasses import dataclass
import hashlib 
# datetima kutuphanesinden datetime ve date import et
from datetime import datetime, date
from key import veri_sifrele, veri_coz
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#kolaylık olması icin bir case olusturuldu 
print("Hash olusturma icin = 1")
print("Hash Kontrol icin = 2")
print("Hash çözümleme icin = 3")
class block_data:
	def __init__(self, zaman, data, eski_hash):
		self.zaman = zaman
		self.data = data
		self.eski_hash = eski_hash
		self.hash = 


class Block:
	def __init__(self, eski_hash='0'):
		self.veri = block_data() = input("Hash oluşturmak icin input giriniz :")
		self.zaman = datetime.now()
		self.eski_hash = eski_hash
		self.hash = self.yeni_hash()

	def yeni_hash(self):
		veri = '-'.join(map(str,self.veri))
		public_key=  RSA.import_key(open('public_key.pem').read())
		hashable_data = (veri + self.zaman.isoformat() + self.eski_hash).encode()
		block_hash = veri_sifrele(hashable_data, PKCS1_OAEP.new(public_key)).upper()
		return block_hash
	
	def çalıştır(self):
		print(self.hash)
		a = self.hash
		f = open("d.txt", "ab") # open =  dosya acma 'a' dosyaya veri ekleme
		f.write(a+"\n".encode()) # dosyaya veri eklenen yer 
		f.close() #dosyadan cikmak icin 
class Test: #  kolaylik olması ve kafa karismamasi icin case olusturuldu
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
		girdi = input("")
		sifreli_veri = veri_sifrele(girdi.encode(), PKCS1_OAEP.new(RSA.import_key(open('public_key.pem').read())))
		cozumlenmis_veri = veri_coz(sifreli_veri, PKCS1_OAEP.new(RSA.import_key(open('private_key.pem').read())))
		print(cozumlenmis_veri)


# main dosyası 
if __name__ == '__main__':
	case = Test()
	case.inp(input(""))
