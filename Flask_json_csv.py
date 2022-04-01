from flask import Flask, jsonify, send_file
import argparse
import json
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--adress')
parser.add_argument('--port')
parser.add_argument('--count', type=int, default=10)
args = parser.parse_args()

app = Flask(__name__)


@app.route('/')
@app.route('/ikea')
def ikea():
    with open('result.json', encoding='utf-8') as file:
        json_file = json.load(file)

    with open('result.csv', 'w', encoding='utf-8') as file1:
        csv_file = csv.writer(file1, delimiter=',')
        csv_file.writerow(['category', 'products'])
        for line in json_file:
            if line['count'] >= args.count:
                csv_file.writerow([line['name'], line['count']])

    # отправка файла
    return send_file('result.csv', download_name='result.csv')

    # with open('result.json', encoding='utf-8') as file3:
    #     json_file = json.load(file3)
    #     return jsonify(json_file)


if __name__ == '__main__':
    app.run(host=args.adress, port=args.port)

    