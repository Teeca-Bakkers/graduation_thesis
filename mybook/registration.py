#registration.py

import sys
import sqlite3
import qrcode
import existance
import add_tag
import qr_reader
import delete

def generator(c,title):
    c.execute("select book_num from bookshelf where book_title = ? ",(title,))
    num = c.fetchone()[0]
    num = str(num)
    img = qrcode.make(num)
    file_name = "shelf/book"+num+".png"
    img.save(file_name)
    print("QRcode was generated!")


def initialize(c):
    bookshelf_table = """create table bookshelf(
        book_num integer primary key,
        book_title text unique default null,
        author_name text default null,
        borrower_id int default null,
        transaction_situation int default 0,
        registration_time date default CURRENT_TIMESTAMP,
        lend_day date default null ,
        timedelta int default 0
        );"""

    tag_table = """create table tag(
        tag_num integer primary key,
        tag_name text unique default null,
        count int default 0
        );"""

    tag_map_table = """create table tag_map(
        master_id integer primary key,
        book_id int default null,
        tag_id int default null
        );"""
    
    c.execute(bookshelf_table) # <<< create index(id&name of owner&borrower) later
    c.execute(tag_table) 
    c.execute(tag_map_table) 
    c.execute("create index tag_desc on tag(count desc)") #desc means descending order

def registration(c):         
    title = input("book title (registration):")
    c.execute("select book_num from bookshelf where book_title = ? ",(title,))
    if  c.fetchone() is not None:
        print("This book is already registered...")
        sys.exit()
    author = input("author (registration):")
    c.execute("insert into bookshelf(book_title, author_name) values(?, ?)", (title, author))
    add_tag.add_tag(c,title)
    check = True
    while check == True:
        ans = input("More tags? yes >> 'y', no >> others ")
        if ans == 'y':
            add_tag.add_tag(c,title)
        else:
            check = False
    generator(c,title)
    
    for i in c.execute("select * from bookshelf"): #delete later
        print(i)
    
  
