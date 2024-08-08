import SHT31,Display,time

while True:

    cTemp,fTemp,humidity =  SHT31.readBus()
    Display.display("Temp.: %.2f C" %cTemp,"RHum.: %.2f %%" %humidity)
    print("Temperature in Celsius is : %.2f C" %cTemp,"Relative Humidity is : %.2f %%RH" %humidity,sep="\n")
    time.sleep(1)
