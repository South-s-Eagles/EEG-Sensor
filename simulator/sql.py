import mysql.connector


def insert_query(table: str, time: str, value: str):
    return f"""INSERT INTO {table} (time, value) 
                           VALUES 
                           ({time}, {value}) """


try:
    connection = mysql.connector.connect(
        host="localhost",
        database="ivan_docker",
        user="docker_ivan",
        password="dockerzinho",
    )

    cursor = connection.cursor()
    cursor.execute(insert_query("EEG", "2323", "23"))
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into EEG table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into EEG table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
