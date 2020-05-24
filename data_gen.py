import csv
import random

from faker import Faker

seed = 42
Faker.seed(seed)
random.seed(seed)

fake = Faker()

with open('big_data.csv', 'w', encoding='utf-8') as csv_file:
    data_writer = csv.writer(csv_file, delimiter='|')

    header = ['transaction_dtm','bban','color','phone_number','lat','long','age']
    data_writer.writerow(header)

    for _ in range(1000):
        data = [fake.date_time().isoformat(), fake.bban(), fake.color_name(), fake.phone_number(), *fake.latlng(), random.randint(0,100)]
        data_writer.writerow([str(d) if not isinstance(d, str) else d for d in data])