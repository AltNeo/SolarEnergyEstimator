import json
import re
from urllib.request import urlopen


## IP Address
# To get coordinates
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
region= data["region"]
#print(region)


##Getting Data
formdata=[{"regionCode":"IND.1_1","code":"IND:IND.1_1","countryCode":"IND","name_en":"Andaman and Nicobar"},{"regionCode":"IND.2_1","code":"IND:IND.2_1","countryCode":"IND","name_en":"Andhra Pradesh"},{"regionCode":"IND.3_1","code":"IND:IND.3_1","countryCode":"IND","name_en":"Arunachal Pradesh"},{"regionCode":"IND.4_1","code":"IND:IND.4_1","countryCode":"IND","name_en":"Assam"},{"regionCode":"IND.5_1","code":"IND:IND.5_1","countryCode":"IND","name_en":"Bihar"},{"regionCode":"IND.6_1","code":"IND:IND.6_1","countryCode":"IND","name_en":"Chandigarh"},{"regionCode":"IND.7_1","code":"IND:IND.7_1","countryCode":"IND","name_en":"Chhattisgarh"},{"regionCode":"IND.8_1","code":"IND:IND.8_1","countryCode":"IND","name_en":"Dadra and Nagar Haveli"},{"regionCode":"IND.9_1","code":"IND:IND.9_1","countryCode":"IND","name_en":"Daman and Diu"},{"regionCode":"IND.10_1","code":"IND:IND.10_1","countryCode":"IND","name_en":"Goa"},{"regionCode":"IND.11_1","code":"IND:IND.11_1","countryCode":"IND","name_en":"Gujarat"},{"regionCode":"IND.12_1","code":"IND:IND.12_1","countryCode":"IND","name_en":"Haryana"},{"regionCode":"IND.13_1","code":"IND:IND.13_1","countryCode":"IND","name_en":"Himachal Pradesh"},{"regionCode":"IND.14_1","code":"IND:IND.14_1","countryCode":"IND","name_en":"Jammu and Kashmir"},{"regionCode":"IND.15_1","code":"IND:IND.15_1","countryCode":"IND","name_en":"Jharkhand"},{"regionCode":"IND.16_1","code":"IND:IND.16_1","countryCode":"IND","name_en":"Karnataka"},{"regionCode":"IND.17_1","code":"IND:IND.17_1","countryCode":"IND","name_en":"Kerala"},{"regionCode":"IND.18_1","code":"IND:IND.18_1","countryCode":"IND","name_en":"Lakshadweep"},{"regionCode":"IND.19_1","code":"IND:IND.19_1","countryCode":"IND","name_en":"Madhya Pradesh"},{"regionCode":"IND.20_1","code":"IND:IND.20_1","countryCode":"IND","name_en":"Maharashtra"},{"regionCode":"IND.21_1","code":"IND:IND.21_1","countryCode":"IND","name_en":"Manipur"},{"regionCode":"IND.22_1","code":"IND:IND.22_1","countryCode":"IND","name_en":"Meghalaya"},{"regionCode":"IND.23_1","code":"IND:IND.23_1","countryCode":"IND","name_en":"Mizoram"},{"regionCode":"IND.24_1","code":"IND:IND.24_1","countryCode":"IND","name_en":"Nagaland"},{"regionCode":"IND.25_1","code":"IND:IND.25_1","countryCode":"IND","name_en":"NCT of Delhi"},{"regionCode":"IND.26_1","code":"IND:IND.26_1","countryCode":"IND","name_en":"Odisha"},{"regionCode":"IND.27_1","code":"IND:IND.27_1","countryCode":"IND","name_en":"Puducherry"},{"regionCode":"IND.28_1","code":"IND:IND.28_1","countryCode":"IND","name_en":"Punjab"},{"regionCode":"IND.29_1","code":"IND:IND.29_1","countryCode":"IND","name_en":"Rajasthan"},{"regionCode":"IND.30_1","code":"IND:IND.30_1","countryCode":"IND","name_en":"Sikkim"},{"regionCode":"IND.31_1","code":"IND:IND.31_1","countryCode":"IND","name_en":"Tamil Nadu"},{"regionCode":"IND.32_1","code":"IND:IND.32_1","countryCode":"IND","name_en":"Telangana"},{"regionCode":"IND.33_1","code":"IND:IND.33_1","countryCode":"IND","name_en":"Tripura"},{"regionCode":"IND.34_1","code":"IND:IND.34_1","countryCode":"IND","name_en":"Uttar Pradesh"},{"regionCode":"IND.35_1","code":"IND:IND.35_1","countryCode":"IND","name_en":"Uttarakhand"},{"regionCode":"IND.36_1","code":"IND:IND.36_1","countryCode":"IND","name_en":"West Bengal"}]
regionlist={"Andaman and Nicobar":0,
"Andhra Pradesh":1,
"Arunachal Pradesh":2,
"Assam":3,
"Bihar":4,
"Chandigarh":5,
"Chhattisgarh":6,
"Dadra and Nagar Haveli":7,
"Daman and Diu":8,
"Goa":9,
"Gujarat":10,
"Haryana":11,
"Himachal Pradesh":12,
"Jammu and Kashmir":13,
"Jharkhand":14,
"Karnataka":15,
"Kerala":16,
"Lakshadweep":17,
"Madhya Pradesh":18,
"Maharashtra":19,
"Manipur":20,
"Meghalaya":21,
"Mizoram":22,
"Nagaland":23,
"NCT of Delhi":24,
"Odisha":25,
"Puducherry":26,
"Punjab":27,
"Rajasthan":28,
"Sikkim":29,
"Tamil Nadu":30,
"Telangana":31,
"Tripura":32,
"Uttar Pradesh":33,
"Uttarakhand":34,
"West Bengal":35}
statecode=regionlist[region]
codedic=formdata[statecode]
regioncode=codedic["regionCode"]
#print(regioncode)


##Actually Pulling Data
url="https://api.globalsolaratlas.info/country/IND/"+regioncode
response=urlopen(url)
data=json.load(response)

s1=(data["dataset"])
s2=s1["solar"]
s3=s2["data"]
s4=s3["PVOUT_median"]
s4=int(s4)

energyThatCanBeProd = "Energy that can be produced at your location: " + str(s4) + "kWh/ sq meter\n"   #CHANGED

# INPUT
#area=int(input("Enter area you wish to apply solar panels to (in meter square) "))

#power=s4*area*10*0.7

#ALL OF THE FOLLOWING LINES WERE TOUCHED
#output1 = "Calculations are done considering that your location gets 10 Hrs of Sunlight and a power conversion factor of 0.7\n" + "Total Energy Produced in one day= " + power + "kWh\n" + "An average household consumes 206 KWh per day (according to statista.com , refer to documentation for more info)"

#powerleft=power-206

#output2 = "After household consumption, energy left= " + power-206 + "kWh\n" + "This much energy is enought to run a fan and a lightbulb for " + ((powerleft*1000)/100) + "hrs\n" + "Or at rate of ₹3 per unit buyback offered by the government, you can earn ₹" + powerleft*3 + " per day\n" + "Or ₹",int(powerleft*90)," per month"