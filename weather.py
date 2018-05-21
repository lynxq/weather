import pyowm
import sys

city = input('В каком городе вас интересует погодные условия? : ')

owm = pyowm.OWM('c8be6c0b003cf8d53ccf10164fff8776' , language='ru')
try:
	observation = owm.weather_at_place(city)
except:
	a = print('Не корректно введено название города! Попробуйте ещё раз!')
	sys.exit()
	
		
w = observation.get_weather()

temperature = w.get_temperature('celsius')['temp']
detailed_status = w.get_detailed_status()

print('-------------------------------------------------------')
print('В городе "' + city + '" сейчас ' + str(temperature) + ' градусов по цельсию, ' + str(detailed_status))
print('-------------------------------------------------------')

if temperature <= 0 :
	print('Так, как температура меньше 0 градусов по цельсию, то есть шанс переохладить ваш организм. Одевайтесь теплее.')
	if temperature >= 0:
		print('Так, как температура на улице больше 0 градусов по цельсию, то можно идти гулять!')	
