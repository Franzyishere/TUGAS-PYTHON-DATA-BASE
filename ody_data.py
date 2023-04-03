#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[ ]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE TABLE Mahasiswa (    NIM VARCHAR(10) PRIMARY KEY,     Nama VARCHAR(30),     Alamat VARCHAR(255),     Matkul VARCHAR(10),     Jurusan VARCHAR(25) )")

cursorObject.execute("CREATE TABLE Dosen (    NIP VARCHAR(20) PRIMARY KEY,     Nama_Dosen VARCHAR(50),     Matkul VARCHAR(50),     Umur INT(3) )")

cursorObject.execute("CREATE TABLE MataKuliah (    Kode_Matkul VARCHAR(10) PRIMARY KEY,     Nama_Matkul VARCHAR(50),     Waktu DATE,     Ruangan VARCHAR(10),     Jurusan VARCHAR(25) )")

cursorObject.close()
dataBase.close()


# In[ ]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Matkul, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('V3922037', 'Fauzi', 'Madiun, 05', 'MK1', 'TI'),
    ('V67890154', 'Bagus', 'Madiun, 07', 'MK2', 'SI')
]

cursorObject.executemany(sql, val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[ ]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO Dosen (NIP, Nama_Dosen, Matkul, Umur) VALUES (%s, %s, %s, %s)"
val = [
    ('12345676745', 'Kelvin', 'MK1', 35),
    ('87654876556', 'Junardi', 'MK2', 38)
]

cursorObject.executemany(sql, val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[ ]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO mataKuliah (Kode_Matkul, Nama_Matkul, Waktu, Ruangan, Jurusan) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('MK1', 'Basis Data', '2023-04-01', 'A101', 'TI'),
    ('MK5', 'Pemrograman Web', '2023-04-05', 'A105', 'TI')
]

cursorObject.executemany(sql, val)

dataBase.commit()

cursorObject.close()
dataBase.close()


# In[ ]:


import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

cursorObject = dataBase.cursor()

sql = "SELECT Mahasiswa.NIM, Mahasiswa.Nama, MataKuliah.Nama_Matkul, Dosen.Nama_Dosen        FROM Mahasiswa        JOIN MataKuliah ON Mahasiswa.Matkul = MataKuliah.Kode_Matkul        JOIN Dosen ON MataKuliah.Kode_Matkul = Dosen.Matkul"

cursorObject.execute(sql)

result = cursorObject.fetchall()

for row in result:
    print("---------------------------")
    print("NIM             : ", row[0])
    print("NAMA            : ", row[1])
    print("MataKuliah      : ", row[2])
    print("Dosen Pengajar  : ", row[3])
    print("---------------------------")

cursorObject.close()
dataBase.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




