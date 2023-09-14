import matplotlib.pyplot as plt
import sqlite3

def printRes(r):
    for l in r:
        print(l)
    print()

if __name__ == "__main__":
    connection = sqlite3.connect(r"C:\Users\jessb\project_management\Quiz_week_8\climate.db")
    cursor = connection.cursor()

    sql_cmd = """
    SELECT name FROM sqlite_master WHERE type='table';
    """
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    print(res)

    for table_info in res:
        table_name = table_info[0]
        sql_cmd = f"""
        SELECT * FROM {table_name}
        """
        cursor.execute(sql_cmd)
        column_names = sqlite3.Row(cursor,(1,)).keys()
        print(f'{table_name}: {column_names}')
    print()

    sql_cmd = """
    SELECT Year FROM ClimateData;
    """
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    printRes(res)

    sql_cmd = """
        SELECT CO2 FROM ClimateData;
        """
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    printRes(res)

    sql_cmd = """
        SELECT Temperature FROM ClimateData;
        """
    cursor.execute(sql_cmd)
    res = cursor.fetchall()
    printRes(res)





            
years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
