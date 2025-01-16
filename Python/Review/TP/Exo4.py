import ttkbootstrap as tb


class PCBuilder(tb.Window):
    def __init__(self):
        super().__init__()
        self.title("PC Cost Calculator")
        # creating the input frames
        self.mother_board_frame = tb.Frame(self)
        self.cpu_frame = tb.Frame(self)
        self.gpu_frame = tb.Frame(self)
        self.ram_frame = tb.Frame(self)
        self.brand_frame = tb.Frame(self)
        self.res_frame = tb.Frame(self)
        self.additional_frame = tb.Frame(self)
        self.categrory_frame = tb.Frame(self)
        self.output_frame = bt.Frame(self)
        # packing the frames    
        self.mother_board_frame.pack(padx= 10, pady=10)
        self.cpu_frame.pack(padx= 10, pady=10)
        self.gpu_frame.pack(padx= 10, pady=10)
        self.ram_frame.pack(padx= 10, pady=10)
        self.brand_frame.pack(padx= 10, pady=10)
        self.res_frame.pack(padx= 10, pady=10)
        self.additional_frame.pack(padx= 10, pady=10)
        self.categrory_frame.pack(padx= 10, pady=10)
        self.output_frame.pack(padx= 10, pady=10)

        # creating the variables
        self.mb_var = tb.DoubleVar()
        self.cpu_var = tb.DoubleVar()
        self.gpu_var = tb.DoubleVar()
        self.ram_var = tb.DoubleVar()
        self.brand_var = tb.DoubleVar()
        self.res_var = tb.DoubleVar()
        self.additional_var = tb.DoubleVar()
        self.categrory_var = tb.StringVar()
        self.output_var = tb.StringVar()


        self.create_widgets() # calling method to create widgets


    def create_widgets(self):
        mb_list = [
            ("ASUS", 100),
            ("Gigabyte", 120),
            ("MSI", 150)]
        cpu_list = [
            ("Intel i5", 200),
            ("Intel i7", 300),
            ("AMD Ryzen 5", 250),
        ]
        gpu_list = [
            ("Nvidia GTX 1660", 150),
            ("Nvidia RTX 3060", 500),
            ("AMD Radeon RX 6700", 400)
        ]
        ram_list = [
            ("8GB", 100),
            ("16GB", 200),
            ("32GB", 400)
        ]
        brand_list = [
            ("Dell", 800),
            ("HP", 700),
            ("Lenovo", 750)
        ]
        res_list = [
            ("1080p", 100),
            ("1440p", 200),
            ("4k", 500)
        ]
        additional_list = [
            ("Printer", 100),
            ("Bag", 50),
            ("Scanner", 80),
            ("Webcam", 40),
        ]
        