import matplotlib.pyplot as plt
connect = sqlite3.connect(climate.db)
cursr = connect.cursor()
cursr.execute("SELECT * FROM climate")

row = cursr.fetchall()

       
years = []
co2 = []
temp = []


for year,co,tem in row:
    years.append(year)
	co2.append(co)
	temp.append(tem)

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
