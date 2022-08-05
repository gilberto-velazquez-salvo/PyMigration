
import mysql.connector
from mysql.connector import Error

import globalConfig

def getBasicInformation(query):
    try:
        connection = mysql.connector.connect(host=globalConfig.MYSQL_HOST,
                                            database=globalConfig.MYSQL_DATABASE,
                                            user=globalConfig.MYSQL_USER,
                                            password=globalConfig.MYSQL_PASS)
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
    getBasicInformation(globalConfig.BASIC_QUERIES["GetPlaftormExchange"])
