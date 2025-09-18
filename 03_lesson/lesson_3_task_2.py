from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24", "+79264567890"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79375551234"),
    Smartphone("Google", "Pixel 8", "+79443332211"),
    Smartphone("OnePlus", "11 Pro", "+79556667788"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
