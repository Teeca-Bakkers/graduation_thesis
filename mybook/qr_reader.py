#qr_reader.py

import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#adjust the contrast of QRcodes
def edit_contrast(image, gamma):
    look_up_table = [np.uint8(255.0 / (1 + np.exp(-gamma * (i - 128.) / 255.)))
        for i in range(256)]
    result_image = np.array([look_up_table[value] for value in image.flat], dtype=np.uint8)
    result_image = result_image.reshape(image.shape)
    return result_image

def qr_reader():
    #connect to camera
    cap_cam = cv2.VideoCapture(0)
    cv2.namedWindow('frame')

    #exit unless camera connects to
    if not cap_cam.isOpened():
        print("Cannot connect to camera...")
        sys.exit()

    while True:
        #capture frame by frame
        ret, frame = cap_cam.read() #ret >>> True of False, frame >>> detailed data
        #break if ret is False
        if not ret:
            print("Cannot recieve the frame.Now finished...")
            break

        #grayscalize and adjust the contrast
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = edit_contrast(gray_scale, 5)

        #display the frame as a result
        cv2.imshow('frame',gray_scale) #cv2.imshow(window's_name, img_itself)
        #break if anything is typed for "1" second
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        #get the frameQR from the edited image, and decode it
        codes = decode(image)

        if len(codes) > 0:
            output = codes[0][0].decode('utf-8', 'ignore')
            print("book_num:",output) #display the content of 'output'

            if 'output' != None:
                #cap_cam.read()
                cap_cam.release()

    #cap.release()
    cv2.destroyAllWindows()
    return output

   
    
#in the case using no camera
"""
from pyzbar.pyzbar import decode
from PIL import Image

def qr_reader(c):
    read_title = input("book title (scan):")
    c.execute("select book_num from bookshelf where book_title = ? ",(read_title,))
    read_num = str(c.fetchone()[0])
    read_img = "shelf/book"+read_num+".png"
    read_data = decode(Image.open(read_img))
    print(read_data[0][0].decode('utf-8', 'ignore'))
"""
