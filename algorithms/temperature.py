"""  To the Util Class add temperature Conversion static function, given the
     temperature in fahrenheit as input outputs the temperature in Celsius or viceversa using the formula
     Celsius to Fahrenheit:   (°C × 9/5) + 32 = °F
     Fahrenheit to Celsius:   (°F − 32) x 5/9 = °C"""


from UtilityMethods import Utility


cel = float(input("enter the Celsius value \n"))
Utility.temp(cel)
