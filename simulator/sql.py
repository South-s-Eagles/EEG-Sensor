import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="SENSOR",
    user="urubu100",
    password="urubu100",
)


def insert_query(nome_sensor : str, time: str, value: str):
    return f"""INSERT INTO algas (nome_sensor, `time`, microvolt) 
                           VALUES 
                           ("{nome_sensor}", "{time}", "{value}") """


def insert_value(nome_sensor : str, time: str, value: str):
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query(nome_sensor, time, value))
        connection.commit()
        print(cursor.rowcount, f"Record inserted successfully into {nome_sensor}")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into EEG table {}".format(error))
        print(error)
