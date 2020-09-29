import json

from green_medic.apps.medicines.models import Medicine


def process_data():
    f = open('data.json')
    medicines = json.load(f)

    final_med_list = []

    for medicine in medicines:
        price = medicine.pop('price')
        price = price.replace(' Tk', '').replace('Price List', '0')
        if price == '':
            price = 0
        medicine['price'] = float(price)

        final_med_list.append(medicine)

    with open('data2.json', 'w', encoding='utf-8') as f:
        json.dump(medicines, f, ensure_ascii=False, indent=2)


def add_medicines(file='data2.json'):
    f = open(file)
    medicines = json.load(f)

    for med in medicines:
        med.pop('sl')
        Medicine.objects.create(**med)
