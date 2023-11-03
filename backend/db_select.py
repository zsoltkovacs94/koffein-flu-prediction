import mysql.connector

# ez még csak a demora valami kezdetleges lekérdezés, lesz ez még szebb is (remélhetőleg)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="only4SOFT922mySQL",
    database="koffein"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM lekert_adatok"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)