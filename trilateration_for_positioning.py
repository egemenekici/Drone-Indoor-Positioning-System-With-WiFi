import matplotlib.pyplot as plt
import math

def getLocation(xA, yA, RSSI_A, xB, yB, RSSI_B, xC, yC, RSSI_C):

    #AP Device's coordinate and signal information.
    print ("1st AP Device's x-Axis, y-Axis (%d, %d) and RSSI (%d dBm) information" % (xA, yA, RSSI_A))
    print ("2nd AP Device's x-Axis, y-Axis (%d, %d) and RSSI (%d dBm) information" % (xB, yB, RSSI_B))
    print ("3rd AP Device's x-Axis, y-Axis (%d, %d) and RSSI (%d dBm) information" % (xC, yC, RSSI_C))

    #Determining the location of the devices with the x, y coordinates
    #and RSSI signal information of the WiFi sensors.
    A = xB*2 - xA*2
    B = yB*2 - yA*2
    C = RSSI_A**2 - RSSI_B**2 - xA**2 + xB**2 - yA**2 + yB**2
    D = xC*2 - xB*2
    E = yC*2 - yB*2
    F = RSSI_B**2 - RSSI_C**2 - xB**2 + xC**2 - yB**2 + yC**2

    #Getting x and y coordinates of WiFi Device.
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)
    print ("x-Axis and y-Axis of WiFi Device = (%.2f, %.2f)" % (x, y))

    #Distance between WiFi device and 1st AP Device. (in meter)
    Distance_XY1 = math.sqrt((xA - x)**2 + (yA - y)**2)
    print ("Distance of Wifi Device to 1st AP device : %.3f" % Distance_XY1, "meters")

    #Distance between WiFi device and 2nd AP Device. (in meter)
    Distance_XY2 = math.sqrt((xB - x)**2 + (yB - y)**2)
    print ("Distance of Wifi Device to 1st AP device : %.3f" % Distance_XY2, "meters")

    #Distance between WiFi device and 3rd AP Device. (in meter)
    Distance_XY3 = math.sqrt((xC - x)**2 + (yC - y)**2)
    print ("Distance of Wifi Device to 1st AP device : %.3f" % Distance_XY3, "meters")

    #AP Devices and WiFi device settings for pyplot.
    circleA = plt.Circle((xA, yA), 5, color='navy')
    circleB = plt.Circle((xB, yB), 5, color='navy')
    circleC = plt.Circle((xC, yC), 5, color='navy')
    circleA_Range = plt.Circle((xA, yA), RSSI_A, color='red')
    circleB_Range = plt.Circle((xB, yB), RSSI_B, color='green')
    circleC_Range = plt.Circle((xC, yC), RSSI_C, color='blue')
    circleX = plt.Circle((x, y), 5, color='gold')

    fig, ax = plt.subplots()

    #Grid Settings.
    ax.grid(True)
    ax.set_facecolor('#EBEBEB')
    ax.grid(which='major', color='white', linewidth=1.2)
    ax.grid(which='minor', color='white', linewidth=0.6)
    ax.set_xlim(-70, 250)
    ax.set_ylim(-70, 250)

    #Display AP Devices and WiFi device.
    ax.add_patch(circleA_Range)
    ax.add_patch(circleB_Range)
    ax.add_patch(circleC_Range)
    ax.add_patch(circleA)
    ax.add_patch(circleB)
    ax.add_patch(circleC)
    ax.add_patch(circleX)
    ax.annotate(text = 'AP1_Signal_Range', xy=(xA+5, yA+5), xycoords='data', color='navy')
    ax.annotate(text = 'AP2_Signal_Range', xy=(xB+5, yB+5), xycoords='data', color='navy')
    ax.annotate(text = 'AP3_Signal_Range', xy=(xC+5, yC+5), xycoords='data', color='navy')
    ax.annotate(text = 'wifi_device_name', xy=(x+3, y+3), xycoords='data', color='gold')

    #Display distance between WiFi device and 1st AP Device in meter.
    x1 = [xA, x]
    y1 = [yA, y]
    ax.plot(x1, y1, linestyle='--', marker='', color='navy')
    ax.annotate('AP1_Distance :', xy=(130, 230), xycoords='data', color='navy')
    ax.annotate(text = "%.3f" % Distance_XY1, xy=(200, 230), xycoords='data', color='navy')

    #Display distance between WiFi device and 2nd AP Device in meter.
    x2 = [xB, x]
    y2 = [yB, y]
    ax.plot(x2, y2, linestyle='--', marker='', color='navy')
    ax.annotate('AP2_Distance :', xy=(130, 210), xycoords='data', color='navy')
    ax.annotate(text = "%.3f" % Distance_XY2, xy=(200, 210), xycoords='data', color='navy')

    #Display distance between WiFi device and 3rd AP Device in meter.
    x3 = [xC, x]
    y3 = [yC, y]
    ax.plot(x3, y3, linestyle='--', marker='', color='navy')
    ax.annotate('AP3_Distance :', xy=(130, 190), xycoords='data', color='navy')
    ax.annotate(text = "%.3f" % Distance_XY3, xy=(200, 190), xycoords='data', color='navy')

    plt.show()

    """
    plt.show(block=False)
    plt.pause(1)
    plt.close()
    """

#Starting x, y coordinates and radius is the RSSI of beacon locations of circles.
#WiFi signals are automated.
xA = 30
yA = 130
RSSI_A = 70

xB = 30
yB = 10
RSSI_B = 80

xC = 150
yC = 30
RSSI_C = 100

#Simulate movement of an object by increasing or decreasing radius of the three WiFi sensors.
for i in range(1,20):
    RSSI_A+=4
    RSSI_B-=4
    RSSI_C-=4
    getLocation(xA, yA, RSSI_A, xB, yB, RSSI_B, xC, yC, RSSI_C)
    print ("i=",i)
