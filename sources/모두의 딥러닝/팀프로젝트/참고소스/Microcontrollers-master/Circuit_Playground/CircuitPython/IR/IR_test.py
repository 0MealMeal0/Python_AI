import board
import digitalio
import time
import pulseio
import adafruit_irremote
import neopixel
#import numpy as np

#MAX_THRESHOLD = 1000 ##Defined in routine check_IR_signals.py

##Let's make the function to compute the RMS
# def RMS(input_signal,avg_signal):
#     global MAX_THRESHOLD
#     ##Assuming both signals are the same and np arrays we should be able to do this
#     ##But they might not
#     if len(input_signal) != len(avg_signal):
#         return MAX_THRESHOLD*100.0
#     else:
#         return np.sum((input_signal-avg_signal)**2)/np.mean(avg_signal)

##Up Button Press
# def change_brightness():
#     global pixel_brightness
#     pixel_brightness+=0.05
#     if pixel_brightness > 0.25:
#         pixel_brightness = 0.0

##Right Button Press
def change_color():
    global COLORMODE,color
    COLORMODE+=1
    if COLORMODE == 0:
        color = (255,255,255)
    elif COLORMODE == 1:
        color = (255,0,0)
    elif COLORMODE == 2:
        color = (0,255,0)
    elif COLORMODE == 3:
        color = (0,0,255)
        COLORMODE = -1
    time.sleep(0.2)
    
def ResetPulses():
    global p
    p.clear()
    p.resume()
    
###Make the Button Press Averages
##Same signals from the Up Button
# up_button = np.asarray([[9130, 4478, 617, 548, 619, 545, 622, 544, 623, 540, 617, 548, 620, 544, 622, 545, 627, 535, 618, 1631, 624, 1625, 619, 1629, 616, 1636, 617, 1628, 617, 1632, 622, 543, 614, 1634, 620, 1628, 620, 548, 620, 1637, 603, 553, 614, 550, 618, 544, 623, 541, 616, 549, 618, 546, 621, 1628, 616, 553, 618, 1626, 624, 1625, 620, 1628, 616, 1633, 622, 1627, 616],
# [9129, 4483, 627, 538, 618, 546, 624, 544, 618, 544, 627, 537, 616, 549, 618, 550, 617, 544, 631, 1617, 620, 1628, 616, 1633, 621, 1632, 612, 1632, 623, 1626, 618, 547, 620, 1628, 617, 1632, 622, 542, 625, 1624, 621, 547, 620, 541, 616, 549, 622, 542, 621, 544, 623, 541, 616, 1633, 621, 545, 622, 1625, 623, 1626, 625, 1624, 622, 1627, 616, 1633, 621],
# [9129, 4483, 628, 537, 620, 549, 614, 546, 621, 543, 624, 541, 617, 548, 618, 546, 621, 544, 627, 1632, 609, 1629, 626, 1623, 620, 1629, 615, 1634, 620, 1629, 616, 549, 618, 1636, 619, 1626, 618, 547, 620, 1629, 616, 549, 618, 547, 620, 547, 620, 542, 630, 535, 621, 543, 620, 1629, 625, 540, 618, 1631, 623, 1626, 622, 1627, 623, 1626, 619, 1631, 624],
# [9096, 4518, 590, 574, 593, 573, 597, 567, 617, 548, 593, 581, 612, 544, 593, 572, 615, 550, 589, 1660, 623, 1626, 591, 1659, 627, 1622, 619, 1630, 624, 1626, 594, 570, 592, 1657, 588, 1662, 622, 543, 614, 1634, 592, 573, 593, 571, 619, 546, 598, 567, 652, 513, 622, 542, 595, 1655, 619, 546, 622, 1627, 597, 1653, 622, 1628, 616, 1635, 619, 1627, 618],
# [9098, 4515, 613, 551, 616, 548, 589, 576, 591, 574, 593, 572, 597, 567, 588, 577, 590, 575, 592, 1657, 588, 1665, 589, 1658, 587, 1663, 591, 1657, 587, 1662, 593, 572, 595, 1654, 620, 1629, 616, 549, 588, 1662, 593, 572, 615, 549, 618, 547, 620, 545, 592, 573, 595, 570, 597, 1657, 587, 574, 624, 1625, 619, 1631, 593, 1656, 620, 1630, 643, 1606, 618],
# [9108, 4515, 612, 548, 589, 576, 592, 574, 593, 571, 616, 549, 599, 566, 590, 576, 627, 537, 625, 1626, 590, 1663, 620, 1626, 589, 1662, 623, 1625, 622, 1633, 588, 572, 615, 1635, 620, 1630, 614, 550, 598, 1656, 588, 573, 624, 541, 616, 549, 588, 577, 621, 544, 593, 572, 595, 1657, 617, 546, 592, 1658, 596, 1654, 591, 1659, 595, 1654, 591, 1663, 621],
# [9125, 4492, 615, 549, 618, 545, 595, 570, 594, 571, 597, 568, 619, 546, 591, 579, 588, 577, 610, 1635, 625, 1627, 612, 1636, 589, 1661, 593, 1656, 589, 1664, 590, 573, 616, 1634, 619, 1631, 642, 525, 596, 1656, 591, 570, 624, 541, 619, 547, 616, 551, 616, 547, 620, 546, 594, 1658, 614, 549, 621, 1630, 621, 1629, 616, 1634, 620, 1630, 614, 1635, 589],
# [9103, 4513, 595, 581, 584, 570, 587, 578, 594, 571, 594, 575, 619, 543, 595, 570, 597, 568, 589, 1661, 605, 1645, 597, 1653, 592, 1658, 616, 1634, 590, 1660, 594, 571, 596, 1656, 588, 1661, 614, 551, 601, 1653, 586, 575, 592, 573, 614, 551, 596, 574, 613, 548, 619, 546, 593, 1657, 595, 571, 616, 1634, 591, 1659, 599, 1653, 588, 1661, 595, 1655, 597]])

