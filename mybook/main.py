#main.py

import sqlite3
import qrcode
import registration
import existance
import qr_reader
import delete
import show
import transaction

conn = sqlite3.connect('bookshelf.db')
c = conn.cursor()

x = input("registration>>>r, show>>>s, delete>>>d, lend>>>l, return>>>ret, (init>>>i) ")

if x == 'r':
	registration.registration(c)
elif x == 's':
	show.show(c)
elif x == 'd':
	delete.delete(c)
elif x == 'l':
	transaction.lend_book(c)
elif x == 'ret':
	transaction.return_book(c)
elif x == 'i':
	registration.initialize(c)
else:
	print("Sorry, that key is not available.")

conn.commit()
conn.close()