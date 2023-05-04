from Airline import Airline
from Aircraft import *
n = Aircraft()
m = Airline()
while True:
    z=int(input("ENTER YOUR ELECTION: "))
    if z == 1:
        m.AddAircraft()
    elif z == 2:
        n.ShowAircraft()



