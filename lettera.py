#
class letter:
    def __init__(self,letterFrom,letterTo):
        self._letterFrom=letterFrom
        self._letterTo=letterTo
        self._line=""
    
    def addLine(self, line):
        self._line+="\n"+line


    def getText(self):
        return f"Dear {self._letterTo}:\n"+self._line+f"\n\nSincerely,\n\n{self._letterFrom}"


let=letter("Mary","Jonh Cena")  
let.addLine("I am sorry we must part.")
let.addLine("I wish you all the best.") 
print(let.getText())