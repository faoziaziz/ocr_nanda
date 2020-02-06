#!/bin/python2
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
    init_x = None
    init_y = None
    Image = None
    Teks = None
    idFileTransferStage = None

    conn = None
    config = {
        'user':'IntanKW',
        'password':'IntanCantik',
        'host':'labseni.com',
        'port':'3306',
        'database':'Trumon'
    }


    def __INIT__(self, SeqNum, RefSN, ImageBlob):
        # Constructor for this class
        
        self.Image = ImageBlob
        self.Refsn = SeqNum
        self.idFileTransferStage = RefSN
        self.conn = mysql.connector.connect(**self.config)
        self.ImageTranslate()

    def ImageSave(self):
        print "image save"

    def ImageTranslate(self):
        # get file from filename

        # files = {'file': open('image/320220.png', 'rb')}
        files = {'file': self.Image}
        response = requests.post('https://api.ocr.proclubstudio.com/file', files=files)
        if response.status_code ==200:
            self.Teks=response.json()["result"]
            self.SaveTeksToTable()
            

            print `self.idFileTransferStage`+ " converted"
        else:
            print response.json()
            

        

    def SaveTeksToTable(self):
        # Save to teks
        curr = self.conn.cursor()
        print "SaveTeksToTable"
        query=(""" INSERT INTO `Teks`(`coloumn1`, `coloumn2`) VALUES (%s, %s)""")
        curr.execute(query, (self.RefSN, self.Teks))
        self.conn.commit()
        self.UpdateFlag()
        curr.close()

    def UpdateFlag(self):
        # update flag
        mycursor = self.conn.cursor()
        query = "UPDATE table SET FlagOCR =1 WHERE idFileTransferStage2 = '%s'"
        print "da"
        myscursor.execute(sql, (self.SeqNUM, ))
        self.conn.commit()
        self.UpdateFlag()
        mycursor.close()
        print "update flag"

    def __DEL__(self):
        print "Destruktor"
        del self.Image
        del self.idFileTransferStage
        del self.Teks



# Main program
config = {
    'user':'IntanKW',
    'password':'IntanCantik',
    'host':'labseni.com',
    'port':3306,
    'database':'Trumon'
}

conn = mysql.connector.connect(**config)
sql_get_query = """select * from Trumon.Image where FlagOCR='%s'""";
FlagOCR = 0
curr = conn.cursor()
curr.execute(sql_get_query,(FlagOCR, ))
rows = curr.fetchall()
for row in rows:
    # SeqNUM  ->
    # RefSN ->
    # ImageBlob ->
    SeqNUM =
    RefSN =
    ImageBlob =
    ocrnanda(SeqNUM, RefSN, ImageBlob)

curr.close()
conn.close()
