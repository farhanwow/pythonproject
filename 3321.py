class mahasiswa:
    
    def __init__(self, anda, kuda, akhir):
        self.anda = anda
        self.kuda = kuda
        self.akhir = akhir
        self.email = anda + kuda + akhir + '@wasssup.com'

    def fullname(self):
        return '{} {}'.format(self.anda, self.kuda)

m_1 = mahasiswa('farhan', 'fadilah', '1')
m_2 = mahasiswa('rizki', 'nur', '69')

m_1.fullname()
print(mahasiswa.fullname(m_1))
print(m_1.email)
print(m_2.email)
print(0*0)
print(0 ** 0)
