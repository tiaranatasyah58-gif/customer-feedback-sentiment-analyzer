# Customer Feedback Sentiment Analyzer
# Project Capstone - Dibuat pake IBM Bob

def analisis_sentimen(teks):
    teks = teks.lower()
    positif = ["bagus", "puas", "cepat", "ramah", "suka", "mantap", "baik", "enak"]
    negatif = ["buruk", "kecewa", "lama", "jelek", "marah", "rusak", "mahal", "lelet"]

    skor_positif = sum(1 for kata in positif if kata in teks)
    skor_negatif = sum(1 for kata in negatif if kata in teks)

    if skor_positif > skor_negatif:
        return "Positif"
    elif skor_negatif > skor_positif:
        return "Negatif"
    else:
        return "Netral"

# Contoh data
feedbacks = [
    "Pelayanan sangat bagus dan cepat, saya puas",
    "Makanan enak tapi pelayanan lama dan mengecewakan",
    "Harga mahal, kualitas jelek",
    "Suka banget, ramah dan mantap",
    "Biasa saja"
]

print("=== HASIL ANALISIS SENTIMEN ===")
for f in feedbacks:
    hasil = analisis_sentimen(f)
    print(f"- {f} => {hasil}")
