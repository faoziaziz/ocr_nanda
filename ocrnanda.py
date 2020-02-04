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


    def __INIT__(self, SeqNum, DeviceID, RefSN, ImageBlob):
        # Constructor for this class
        self.DevID = DeviceID
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
            print "=================="
            print response.json()
            

        

    def SaveTeksToTable(self):
        # Save to teks
        curr = self.conn.cursor()
        print "SaveTeksToTable"
        query=(""" INSERT INTO `Teks`(`DeviceId`, `RefSN`, `Data`) VALUES (%s, %s, %s)""")
        curr.execute(query, (self.DeviceId, self.RefSN, self.Teks))
        self.conn.commit()
        self.UpdateFlag()
        curr.close()

    def UpdateFlag(self):
        # update flag
        mycursor = self.conn.cursor()
        query = "UPDATE Image SET Flag=1 WHERE SeqNum = '%s'"
        print "+= da =+"
        myscursor.execute(sql, (self.RefSN, ))
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
    SeqNUM = row[0]
    DeviceID = row[1]
    RefSN = row[2]
    ImageBlob =row[3]
    
    ocrnanda(SeqNUM, DeviceID, RefSN, ImageBlob)

curr.close()
conn.close()
