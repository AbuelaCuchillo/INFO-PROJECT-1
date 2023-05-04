class Airline:
    def __init__(self):
        self.a = []
        self.ac = []
        self.f = []
        self.A1 = []
    def AddAircraft(self):
        self.CALLSIGN = str(input("ENTER THE AIRCRAFT'S CALLSIGN: "))
        self.TYPE = str(input("ENTER THE AIRCRAFT'S TYPE: "))
        self.MAXCAP = int(input("ENTER THE MAXIMUM CAPACITY: "))
        self.A1 = [self.CALLSIGN,self.TYPE,self.MAXCAP]
        self.a.append(self.A1)


