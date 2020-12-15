#add_tag.py
import sqlite3

def add_tag(c, title):
	tag_recommend(c)
	tag = input("tag (registration):")
	if len(tag) == 0:
		print("input tag you like")
		add_tag(c, title)
	c.execute("select tag_num from tag where tag_name = ? ",(tag,))
	if c.fetchone() is None:
		c.execute("insert into tag(tag_name) values(?)",(tag,))
	c.execute("select count from tag where tag_name = ?",(tag,))
	count = c.fetchone()[0]
	count += 1
	c.execute("update tag set count = ? where tag_name = ?",(count,tag))
	c.execute("select book_num from bookshelf where book_title = ?",(title,))
	book_num = c.fetchone()[0]
	c.execute("select tag_num from tag where tag_name = ?",(tag,))
	tag_num = c.fetchone()[0]
	c.execute("insert into tag_map(book_id,tag_id) values(?,?)",(book_num,tag_num))

def tag_recommend(c):
	c.execute("drop index tag_desc") 
	c.execute("create index tag_desc on tag(count desc)")
	c.execute("select tag_name from tag")
	tag_list = c.fetchall()
	TIME = 10 
	if len(tag_list) < TIME:
		TIME = len(tag_list)
	for i in range(TIME):
		print(tag_list[i][0])


		