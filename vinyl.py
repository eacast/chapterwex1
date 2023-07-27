"""
FileName: vinyl.py
Assignment: Record Store ch10_ex1
Author: Esgar Castro
abc123: fno202

Program Purpose: This program creates a class
that will hold data in relation to vinyls in stock.
The program will hold attributes for the 
Artist, Album Title, Stock number, and price of
each album.
"""

class vinyl:

    def __init__(self, artist, title, stock, price):
        self.__artist = artist
        self.__title = title
        self.__stock = stock
        self.__price = price

    def set_artist(self, artist):
        self.__artist = artist
        
    def set_title(self, title):
        self.__title = title
        
    def set_stock(self, stock):
        self.__stock = stock
        
    def set_price(self, price):
        self.__price = price
        
    def get_artist(self):
        return self.__artist
        
    def get_title(self):
        return self.__title
        
    def get_stock(self):
        return self.__stock
        
    def get_price(self):
        return self.__price

    def __str__(self):
        result = (f'Author:\t{self.get_artist()}\n') + \
                 (f'Title:\t{self.get_title()}\n') + \
                 (f'Stock:\t{str(self.get_stock())}\n') + \
                 (f'Price:\t${self.get_price():.2f}\n')
        return result