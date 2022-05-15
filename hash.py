# kutuphaneyi import et
# datetima kutuphanesinden datetime ve date import et
from datetime import datetime
import hashlib
print("blok olusturma icin = 1")
print("block Kontrol icin = 2")
print("block çözümleme icin = 3")

class datas:
	def __init__(self, urun_bilgisi, kullanıcı_kimliği, hasar_kaydı, kullanıcı_adresi):
		self.urun_bilgisi = urun_bilgisi
		self.kullanıc_kimliği = kullanıcı_kimliği
		self.hasar_kaydı = hasar_kaydı
		self.kullanıcı_adresi = kullanıcı_adresi

class block_data:
	def __init__(self, zaman, data, eski_hash = "0"):
		self.zaman = zaman
		self.data = data
		self.eski_hash = eski_hash 
		self.hash = self.get_hash()
	def get_hash(self):
		return 	(hashlib.sha256((str(self.zaman)+ str(self.data)+ str(self.eski_hash)).encode()).hexdigest())

class Block_chain:
	def __init__(self):
		self.chain= [self.genessisblock()]
	def genessisblock(self):
		return block_data(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "first data", "")
	def block_ekle(self, data):
		node= block_data(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),data, self.chain[-1].hash)
		self.chain.append(node)
	def kontrol(self):
		for i in range(len(self.chain)) :
			if i != 0 :
				ilk = self.chain[i-1].hash
				suan = self.chain[i].eski_hash
				if ilk != suan :
					return('block GG')
				return 'saglam'
	def listleme(self):
		print("Blokchain = \n")
		for i in range(len(self.chain)):
			print("=================\n")
			print("Block = ", i, "\nHash = ", str(self.chain[i].hash), '\nzaman damgasi = ', str(self.chain[i].zaman), '\ndata = ', str(self.chain[i].data), '\neski hash = ', str(self.chain[i].eski_hash))
			print("=================\n")

	


# main dosyası 

urun = Block_chain()
while(1) :
	case = (input(""))
	if case == '1':
		urun.block_ekle(datas(input("urun bilgisi: "), input("kullanici kimligi: "), input("hasar kaydi: "),input("kullanici adresi: ")))
	if case == '2':
		urun.kontrol
	if case == '3':
		urun.listleme()
