#show.py

import sys
import existance
import qr_reader
import url_check

def show(c):
	num = qr_reader.qr_reader()
	c.execute("select book_title from bookshelf where book_num = ? ",(num,))
	if c.fetchone() is None:
		print("This QRcode is not for a book...")
		sys.exit()
	url_check.url_check(num) #<<< url_check
	c.execute("select book_title from bookshelf where book_num = ? ",(num,))
	title = c.fetchone()[0]
	c.execute("select author_name from bookshelf where book_num = ? ",(num,))
	author = c.fetchone()[0]
	print("title:",title," author:",author)
	c.execute("select tag_id from tag_map where book_id = ? ",(num,))
	tag_num = c.fetchall()
	for i in tag_num:
		c.execute("select tag_name from tag where tag_num = ? ",(i[0],))
		print("tag:", c.fetchone()[0])
	  	