#!/usr/bin/python2

import gtk

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Calculator")
        self.set_size_request(250, 230)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.entry_result = gtk.Entry()

        vbox = gtk.VBox(False, 2)

        table = gtk.Table(5, 4, True)

        #Define all the buttons

        button_cls = gtk.Button("Cls")
        button_cls.connect("clicked", lambda a: self.entry_result.set_text(""))

        button_bck = gtk.Button("bck")
        button_bck.connect("clicked", lambda a: self.entry_result.set_text(self.entry_result.get_text()[:len(self.entry_result.get_text())-1]))
        button_label = gtk.Label()

        button_close = gtk.Button("Close")
        button_close.connect("clicked", lambda a: gtk.main_quit())
        button_7 = gtk.Button("7")
        button_7.connect("clicked", self.num_button_pressed, "7")
        button_8 = gtk.Button("8")
        button_8.connect("clicked", self.num_button_pressed, "8")

        button_9 = gtk.Button("9")
        button_9.connect("clicked", self.num_button_pressed, "9")

        button_slash = gtk.Button("/")
        button_slash.connect("clicked", self.num_button_pressed, " / ")

        button_4 = gtk.Button("4")
        button_4.connect("clicked", self.num_button_pressed, "4")
        
        button_5 = gtk.Button("5")
        button_5.connect("clicked", self.num_button_pressed, "5")
        
        button_6 = gtk.Button("6")
        button_6.connect("clicked", self.num_button_pressed, "6")

        button_star = gtk.Button("*")
        button_star.connect("clicked", self.num_button_pressed, "*")

        button_1 = gtk.Button("1")
        button_1.connect("clicked", self.num_button_pressed, "1")

        button_2 = gtk.Button("2")
        button_2.connect("clicked", self.num_button_pressed, "2")

        button_3 = gtk.Button("3")
        button_3.connect("clicked", self.num_button_pressed, "3")

        button_minus = gtk.Button("-")
        button_minus.connect("clicked", self.num_button_pressed, " - ")

        button_0 = gtk.Button("0")
        button_0.connect("clicked", self.num_button_pressed, "0")

        button_dot = gtk.Button(".")
        button_dot.connect("clicked", self.num_button_pressed, ".")

        button_equals = gtk.Button("=")
        button_equals.connect("clicked", lambda a: self.entry_result.set_text(str(eval(self.entry_result.get_text()))))

        button_plus = gtk.Button("+")
        button_plus.connect("clicked", self.num_button_pressed, "+")


        table.attach(button_cls, 0, 1, 0, 1)
        table.attach(button_bck, 1, 2, 0, 1)
        table.attach(button_label, 2, 3, 0, 1)
        table.attach(button_close, 3, 4, 0, 1)

        table.attach(button_7, 0, 1, 1, 2)
        table.attach(button_8, 1, 2, 1, 2)
        table.attach(button_9, 2, 3, 1, 2)
        table.attach(button_slash, 3, 4, 1, 2)

        table.attach(button_4, 0, 1, 2, 3)
        table.attach(button_5, 1, 2, 2, 3)
        table.attach(button_6, 2, 3, 2, 3)
        table.attach(button_star, 3, 4, 2, 3)

        table.attach(button_1, 0, 1, 3, 4)
        table.attach(button_2, 1, 2, 3, 4)
        table.attach(button_3, 2, 3, 3, 4)
        table.attach(button_minus, 3, 4, 3, 4)

        table.attach(button_0, 0, 1, 4, 5)
        table.attach(button_dot, 1, 2, 4, 5)
        table.attach(button_equals, 2, 3, 4, 5)
        table.attach(button_plus, 3, 4, 4, 5)

        self.entry_result.set_size_request(30,40)
        vbox.pack_start(self.entry_result, False, False, 0)
        vbox.pack_end(table, True, True, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
    def num_button_pressed(self, button, data=None):
        self.entry_result.insert_text(data, len(self.entry_result.get_text()))

PyApp()
gtk.main()
