import pyodbc
print("About to insert Hagi:")
#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn = pyodbc.connect(
    'DRIVER={FreeTDS};SERVER=**;PORT=**;DATABASE=**;UID=**;PWD=**', autocommit=True)
cur = conn.cursor()
#This is just an example
cur.execute(
    f"INSERT INTO [FootballPLayers] ([Name],[Age],[Job],[Country],[Married],[YearsEmployed]) VALUES ('Gheorghe Hagi','55','Manager','Romania','Y','6')")
conn.commit()
print('Should have inserted Hagi')
cur.close()
conn.close()