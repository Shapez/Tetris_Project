# tetrous.py
#wx.TextCtrl parameters are parent, id, value, pos size, style
import wx  #All functions and objects from the basic modules will start with a wx.

APP_EXIT = 1 #

class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()

class tetrous(wx.Frame):    #all widgets belong in this class aside from another frame or dialogue boxes

    def __init__(self, parent, *args, **kwargs):
        super(MyPopupMenu, self).__init__()

    def __init__(self, parent, title, *args, **kwargs):
        super(tetrous, self).__init__(parent, title=title,
            size=(500, 800), *args, **kwargs)
        self.Centre()
        self.Show()     #self = wx.
        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT) #new
        font.SetPointSize(9)

        vbox1 = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        tctrl = wx.TextCtrl(panel, pos=(35, 510), size =(415, 150) ) #changed recently
        hbox1.Add(tctrl, proportion = 1)
        vbox1.Add(hbox1, flag = wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border = 10) #controls size of distance between widge

        vbox1.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        vbox1.Add(hbox2, flag = wx.LEFT | wx.TOP, border = 10)

        vbox1.Add((-1,10))



        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        vbox1.Add(hbox4, flag = wx.LEFT, border = 10)

        vbox1.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label = 'Pause', pos= (225,675), size= (50, 30))
        hbox5.Add(btn1)
        vbox1.Add(hbox5, flag = wx.ALIGN_RIGHT | wx.RIGHT, border = 10)

        panel.SetSizer(vbox1)

        panel.SetBackgroundColour('#2ECC71')
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#7D3C98')

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20) #looks diff if assigned to vbox1
        panel.SetSizer(vbox)

        menubar = wx.MenuBar()

        fileMenu = wx.Menu() #menu object created under menubar
        fileMenu.Append(wx.ID_NEW, '&Reincarnate\tCtrl+R')
        fileMenu.Append(wx.ID_OPEN, '&Load\tCtrl+L')
        fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S')
        fileMenu.AppendSeparator()

        imp = wx.Menu()     #submenu of wx.Menu
        imp.Append(wx.ID_ANY, 'Change difficulty...')
        imp.Append(wx.ID_ANY, 'Import level...')
        imp.Append(wx.ID_ANY, 'Import theme...')
        imp.Append(wx.ID_ANY, 'Import mod...')

        fileMenu.Append(wx.ID_ANY, 'O&ptions', imp)
        fileMenu.Append(wx.ID_ABOUT, '&About\tCtrl+A')


        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&AnHero\tCtrl+Q') #menu items are also the commands associated with the items creates the qmi item
        qmi.SetBitmap(wx.Bitmap('exit.png'))

        fileMenu.Append(qmi)

        menubar.Append(fileMenu, '&Ask')

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown) #new
        self.SetSize((250, 200)) #new
        self.SetTitle('Context Menu') #new
        self.Show(True) #new
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)#qmifitem) #binds the ect_menu item to the onquit method which closes the appplication
        self.SetSize((500, 800))
        self.SetTitle('notsuspicious.exe')
        self.Centre()
        self.Show(True) #actually shows the widget



    def OnRightDown(self, f):
        self.PopupMenu(MyPopupMenu(self), f.GetPosition())

    def OnQuit(self, e):
        self.Close()

    def OnReincarnate(self):
        self.Refresh()


#_______________________________________________________________________


def main():

    app = wx.App()
    tetrous(None, title='Size')
    app.MainLoop()

if __name__ == '__main__':
    main()
