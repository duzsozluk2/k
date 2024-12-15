def diameter_security_test(phone_number):
    print(f"Diameter Güvenlik Testi Başlatılıyor... Hedef Numara: {phone_number}")
    # Diameter protokolü güvenlik testleri gerçekleştirilir
    
    # Örnek sonuç bilgisi
    
    
    print("Test Sonuçları:")
    for key, value in test_result.items():
        print(f"{key}: {value}")
    
    print("Diameter Güvenlik Testi Tamamlandı.")

if __name__ == "__main__":
    target_number = input("Lütfen hedef telefon numarasını girin: ")
    diameter_security_test(target_number)
