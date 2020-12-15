#transaction.py
import sqlite3
import sys
import datetime

def lend_book(c):
	title = input("Book:")
	c.execute("select book_title from bookshelf where book_title = ?", (title,))
	if c.fetchone()[0] is None:
		print("The book is not registered...")
		sys.exit()
	borrower_id = input("Borrower's id: ")
	timedelta = input("How long will you lend the book? ")
	c.execute("update bookshelf set transaction_situation = ? where book_title = ?",(1, title))
	c.execute("update bookshelf set borrower_id = ? where book_title = ?",(borrower_id, title))
	c.execute("update bookshelf set lend_day = CURRENT_TIMESTAMP where book_title = ?",(title,))
	c.execute("update bookshelf set timedelta = ? where book_title = ?",(timedelta, title))
	print("Setteing Completed")

def return_book(c):
	title = input("Book: ")
	c.execute("select book_title from bookshelf where book_title = ?", (title,))
	if c.fetchone()[0] is None:
		print("The book is not registered...")	
		sys.exit()
	c.execute("update bookshelf set transaction_situation = ? where book_title = ?",(0, title))
	c.execute("update bookshelf set borrower_id = ? where book_title = ?",(0, title))
	c.execute("update bookshelf set lend_day = CURRENT_TIMESTAMP where book_title = ?", (title,))
	c.execute("update bookshelf set timedelta = ? where book_title = ?",(0, title))
	print("Return Completed")

