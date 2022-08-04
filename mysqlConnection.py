
import mysql.connector
from mysql.connector import Error

import configuration

def getBasicInformation(query):
    try:
        connection = mysql.connector.connect(host=configuration.MYSQL_HOST,
                                            database=configuration.MYSQL_DATABASE,
                                            user=configuration.MYSQL_USER,
                                            password=configuration.MYSQL_PASS)
        if connection.is_connected():
            #db_Info = connection.get_server_info()
            #print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            return record

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    getBasicInformation(configuration.BASIC_QUERIES["GetPlaftormExchange"])
