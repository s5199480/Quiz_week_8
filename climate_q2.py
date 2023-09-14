import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


if __name__ == "__main__":
    cd = openpyxl.load_workbook("C:\Users\jessb\project_management\Quiz_week_8\climate.csv")
    print(wb.sheetnames)


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
plt.savefig("co2_temp_2.png") 

