PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

products_name = PRICE_LIST.split()[::2]
products_price = [int(x.strip('р')) for x in PRICE_LIST.split()[1::2]]
new_list = dict(zip(products_name, products_price))

print(new_list)
