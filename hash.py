# kutuphaneyi import et
from calendar import c
from dataclasses import dataclass
import hashlib 
# datetima kutuphanesinden datetime ve date import et
from datetime import datetime, date
from platform import node
from key import veri_sifrele, veri_coz
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#kolaylık olması icin bir case olusturuldu 
print("Hash olusturma icin = 1")
print("Hash Kontrol icin = 2")
print("Hash çözümleme icin = 3")
class datas:
	def __init__(self, kullanıcı_kimliği, hasar_kaydı, kullanıcı_adresi):
		self.kullanıc_kimliği = self.kullanıc_kimliği + " " +kullanıcı_kimliği
		self.hasar_kaydı =      self.hasar_kaydı + " " +hasar_kaydı
		self.kullanıcı_adresi = self.kullanıcı_adresi + " " +hasar_kaydı

class block_data:
	def __init__(self, zaman, data, eski_hash = "0"):
		self.zaman = zaman
		self.data = data
		self.eski_hash = eski_hash 
		self.hash = get_hash()

	def get_hash(self):
		return 	veri_sifrele((self.zaman, self.data, self. eski_hash).encode(), \
		(PKCS1_OAEP.new(RSA.import_key(open('public_key.pem').read()))))

class Block_chain:
	def __init__(self):
		self.chain= [self.genessisblock()]
	def genessisblock(self):
		return block_data(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "first data", "")
	def block_ekle(self, data):
		node= block_data(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),data, self.chain[-1].hash)
		self.chain.node
	def kontrol(self):
		for i in range(len(Self.chain)):
			if i != 0 :
				ilk = self.chain[i-1].hash
				suan = self.chain[i].eski_hash
				if ilk != suan :
					return('block GG')
				return 'saglam'
	def listleme(self):
		print("Blokchain = \n")
		for i in range(len(self.chain)):
			print("Block => ",i,"\nHash = ", str(self.chain[i].hash),"\nZaman Damgası =", str(self.chain[i].zaman), "\nData = ",str(self.chain[i].data), "\nEski Hash = ", str(self.chain[i].eski_hash))

class Test: #  kolaylik olması ve kafa karismamasi icin switch case olusturuldu
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
	while(1) :
		case.inp(input(""))
