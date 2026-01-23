from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro Max", "+73383423820"),
    Smartphone("Xiaomi", "14 Ultra", "+73383424820"),
    Smartphone("Nuawei", "Mate10", "+79983423820"),
    Smartphone("Poco", "F6", "+73383424420"),
    Smartphone("Nokia", "3310", "+72443423820")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
