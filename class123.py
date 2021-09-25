class car(object):
    def __init__(self, model, color, company, speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit


    def start(self):
        print ('starter')

    def stop(self):
        print ('stop')

audi = car ('asics', 'red', 'audi', '100')
print (audi.start())
