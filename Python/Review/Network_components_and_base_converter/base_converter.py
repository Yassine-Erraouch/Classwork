class Converter:
    def __init__(self, number):
        self.number = number
        

    def getBase(self):
        try: 
            base = ''
            if self.number.startswith("0b", "0B"):
                base = 2
            elif self.number.startswith("0o", "0O"):
                base = 8
            elif self.number.startswith("0x", "0X"):
                base = 16
            elif int(self.number):
                base = 10
            return base
        except:
            return "Invalid base"
            
    def convert(self, to_base):
        self.getBase()
        num = self.number
        num = num.lstrip("0b0B0o0O0x0X")

        num = int(num)
        output = ""
        if to_base == 2:
            output = bin(num)
        elif to_base == 8:
            output = oct(num)
        elif to_base == 10:
            output = num
        elif to_base == 16:
            output = hex(num)
        else:
            return f"Invalid destination base"
        return str(output)
            


if __name__ == "__main__":
    print("Testing the Converter class:")
    c1 = Converter("0b1010")
    print(c1.convert(10)) # should print 10
    c2 = Converter(10)
    print(c2.convert(2)) # should print 0b1010
    c3 = Converter("0o101")
    print(c3.convert(16)) # should print 0x5
    c4 = Converter(0x5)
    print(c4.convert(8)) # should print 0o5
    c5 = Converter(0x5)
    print(c5.convert(10)) # should print 5
