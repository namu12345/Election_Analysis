#counties_tuple = ("Arapahoe","Denver","Jefferson")
#print(counties_tuple)
#print(counties_tuple[:2])
#print(counties_tuple[:-1])

#counties = ["Arapahoe","Denver","Jefferson"]
#print(counties)
#if counties[1] == 'Denver' :

# print(counties[1])




#for county in counties:
 #   print(county)

#numbers = [0,1,2,3,4,5]
#for num in numbers:
 #   print(num)

#for i in range(len(counties)):
 #   print(counties[i])

counties_dict = {"Arapahoe": "422829", "Denver": "463353", "Jefferson": "432438"}

#for county in counties_dict :
    #print(county)

#for county in counties_dict.keys():
    #print(county)

print("****************************")
#counties_dict = {}
#counties_dict["Arapahoe"] = '422829'
#print(counties_dict)
#print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.get("Denver"))


#print("Arapahoe"+":"+counties_dict.get("Arapahoe"))

#for key,value in counties_dict.items():
    #print(key +"  "+value)

#for key in counties_dict.keys():
    #print(key +"  "+counties_dict.get(key))   

students_dict = {"namrata" : 12, "Hemant": 25, "Aarna":28}

print(students_dict.get("namrata"))
print(students_dict.values())
print(students_dict.items())
print(students_dict)

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)
print(len(voting_data))

for key,value in counties_dict.items():
    print(f"{key} has {value} registered voters.")

num = int(1)

while num<10 :
    print(num)
    num = num+1


for county_dict in voting_data :
    for key,value in county_dict.items():
        print(key,value)



import datetime as dt
now = dt.datetime.now()
print("The time right now is ", now)

dir(counties_dict)
# dir({"Arapahoe": "422829", "Denver": "463353", "Jefferson": "432438"})
print(dir)







   