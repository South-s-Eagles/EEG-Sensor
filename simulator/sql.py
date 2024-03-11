import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="SENSOR",
    user="urubu100",
    password="urubu100",
)


def insert_query(table: str, time: str, value: str):
    return f"""INSERT INTO {table} (time, microvolt) 
                           VALUES 
                           ({time}, {value}) """


def insert_value(time: str, value: str):
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query("electroencephalogram", time, value))
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into EEG table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into EEG table {}".format(error))
