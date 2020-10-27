import pandas as pd

def cargar_json(file):
    df_books=pd.read_json(file)
    return df_books

def limpiar_stock(df_books):
    stock = df_books['stok'].tolist()
    stok_list = []

    for s in stock:
        aux1 = s.replace('\n', '')
        aux2 = aux1.replace('\t', '')
        aux1 = aux2.replace('available)', '')
        aux2 = aux1.replace('            In stock (', '')
        aux1 = aux2.replace('     ','')
        stok_list.append(aux1)

    return stok_list


def limpiar_value(df_books):
     value = df_books['value'].tolist()
     value_list = []

     for v in value:
         aux1 = v.replace('£','')
         value_list.append(aux1)

     return value_list


def clean_up():
    file = 'books.json'
    df_books = cargar_json(file)
    print(df_books)
    stock_limpio_list = limpiar_stock(df_books)
    value_limpio_list = limpiar_value(df_books)

    df = pd.DataFrame(
        {
            'title': df_books['title'],
            'value': value_limpio_list,
            'stock': stock_limpio_list
        }
    )
    df.to_json('books_l.json')


if __name__ == '__main__':
    clean_up()
    df = pd.read_json('books_l.json')
    print(df)













