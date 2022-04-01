import csv
import json

result = []
with open('ikea.csv', encoding='utf-8') as f:
    csv_file = csv.DictReader(f, delimiter=';')

    for line in csv_file:
        for d in result:
            if line['product_name'] == d['name']:
                d['count'] += 1
                d['products'].append(line['keywords'])
                break
        else:
            result.append({'name': line['product_name'],
                           'count': 1,
                           'products': [line['keywords']]
                           })

result.sort(key=lambda dct: (dct['count'], dct['name']))

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
