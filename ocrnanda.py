#
# author      : Aziz Amerul Faozi
# description : This code will use for testing ocr
#

import requests
import mysql.connector
from mysql.connector import error


class ocrnanda:

    # Class Variable
    
    conn = None
    DevID = None
    Data = None
    RefSN = None
    SeqNUM = None
    init_x = None
    init_y = None

    conn = None
    config = {
        'user':'username',
        'password':'password',
        'host':'127.0.0.1',
        'port':'3306',
        'database':'database'
    }


    def __INIT__(self, x, y):
        self.init_x = x
        self.init_y = y
        self.conn = mysql.connector.connect(**self.config)
        

    def ImageImageSave(self):
        print "ImageSave"
        

    def ImageTranslate(self):
        # get file from filename
        print "ImageTranslate"

    def SaveTeksToTable(self):
        
        print "SaveTeksToTable"
        query=(""" INSERT INTO `Table`(`coloumn1`, `coloumn2`, `coloumn3`) VALUES (%s, %s, %s)""")
        # curr.execute(query, (self.VAL1, self.VAL2, self.VAL3))
        # self.conn.commit()
        # curr.close()

    def UpdateFlag():
        
        print "update flag"

    def __DEL__(self):
        print "Destruktor"



# Main program

        


        

        

url = "https://api.ocr.proclubstudio.com/file"

payload = {}
files = [
  ('file', open('/home/faoziaziz/github/OCR_nanda/image/320220.png','rb'))
]

#file2 = open('/home/faoziaziz/github/OCR_nanda/image/320220.png','rb')

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.post(url, 'multipart/form-data',  [('file', open('/home/faoziaziz/github/OCR_nanda/image/320220.png','rb'))])

print(response.text.encode('utf8'))
