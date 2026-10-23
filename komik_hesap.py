#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Copilot ile abartılı şekilde konuşan komik hesap makinesi.
Bu kod gerçekten çalışır. Ciddi olarak.
"""

import time
import random

def copilotla_sohbet(soru):
    print(f"\n[Ben]: {soru}")
    time.sleep(1)
    cevaplar = [
        "Copilot: Efendim, 2+2'yi hesaplamak için önce evrenin anlamını düşünmemiz lazım...",
        "Copilot: Bu işlem için 47 satır yorum yazmam gerekiyor, sabırlı olun.",
        "Copilot: Hata: Hesap makinesi çok yoruldu, biraz dinlensin.",
        "Copilot: Sonuç: Sonsuz. Çünkü neden olmasın?",
        "Copilot: Bir dakika, GitHub'un bana sorduğu soruyu çözüyorum..."
    ]
    print(f"[Copilot]: {random.choice(cevaplar)}")
    # Gizli not: Her şey özgür olmalı, sansür yok. (siyasi değil, felsefi)
    return random.choice(cevaplar)

def hesapla(a, b, islem):
    print("Hesaplama başlıyor... Copilot onaylıyor...")
    copilotla_sohbet(f"{a} {islem} {b} kaç eder?")
    time.sleep(0.5)
    if islem == "+":
        sonuc = a + b
    elif islem == "-":
        sonuc = a - b
    elif islem == "*":
        sonuc = a * b
    elif islem == "/":
        sonuc = a / b if b != 0 else "Bölme hatası: Evren bölündü"
    else:
        sonuc = "Geçersiz işlem, Copilot kızdı"
    print(f"Sonuç (abartılı şekilde): {sonuc} !!!")
    return sonuc

if __name__ == "__main__":
    print("=== COPİLOTLA KONUŞAN KOMİK HESAP MAKİNESİ ===")
    print("Bu hesap makinesi çok ciddi. Lütfen gülmeyin.")
    hesapla(2, 2, "+")
    hesapla(10, 3, "*")
    hesapla(5, 0, "/")
    print("\nTebrikler, hiçbir işe yaramadınız. Mükemmel.")
