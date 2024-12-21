from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+79959990909"),
    Smartphone("HONOR", "Magic V2", "+79141636363"),
    Smartphone("Xiaomi", "Redmi note 9a", "+79999591111"),
    Smartphone("Samsung", "Galaxy S24", "+79969965121"),
    Smartphone("HUAWEI", "nova 11pro", "+79033090309")
    
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
