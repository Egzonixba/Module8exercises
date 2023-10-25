
#1

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='theminons',
)


def fetch_airport():
    code = str(input("Insert the ICAO code of the airport: "))
    cursor = connection.cursor
    cursor.execute("SELECT name, municipality FROM airport where ident='" + code + "'")
    result = cursor.fetchall()

    if cursor.rowcount != 0:
        for row in result:
            print(code + ':', row[0] + ", located in", row[1])
    else:
        print("Airport code not in our system!")


#2
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='theminons',
)

area_code = input("Please enter the area code (e.g., FI): ")


mycursor = mydb.cursor()
mycursor.execute("SELECT type, count(*) as count FROM airports WHERE iso_country = %s GROUP BY type", (area_code,))
results = mycursor.fetchall()


if results:
    print(f"Airports in the country with area code {area_code}:")
    for result in results:
        airport_type, count = result
        print(f"{count} {airport_type} airports")
else:
    print("No airports found for the given area code.")


mydb.close()

#3

import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='dbuser',
    password='theminons',
)
)


icao_code1 = input("Please enter the ICAO code of the first airport: ")
icao_code2 = input("Please enter the ICAO code of the second airport: ")


mycursor = mydb.cursor()
mycursor.execute("SELECT latitude_deg, longitude_deg FROM airports WHERE ident = %s OR ident = %s", (icao_code1, icao_code2))
results = mycursor.fetchall()


if len(results) == 2:
    coords1 = (results[0][0], results[0][1])
    coords2 = (results[1][0], results[1][1])


    distance = geodesic(coords1, coords2).kilometers
    print(f"The distance between the two airports is approximately {distance:.2f} kilometers.")
else:
    print("One or both of the airports were not found in the database.")


mydb.close()