##Let's also get an average of the pulses
# up_button_avg = np.mean(up_button,axis=0)

##Ok now let's do the same for the right button
# right_button = np.asarray([[9130, 4477, 615, 547, 621, 543, 627, 536, 617, 548, 618, 545, 622, 543, 624, 540, 617, 547, 620, 1628, 626, 1625, 618, 1626, 618, 1630, 624, 1624, 650, 1597, 619, 546, 619, 1629, 627, 536, 619, 1629, 624, 540, 617, 1631, 623, 541, 617, 547, 619, 546, 651, 513, 624, 1636, 608, 548, 619, 1624, 620, 545, 622, 1625, 619, 1629, 624, 1629, 645, 1597, 627],
# [9124, 4481, 615, 549, 619, 545, 591, 573, 624, 540, 616, 548, 622, 542, 622, 542, 595, 569, 618, 1634, 624, 1622, 588, 1657, 617, 1630, 623, 1625, 633, 1615, 619, 549, 614, 1629, 615, 549, 618, 1630, 623, 540, 617, 1633, 621, 541, 616, 549, 618, 546, 621, 543, 624, 1627, 617, 544, 623, 1625, 618, 546, 621, 1627, 617, 1630, 624, 1624, 620, 1627, 616],
# [9101, 4507, 592, 581, 582, 574, 593, 569, 588, 576, 590, 575, 592, 572, 595, 569, 600, 564, 592, 1656, 596, 1651, 626, 1626, 614, 1631, 593, 1653, 622, 1628, 595, 568, 589, 1658, 595, 569, 593, 1655, 628, 537, 596, 1651, 592, 573, 594, 569, 618, 546, 591, 573, 594, 1654, 590, 574, 594, 1653, 592, 573, 621, 1626, 588, 1660, 594, 1653, 590, 1658, 596],
# [9092, 4512, 585, 575, 592, 572, 614, 550, 617, 547, 590, 577, 633, 528, 596, 568, 619, 545, 592, 1656, 588, 1658, 596, 1655, 619, 1624, 620, 1628, 596, 1652, 591, 572, 595, 1655, 589, 573, 614, 1633, 595, 568, 594, 1653, 591, 573, 624, 540, 616, 548, 589, 575, 592, 1655, 618, 545, 622, 1626, 618, 547, 620, 1625, 590, 1658, 594, 1653, 621, 1626, 618],
# [9126, 4476, 615, 548, 619, 545, 622, 542, 617, 546, 618, 546, 621, 542, 624, 539, 622, 542, 621, 1626, 618, 1629, 625, 1624, 620, 1625, 618, 1629, 625, 1622, 622, 542, 625, 1622, 622, 544, 623, 1622, 625, 541, 613, 1636, 618, 542, 615, 548, 619, 545, 622, 542, 615, 1632, 625, 538, 616, 1631, 623, 541, 626, 1621, 622, 1625, 619, 1628, 626, 1621, 622],
# [9120, 4481, 625, 539, 618, 546, 621, 543, 624, 540, 617, 547, 620, 543, 628, 536, 616, 548, 619, 1628, 616, 1632, 622, 1625, 620, 1627, 616, 1631, 623, 1624, 620, 544, 623, 1625, 619, 544, 622, 1626, 627, 536, 622, 1626, 619, 545, 621, 542, 625, 539, 618, 546, 621, 1626, 618, 548, 620, 1626, 617, 547, 619, 1628, 616, 1631, 623, 1627, 617, 1628, 626],
# [9123, 4478, 617, 546, 626, 538, 614, 550, 597, 571, 616, 544, 623, 543, 613, 548, 592, 575, 619, 1629, 615, 1629, 614, 1634, 620, 1627, 617, 1639, 585, 1654, 620, 544, 623, 1627, 617, 544, 643, 1604, 620, 544, 626, 1622, 618, 546, 591, 573, 618, 545, 618, 548, 589, 1657, 624, 540, 620, 1627, 597, 567, 625, 1624, 594, 1651, 623, 1625, 619, 1628, 615],
# [9117, 4479, 617, 546, 621, 544, 593, 571, 615, 548, 621, 543, 592, 571, 596, 568, 589, 575, 592, 1655, 589, 1659, 615, 1633, 623, 1627, 585, 1660, 594, 1653, 621, 545, 592, 1653, 590, 573, 614, 1634, 620, 544, 594, 1654, 589, 574, 593, 571, 616, 549, 618, 545, 594, 1658, 613, 547, 590, 1656, 588, 576, 591, 1657, 597, 1650, 625, 1627, 586, 1662, 596],
# [9115, 4480, 596, 567, 620, 544, 593, 571, 595, 570, 587, 575, 622, 541, 615, 549, 588, 576, 593, 1660, 612, 1630, 601, 1646, 621, 1626, 618, 1629, 614, 1634, 621, 542, 594, 1653, 596, 568, 594, 1653, 624, 540, 594, 1653, 621, 543, 593, 570, 617, 546, 591, 573, 593, 1657, 617, 543, 614, 1633, 593, 571, 623, 1624, 620, 1627, 587, 1660, 624, 1624, 590],
# [9114, 4484, 591, 572, 615, 551, 586, 575, 621, 543, 614, 549, 620, 544, 591, 572, 594, 570, 587, 1660, 614, 1633, 621, 1626, 618, 1630, 593, 1653, 591, 1656, 621, 543, 591, 1656, 617, 546, 591, 1656, 591, 573, 590, 1657, 622, 542, 590, 573, 594, 572, 595, 569, 617, 1627, 591, 573, 590, 1656, 597, 567, 590, 1657, 597, 1653, 643, 1600, 591, 1660, 584],
# [9085, 4514, 592, 570, 587, 577, 623, 541, 593, 570, 596, 570, 587, 574, 593, 574, 613, 547, 590, 1658, 595, 1651, 593, 1654, 594, 1653, 602, 1645, 624, 1627, 587, 573, 593, 1654, 593, 575, 589, 1653, 620, 544, 593, 1658, 586, 574, 592, 571, 616, 547, 590, 574, 593, 1654, 591, 573, 592, 1655, 589, 575, 592, 1655, 589, 1658, 596, 1652, 591, 1655, 589]])

##Let's also get an average of the pulses
# right_button_avg = np.mean(right_button,axis=0)
 
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

#Set up pixels
pixel_brightness = 0.15
color = (255,255,255)
COLORMODE = 0
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=pixel_brightness)
pixels.fill(color)
pixels.show()

p = pulseio.PulseIn(board.REMOTEIN,maxlen=120,idle_state=True)
d = adafruit_irremote.GenericDecode()
ResetPulses()
while True:
    ##Wait for a signal or maybe just casually check. Not sure
    det = d.read_pulses(p)
    ##If we get a signal check to see what signal it is
    if det is not None:
        # if RMS(det,up_button_avg) < MAX_THRESHOLD:
        #     ##This is a up button press
        #     change_brightness()
        # elif RMS(det,right_button_avg) < MAX_THRESHOLD:
        #     ##This is a right button press
        #     change_color()
        #No matter what we want to Reset Pulses
        ResetPulses()
        #print(det) #only for debugging
        change_color() #only for debugging
     
    #Reset color and brightness
    pixels.brightness = pixel_brightness
    pixels.fill(color)
    pixels.show()
