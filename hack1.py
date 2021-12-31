class House:
    type = "особняк"
    area = 30
    def __init__(self, bedroom, garderob, chair):
        self.bedroom = 4
        self.garderob = 2
        self.chair = 1.5
    def furniture (self):
        print("спальня",{self.bedroom}, "гардероб" ,{self.garderob},'стол',{self.chair})
        print('оставщаяся площадь',self.area - self.bedroom - self.chair - self.garderob)
        print('общая площадь',self.area)
        print('тип дома',self.type)

s = House('4m2','2 m2','1,5 m2')
s.furniture()