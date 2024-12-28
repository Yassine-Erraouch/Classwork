import ttkbootstrap as tb


class BillMaker(tb.Window):
    def __init__(self):
        super().__init__(themename="minty")
        self.title("Bill Maker")
        
        
        self.create_ui()
        
    def create_ui(self):
        self.entry_frame = tb.Frame(self)
        self.bill_frame = tb.Frame(self)