#!/usr/bin/python

# tetrous.py

import wx #imports wx modules and all subsequent modules will start with wx.
import time

#All functions and objects from the basic modules will start with a wx.
APP_EXIT = 1
#define width and height
w = 500
h = 800

#define colors
grn = '#52FF33'
prp = '#7D3C98'
blk = '#000000'

#list of games
game_library = ['tetris']
game_id = 0


class tetrous(wx.Frame):    #all widgets aside from another frame or dialogue box go in this class



    def __init__(self, parent, title, *args, **kwargs):
        super(tetrous, self).__init__(parent, title=title,
            size=(w, h), *args, **kwargs)
        self.Centre()
        self.Show()
        self.InitUI()
    #    self.timer = wx.TIMER_CONTINUOUS(self, 1000)
     #   self.Bind(wx.EVT_TIMER, self.Ontimer)
        self.GameState = 0
        self.runtime = 0



    def InitUI(self):

        panel = wx.Panel(self)
        panel.SetBackgroundColour(grn)
        vbox = wx.BoxSizer(wx.VERTICAL)

        midPan = wx.Panel(panel)
        #current_title = wx.StaticText(midPan, label="Tetris", pos=(w/2,h/12))
        #current_title.SetForegroundColour(grn)
        #font = current_title.GetFont()
        #font.PointSize += 100
        #current_title.GetFont()
        midPan.SetBackgroundColour(blk)

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)

        #buttons - docs https://www.blog.pythonlibrary.org/2010/06/09/wxpython-a-tour-of-buttons-part-1-of-2/

        # 1) create the button variable (it needs to be bound to a  method
        On_Button = wx.Button(panel, id=wx.ID_ANY, label="Start", name="Start")
        On_Button.Bind(wx.EVT_BUTTON, self.OnButton)

        #2) add to sizer
        vbox.Add(On_Button, 0, wx.ALL, 5)



        menubar = wx.MenuBar() #menubar created
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


        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&AnHero\tCtrl+Q') #menu items are also commands
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(qmi)

        menubar.Append(fileMenu, '&Ask')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)#qmifitem) #binds the ect_menu item to the onquit method which closes the appplication
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.w = w
        self.h = h
        self.SetSize((self.w, self.h))
        self.SetTitle('notsuspicious.exe')
        self.Centre()
        self.Show(True) #actually shows the widget
        print("self.show = ", self.Show())


    def OnButton(self, e):
        """
        This method is fired when the start button is clicked.
        :param e:
        :return:
        """

        start_button = e.GetEventObject()
        print("you clicked " + start_button.GetName())
        if self.GameState == 0:
          #  self.timer.Start(1000)
            start_button.SetLabel("Pause")
            print("Game is now started. Click 'Pause' to pause")
            self.GameState = 1
            self.OnReincarnate()
            print("GameState set to " + str(self.GameState))
          #  print(self.timer.GetInterval())

        else:
            if self.GameState == 1:
             #   self.timer.Stop()
                start_button.SetLabel("Start")
                self.GameState = 0
                print("Game is Paused. Click 'Start' to start")
                self.OnReincarnate()
                print("GameState set to " + str(self.GameState))





    def OnRightDown(self, f): #new changes
  #      print(self.PopupMenu(MyPopupMenu(self), f.GetPosition()))
        print("OnRightDown")

    def OnQuit(self, e):
       print(runtime)


    def OnReincarnate(self):
        self.Refresh()


#_______________________________________________________________________


def main():
    print("def main()")
    app = wx.App()
    print('app = ',app)
    tetrous(None, title='Size')
    app.MainLoop()

if __name__ == '__main__':
    main()


