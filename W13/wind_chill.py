temperature = float(input('What is the temperature? '))
measurement = input('Fahrenheit or Celsius (F/C)? ')

final_temperature = 0

if measurement.lower() == 'f':
    final_temperature = temperature
else:
    final_temperature = (temperature * (9 / 5)) + 32

def get_wind_chill(speed):
    wind_chill = 35.74 + (0.6215 * final_temperature) - (35.75 * (speed ** 0.16)) + (0.4275 * final_temperature * (speed ** 0.16))
                # 35.74 + 0.6215T -                     35.75(V0.16) +              0.4275T(V0.16)
    return wind_chill

for num in range(1, 13):
    speed = num * 5
    wind_chill = get_wind_chill(speed)
    print(f'At temperature {final_temperature}, and wind speed {speed} mph, the windchill is: {wind_chill:.2f}F')