#Product
Product=[
    {
        "id": 123,
        "name": "Libreta",
        "price": 12.500,
        "id_cat": 1
    },
    {
        "id": 111,
        "name": "Jabon ",
        "price": 10.500,
        "id_cat": 2
    }
]
#Category
Category=[
    {
        "id": 1,
        "name": "Utiles escolares",
    },
    {
        "id": 2,
        "name": "Aseo ",
    }
]

#Products_Categories
Products_Categories = []

for product in Product:
    for category in Category:
        if product['id_cat'] == category['id']:
            Products_Categories.append({
                'id': product['id'],
                'product name': product['name'],
                'category name': category['name']
            })

# Imprimir el diccionario de productos con categorías
for info in Products_Categories:
    print(f"ID: {info['id']}, Producto: {info['product name']}, Categoría: {info['category name']}")