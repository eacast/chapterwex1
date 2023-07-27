"""
FileName: ch10_ex1.py
Assignment: Record Store
Author: Esgar Castro
abc123: fno202

Program Purpose: This program import class "vinyl".
The program will take the atributes from that class and
create the objects and print the resluts for 
Artist, Album Title, Stock number, and price of
each album.
"""

import vinyl

def main():
    """
    This is the main function, where the primary code
    for your program will reside.  You shoud update this
    docstring to reflect the purpose of the main function.
    Note that everything inside of the main 'code block'
    is indented.
    All of the code is for demo purposes. It should all be
    deleted and replaced with your code.
    """

    arctic_monkeys = ("Arctic Monkeys", "AM", 12, 17.79)
    lana_del_rey = ("Lana Del Rey", "Born To Die", 21, 16.62)
    neutral_milk_hotel = ("Neutral Milk Hotel", "In The Aeroplane Over the Sea", 1, 14.99)
    bon_iver = ("Bon Iver", "For Emma, Forever Ago", 5, 19.01)
    pixies = ("Pixies", "Doolittle", 13, 23.98)

    print('Record Store Item 1:')
    print(f'Artist: {arctic_monkeys.get_artist()}')
    print(f'Title: {arctic_monkeys.get_title()}')
    print(f'Stock: {arctic_monkeys.get_stock()}')
    print(f'Price: {arctic_monkeys.get_price()}')

    print('Record Store Item 2:')
    print('Artist: {lana_del_rey.artist}')
    print('Title: {lana_del_rey.title}')
    print('Stock: {lana_del_rey.stock}')
    print('Price: ${lana_del_rey.price}')

    print('Record Store Item 3:')
    print('Artist: {neutral_milk_hotel.artist}')
    print('Title: {neutral_milk_hotel.title}')
    print('Stock: {neutral_milk_hotel.stock}')
    print('Price: ${neutral_milk_hotel.price}')

    print('Record Store Item 4:')
    print('Artist: {bon_iver.get_artist}')
    print('Title: {bon_iver.get_title}')
    print('Stock: {bon_iver.get_stock}')
    print('Price: ${bon_iver.get_price}')

    print('Record Store Item 5:')
    print('Artist: {pixies.get_artist}')
    print('Title: {pixies.get_title}')
    print('Stock: {pixies.get_stock}')
    print('Price: ${pixies.get_price}')

if __name__ == '__main__':
    main()