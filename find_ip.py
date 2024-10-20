import maxminddb

with maxminddb.open_database('/home/amoraru/Documents/GitHub/CCS/databases/ip_to_country.mmdb') as reader:
    response = reader.get('193.142.201.214')
    print(response)