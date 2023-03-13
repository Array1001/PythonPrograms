import time

Length = int(input("Length(Meters): "))
Width = int(input("Width(Meters): "))
Depth = int(input("Depth(Meters): "))
WaterToTop = int(input("Water To Pool Top Distance: "))

ADJDEPTH = Depth-WaterToTop
VOLUME = Length*Width*ADJDEPTH

print(VOLUME, "Liters")

time.sleep(5)

