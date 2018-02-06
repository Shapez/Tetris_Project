
#!/usr/bin/python

# tetrous.py

import wx
#All functions and objects from the basic modules will start with a wx.
APP_EXIT = 1
class tetrous(wx.Frame):    #tetrous was changed from Example



    def __init__(self, parent, title, *args, **kwargs):
        super(tetrous, self).__init__(parent, title=title,
            size=(500, 800), *args, **kwargs)
        self.Centre()
        self.Show()
        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&AnHero\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('exit.png')) #need to load exit.jpg
        fileMenu.Append(qmi)
      #  fitem = fileMenu.Append( wx.ID_EXIT, #'AnHero', 'Rage Quit')
        menubar.Append(fileMenu, '&Ask') #&Ask used to be called file
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)#qmifitem)

        self.SetSize((500, 800))
        self.SetTitle('notsuspicious.exe')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()




#_______________________________________________________________________
def main():

    app = wx.App()
    tetrous(None, title='Size')
    app.MainLoop()

if __name__ == '__main__':
    main()


