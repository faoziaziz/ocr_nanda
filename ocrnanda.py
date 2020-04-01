#!/usr/bin/python2
#
# author      : Aziz Amerul Faozi
# description : This code will use for testing ocr
#
import os
import requests
import mysql.connector
import time
from mysql.connector import errorcode


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
    path = None

    conn = None
    config = {
        'user':'root',
        'password':'trumon123',
        'host':'127.0.0.1',
        'port':'3306',
        'database':'Trumon'
    }


    def __init__(self, SeqNum, DeviceID, RefSN, ImageBlob):
        # save image
        #
        #
        #
        # Constructor for this class
        self.path = "image/" + str(SeqNUM)+".png"
        self.DevID = DeviceID
        self.Image = ImageBlob
        self.RefSN = SeqNum
        self.idFileTransferStage = RefSN
        self.conn = mysql.connector.connect(**self.config)
        self.ImageSave()
        self.ImageTranslate()
        print "error"
 

    def ImageSave(self):
        fout = open(self.path, 'wb')
        fout.write(self.Image)
        fout.close()
       

    def ImageTranslate(self):
        # get file from filename

        files = {'file': open(self.path, 'rb')}
        #files = {'file': self.Image}
        response = requests.post('http://172.26.2.5:8000/file', files=files)
        if response.status_code ==200:
            self.Teks=response.json()["result"]
            self.SaveTeksToTable()

            print `self.idFileTransferStage`+ " converted"
        else:
            print "=================="
            print response.json()
            print "reconnect >>>"
            time.sleep(3)
            self.ImageTranslate()
            

        

    def SaveTeksToTable(self):
        # Save to teks
        curr = self.conn.cursor()
        print "SaveTeksToTable"
        query=(""" INSERT INTO `Teks`(`DeviceId`, `RefSN`, `Data`) VALUES (%s, %s, %s)""")
        curr.execute(query, (self.DevID, self.RefSN, self.Teks))
        self.conn.commit()
        self.UpdateFlag()
        curr.close()

    def UpdateFlag(self):
        # update flag
        mycursor = self.conn.cursor()
        query = "UPDATE Image SET Flag=1 WHERE SeqNum = '%s'"
        print "+= da =+"
        mycursor.execute(query, (self.RefSN, ))
        self.conn.commit()
        #self.UpdateFlag()
        mycursor.close()
        print "update flag"
        #os.remove("image/temp.png")

    def __del__(self):
        print "Destruktor"
        del self.Image
        del self.idFileTransferStage
       # del self.Teks



# Main program
config = {
    'user':'root',
    'password':'trumon123',
    'host':'127.0.0.1',
    'port':3306,
    'database':'Trumon'
}

conn = mysql.connector.connect(**config)
sql_get_query = """select * from Image where Flag='0'""";
curr = conn.cursor()
curr.execute(sql_get_query)
rows = curr.fetchall()
for row in rows:
    # SeqNUM  ->
    # RefSN ->
    # ImageBlob ->
    SeqNUM = row[0]
    print "SeqNUM "+`SeqNUM`
    DeviceID = row[1]
    
    RefSN = row[2]
    ImageBlob =row[3]
    
    ocrnanda(SeqNUM, DeviceID, RefSN, ImageBlob)

curr.close()
conn.close()
