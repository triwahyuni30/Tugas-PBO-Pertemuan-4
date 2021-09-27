class Ojek():
   def __init__(self, nama, transmisi, alamat): 
      self.nama = nama
      self.transmisi = transmisi
      self.alamat = alamat
   
   def cek_id_abang(self):
       print('\nnama:', self.nama, '\nmotor:',self.transmisi, '\nalamat: ', self.alamat)

class Gojek(Ojek):
    def __init__(self, nama, transmisi, alamat): 
       self.nama = nama
       self.transmisi = transmisi
       self.alamat = alamat
    
    def cek_id_abang (self):
        print('\nnama:', self.nama, '\nmotor:',self.transmisi, '\nalamat:',self.alamat)


ojek1 = Ojek('Andri', 'manual', 'Warung Jati')
ojek2 = Ojek('Herdiana', 'matic', 'Serang')

ojek1.cek_id_abang()
ojek2.cek_id_abang()