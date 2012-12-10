from Tkinter import *

class GUI(object):
    def __init__(self):
        self.active = False
        self.command = 'stop'
        self.setup()

    def move(self, code, value):
        self.command = 'C'+str(code)+value
        print self.command

    def start(self):
        if  self.throttle.get()==0:
            self.active = True
            for c in self.controls:
                c.configure(state = 'normal')
                c.set(0)
            print 'started'

    def stop(self):
        self.active = False
        print 'stopped'
        self.command= 'stop'

    def key(self,event):
        print 'up'

    def setup(self):
        root = Tk()

        #bindings
        root.bind("w", self.key)
        root.bind("a", self.key)
        root.bind("s", self.key)
        root.bind("d", self.key)

        root.bind("<Up>", self.key)
        root.bind("<Left>", self.key)
        root.bind("<Right>", self.key)
        root.bind("<Down>", self.key)

        root.bind("<Escape>", self.key)

        #wigets:
        sidebar_bg = '#228800'

        title = Label(text="PiQuopter", background="#554400",  font=("Helvetica", "16"))

        leftbar = Frame(bg = sidebar_bg, bd=0)
        start = Button(leftbar, text = 'start', command=lambda: self.start())
        self.throttle = Scale(leftbar, variable=IntVar(), orient='vertical', length=200,from_=100, to=0, bg = sidebar_bg, bd=0, tickinterval=5, state='disabled', command=lambda(x): self.move(0,x))
        self.yaw = Scale(leftbar, variable=IntVar(), orient='horizontal', length=200,from_=-50, to=50, bg = sidebar_bg, tickinterval=5, state='disabled',command=lambda(x): self.move(1,x))

        screen = Canvas(width=320, height=240)
            # add canvasy stuff


        rightbar = Frame(background=sidebar_bg)
        stop = Button(rightbar, text='stop', command=lambda: self.stop())
        self.pitch = Scale(rightbar, variable=IntVar(), orient='vertical', length=200,from_=-50, to=50, bg = sidebar_bg, tickinterval=5, state='disabled', command=lambda(x): self.move(2,x))
        self.roll = Scale(rightbar, variable=IntVar(), orient='horizontal', length=200,from_=-50, to=50, bg = sidebar_bg, tickinterval=5, state='disabled', command=lambda(x): self.move(3,x))

        self.controls = [self.throttle, self.yaw, self.pitch, self.roll]
        #placing:
        title.grid(row=0, column=0, columnspan=3, sticky=E+W)

        leftbar.grid(row=1, column=0, sticky=N+S)
        start.pack(fill='both')
        self.throttle.pack(fill='x')
        self.yaw.pack()

        screen.grid(row = 1, column = 1)

        rightbar.grid(row=1, column=2, sticky=N+S)
        stop.pack(fill='x')
        self.pitch.pack()
        self.roll.pack()

        root.mainloop()


gui = GUI()








