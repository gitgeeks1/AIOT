import serial
from time import sleep
import webbrowser
import sys

def GPS_Info():
	global NMEA_buff
	global lat_in_degrees
	global long_in_degrees
	nmea_time=[]
	nmea_latitude=[]
	nmea_longitude=[]
	nmea_time=NMEA_buff[0]
	nmea_latitude=NMEA_buff[1]
	nmea_longitude=NMEA_buff[3]
	
	nmea_latitude=1905.1535
	nmea_longitude=7305.0250
	
	print("NMEA Time : ", nmea_time)
	print("Latitude : ", nmea_latitude, "Longitude : ", nmea_longitude)
	
	lat=float(nmea_latitude)
	longi=float(nmea_longitude)
	
	
	lat_in_degrees=convert_to_degrees(lat)
	long_in_degrees=convert_to_degrees(longi)
	

def convert_to_degrees(raw_value):
	decimal_value=raw_value/100.00
	degrees=int(decimal_value)
	mm=(decimal_value - int(decimal_value))/0.6
	pos= degrees + mm
	pos= "%.4f"%(pos)
	return pos
	
gp_info="$GPGGA"
ser=serial.Serial("/dev/ttyS0")
GPGGA_buffer=0
NMEA_buff=0
lat_in_degrees=0
long_in_degrees=0

try:
	while True:
		received_data=(str)(ser.readline())
		GPGGA_data_available=received_data.find(gp_info)
		if(GPGGA_data_available>0):
			GPGGA_buffer=received_data.split("$GPGGA,",1)[1]
			NMEA_buff=(GPGGA_buffer.split(','))
			GPS_Info()
			
			print("LAT in degrees : ", lat_in_degrees, "Long in Degrees :", long_in_degrees)
			map_link='https://maps.google.com/?q=+' +lat_in_degrees+','+long_in_degrees
			print("<<< PRESS CTRL+C to plot location >>>>")
			print("------------")
			
except KeyboardInterrupt:
	webbrowser.open(map_link)
	sys.exit(0)
