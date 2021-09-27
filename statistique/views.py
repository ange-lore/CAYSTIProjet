import sqlite3


# Function for Convert Binary Data
# to Human Readable Format
def convertToBinaryData(filename):
    # Convert binary format to images
    # or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(id, date,  photo):
    try:

        # Using connect method for establishing
        # a connection
        sqliteConnection = sqlite3.connect('SQLite_Retrieving_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # insert query
        sqlite_insert_blob_query = """ INSERT INTO statistique
                                  (id, date, photo) VALUES (?, ?)"""

        # Converting human readable file into
        # binary data
        empPhoto = convertToBinaryData(photo)

        # Convert data into tuple format
        data_tuple = (date, empPhoto)

        # using cursor object executing our query
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


insertBLOB(1,"2021/09/08", "E:\python\caysti\static\caysti\image\8-sept221.png")
#insertBLOB("David", "D:\Internship Tasks\GFG\images\person.png")