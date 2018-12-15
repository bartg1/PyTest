# objective of class is to print inbound strings
class PrintWords():
    def __init__(self, text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        print('Construction Complete')
        
    #def PrintTexts(self, text1, text2, text3):
    def PrintTexts (self):
        print(self.text1 + " | " + self.text2 + " | " + self.text3)
        
    def UpdateTexts(self,text1b, text2b, text3b):
        self.text1 = text1b
        self.text2 = text2b
        self.text3 = text3b

#create a new MyClass"
ob = PrintWords('test1','test2','test3')

#Actions
ob.PrintTexts()
ob.UpdateTexts('Updated 1b', 'Updated 2b', 'Updated 3b')
ob.PrintTexts()