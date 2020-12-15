#delete.py

import os
import sys
import existance

def delete(c): 
    book_title = input("book title (delete):")
    c.execute("select book_num from bookshelf where book_title = ? ",(book_title,))
    if c.fetchone() is None:
        print("The book doesn't exist...")
        sys.exit()
    agree = input("Are you sure you want to permanently delete the data?: Yes >>> y, No >>> others") 
    if agree != 'y':
        print("Interruption.")
        sys.exit()
    c.execute("select book_num from bookshelf where book_title = ? ",(book_title,))
    delete_num = c.fetchone()[0]
    delete_num_dum = delete_num
    delete_num = str(delete_num)
    delete_file_name = "shelf/book"+delete_num+".png"
    c.execute("delete from bookshelf where book_title = ?", (book_title,))
    c.execute("delete from tag_map where book_id = ?", (delete_num_dum,))
    if os.path.exists(delete_file_name) == False:
        print("The QRcode doesn't exist...")
        sys.exit()
    os.remove(delete_file_name)
    print("The registration and QRcode were deleted!")