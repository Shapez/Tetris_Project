#!/usr/bin/python

# tetrous.py

import wx
'''
*All functions and objects from the basic modules will start with a wx.
*most documents will use methods such as AppendSeperator() or ItemAppend, this will bug out
    these methods should be simplified as simply .Append
*when you arent cracked out you need to add icons and hotkeys to the menu
'''
APP_EXIT = 1
class tetrous(wx.Frame):



    def __init__(self, parent, title, *args, **kwargs):
        super(tetrous, self).__init__(parent, title=title,
            size=(500, 800), *args, **kwargs)
        self.Centre()
        self.Show()
        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        #fileMenu.Append(wx.ID_NEW, '&Reincarnate') commented out when reincarnate icon and hotkeys added
        fileMenu.Append(wx.ID_OPEN, '&Load')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.Append(wx.ID_ABOUT, '&About')
        fileMenu.AppendSeparator()

        imp = wx.Menu()     #submenus are of wx.Menu
        imp.Append(wx.ID_ANY, 'Change difficulty...')
        imp.Append(wx.ID_ANY, 'Import level...')
        imp.Append(wx.ID_ANY, 'Import theme...')
        imp.Append(wx.ID_ANY, 'Import mod...')

        fileMenu.Append(wx.ID_ANY, 'O&ptions', imp)
        rmi = wx.MenuItem(fileMenu, APP_EXIT, '&Reincarnate\tCtrl+R')
        rmi.SetBitmap(wx.Bitmap('reincarnate.png')) #new reincarnate
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&AnHero\tCtrl+Q') #Does this need wx.ID_EXIT?
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.Append(rmi)
        fileMenu.Append(qmi)    #removed fileMenu.ItemAppend(qmi) because of deprication error warning is qmi quote menu item or quote menu input
       # fitem = fileMenu.Append( wx.ID_EXIT, 'AnHero', 'Rage Quit') redundant menu item can probably be deleted.

        menubar.Append(fileMenu, '&Ask')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        self.Bind(wx.EVT_MENU, self.Refresh, rmi)

        self.SetSize((500, 800))
        self.SetTitle('notsuspicious.exe')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):    #called when menu item is selected
        self.Close()

    def onReincarnate(self, f): #new onReincarnate
        self.Refresh() #new reincarnate

#_______________________________________________________________________
def main():

    app = wx.App()
    tetrous(None, title='Size')
    app.MainLoop()

if __name__ == '__main__':
    main()









