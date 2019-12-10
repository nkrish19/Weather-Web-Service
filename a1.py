# function to get weather response
def weather_response(location, API_key):
	"""This function takes in location and an API key as input.
	The location must be in the city list document available at openweathermap.org .
	Don't generate an API key more than once in ten minutes for good a response.
	A json string is returned as the output along with " b' " and " ' " in the beginning and the end of the string.
	"""
	import urllib.request
	url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
	url = str(url.read())
	return url
	#'url' is the json string

#Just to check the code
json = weather_response("Kathmandu","04fbff9be0357cbc962dd530a3a49bf1")
print ("json is",json)


# function to check for valid response 
def has_error(location,json):
	"""This function returns a value of True if the response city name and input location do not match in the json string.
	Else the program until now has been running succesfully.
	"""
	var1 = json.find('name')
	var2 = json.find('coord')
	city = json[var1+7:var2-3]
	if city == location :
		return False
	else:
		return True
	 
#Just to check the code
Error = has_error("Kathmandu",json)
print ('\n\nError is',Error)


# function to get attributes on nth day


#Temperature
def get_temperature (json, n, t):
	"""This function takes input of a json string, an integer 'n' which should lie between 0-4 and time 't' which should be in HH:MM"SS format.
	Only the following values of time are allowed: 03:00:00 , 06:00:00 , 09:00:00 , 12:00:00 , 15:00:00 , 18:00:00 , 21:00:00
	This function returns the temperature of nth day at tth time from current date.
	Temperature is in Kelvin.
	"""
	import datetime
	#Today is today's date
	if type(n) is int and type(t) is str and type(json) is str:
		Today = datetime.date.today()
		print ("\nToday\'s date is", Today)
		Delta = datetime.timedelta(days=n)
		#Date is the date we are checking
		Date = str(Today + Delta)
		print ("The date at which we are checking the attribute is", Date)
		print ("The time at which we are checking the attribute is", t)
		#Time is not the time at which we are checking
		Time = json.find(Date)
		#DatenTime is the final value whose index we are finding
		DatenTime = json.find(t, Time)
		#var is "temp" in json
		var = json.rfind("\"temp\"",0,DatenTime)
		temp = json[var+7:var+12]
		return float(temp)
	else:
		print ("Error. \nEnter correct input type")

#Just to check the code
Temp = get_temperature(json,4,"21:00:00")
print("\nTemperature is",Temp)


#Humidity
def get_humidity(json, n, t):
	"""This function takes input of a json string, an integer 'n' which should lie between 0-4 and time 't' which should be in HH:MM"SS format.
	Only the following values of time are allowed: 03:00:00 , 06:00:00 , 09:00:00 , 12:00:00 , 15:00:00 , 18:00:00 , 21:00:00
	This function returns the humidity of nth day at tth time from current date.
	Humidity is in percentage.
	"""
	import datetime
	if type(n) is int and type(t) is str and type(json) is str :
		Today = datetime.date.today()
		Delta = datetime.timedelta(days=n)
		Date = str(Today + Delta)
		Time = json.find(Date)
		DatenTime = json.find(t, Time)
		#var is the "humidity" in json
		var = json.rfind("\"humidity\"",0,DatenTime)
		humidity = json[var+11:var+13]
		return float(humidity)
	else:
		print ("Error. \nEnter correct input type")	
#Just to check the code
Humid = get_humidity(json,4,"21:00:00")
print ("Humidity is",Humid)


#Pressure
def get_pressure(json, n, t):
	"""This function takes input of a json string, an integer 'n' which should lie between 0-4 and time 't' which should be in HH:MM"SS format.
	Only the following values of time are allowed: 03:00:00 , 06:00:00 , 09:00:00 , 12:00:00 , 15:00:00 , 18:00:00 , 21:00:00
	This function returns the atmospheric pressure of nth day at tth time from current date.
	Pressure is in millibars.
	"""
	import datetime
	if type(n) is int and type(t) is str and type(json) is str :
		Today = datetime.date.today()
		Delta = datetime.timedelta(days=n)
		Date = str(Today + Delta)
		Time = json.find(Date)
		DatenTime = json.find(t, Time)
		#var is the "pressure" in json
		var = json.rfind("\"pressure\"",0,DatenTime)
		pressure = json[var+11:var+15]
		return float(pressure)
	else:
		print ("Error. \nEnter correct input type")	
#Just to check the code
Press = get_pressure(json,4,"21:00:00")
print ("Pressure is", Press)


#Wind
def get_wind(json, n, t):
	"""This function takes input of a json string, an integer 'n' which should lie between 0-4 and time 't' which should be in HH:MM"SS format.
	Only the following values of time are allowed: 03:00:00 , 06:00:00 , 09:00:00 , 12:00:00 , 15:00:00 , 18:00:00 , 21:00:00
	This function returns the wind speed of nth day at tth time from current date.
	The speed is in kilometers per hour.
	"""
	import datetime
	if type(n) is int and type(t) is str and type(json) is str :
		Today = datetime.date.today()
		Delta = datetime.timedelta(days=n)
		Date = str(Today + Delta)
		Time = json.find(Date)
		DatenTime = json.find(t, Time)
		#var is the "wind" in json
		var = json.rfind("\"wind\"",0,DatenTime)
		wind = json[var+16:var+17]
		return float(wind)
	else:
		print ("Error. \nEnter correct input type")
#Just to check the code
Wind = get_wind(json,4,"21:00:00")
print ("Wind speed is",Wind)


#Sea Level
def get_sealevel(json, n, t):
	"""This function takes input of a json string, an integer 'n' which should lie between 0-4 and time 't' which should be in HH:MM"SS format.
	Only the following values of time are allowed: 03:00:00 , 06:00:00 , 09:00:00 , 12:00:00 , 15:00:00 , 18:00:00 , 21:00:00
	"""
	import datetime
	if type(n) is int and type(t) is str and type(json) is str :
		Today = datetime.date.today()
		Delta = datetime.timedelta(days=n)
		Date = str(Today + Delta)
		Time = json.find(Date)
		DatenTime = json.find(t, Time)
		#var is the "sea level" in json
		var = json.rfind("\"sea_level\"",0,DatenTime)
		sl = json[var+12:var+16]
		return float(sl)
	else:
		print ("Error. \nEnter correct input type")
#Just to check the code
SeaL = get_sealevel(json,4,"21:00:00")
print ("Sea level is", SeaL)





