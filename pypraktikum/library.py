import random
import datetime
from strukturData import karier, cinta, keberuntungan

def hitung_umur(tgl_lahir):
    try:
        tahun_lahir = datetime.datetime.strptime(tgl_lahir, "%Y-%m-%d")
        umur = datetime.datetime.now().year - tahun_lahir.year
        return umur
    except ValueError:
        return None

def ramal_masa_depan(nama, umur):
    print(f"\n🔮 Halo {nama}! Berikut ramalan masa depanmu 🔮")
    print(f"📏 Umurmu sekarang: {umur} tahun")
    print(f"💼 Karier masa depan: {random.choice(karier)}")
    print(f"💖 Cinta masa depan: {random.choice(cinta)}")
    print(f"🍀 Keberuntungan hari ini: {random.choice(keberuntungan)}\n")
