#Understanding program for constructor
class laptop:
    def __init__(self):
        self.name=""
        self.processor=""
        self.chargertype=""
    def display(self):
        print("Name:",self.name)
        print("Processor:",self.processor)
        print("Chargertype:",self.chargertype)

dell=laptop()
dell.name="Dell"
dell.processor="i7"
dell.chargertype="C-type"
dell.display()



#Example2
class laptop:
    def __init__(self,name,processor,chargertype):
        self.name=name
        self.processor=processor
        self.chargertype=chargertype
    def display(self):
        print("Name:",self.name)
        print("Processor:",self.processor)
        print("Chargertype:",self.chargertype)

dell=laptop("Dell","i7","C-type")
dell.display()
