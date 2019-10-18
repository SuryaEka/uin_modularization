nama = 'Surya Eka Kurnia'
program = 'Gerak Lurus'

print(f'program {program} oleh {nama}')

def hitung_daya(usaha,waktu):
    daya = usaha / waktu
    print(f'usaha joule dalam satuan waktu = {waktu / 60}menit')
    print(f'Sehingga daya = {daya} joule/s')
    return daya

# usaha = 1000
# waktu = 5 * 60
daya = hitung_daya(1000, 5 * 60)
daya = hitung_daya(3000, 70 * 60)