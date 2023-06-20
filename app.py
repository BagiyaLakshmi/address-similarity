import csv
from faker import Faker

fake = Faker()

with open('fake_addresses.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Street Address', 'City', 'State', 'Postal Code'])

    for _ in range(100):
        try:
            address = fake.address().split('\n')
            street_address = address[0]
            city_state_postal = address[1]
            city, state_postal = city_state_postal.split(',')
            state, postal_code = state_postal.strip().split()
            # country = address[2]

            writer.writerow([street_address, city, state, postal_code])
        except:
            pass


print("Fake addresses generated and saved to fake_addresses.csv")
