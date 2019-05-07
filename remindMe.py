import wx
from controller import Controller

class InputPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        # list out the reminders
        reminders = self.Read()
        self.reminders = wx.StaticText(self, label="List of reminders:\n\r" + reminders)
        grid.Add(self.reminders, pos=(0, 0))

        self.quote = wx.StaticText(self, label="Enter an reminder item:")
        grid.Add(self.quote, pos=(1, 0))

        # add a spacer to the sizer
        # grid.Add((10, 40), pos=(1, 0))

        # A save button
        self.button1 = wx.Button(self, label="Save")
        self.Bind(wx.EVT_BUTTON, self.OnSave, self.button1)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Task:")
        grid.Add(self.lblname, pos=(2, 0))
        self.editname = wx.TextCtrl(self, value="", size=(140, -1))
        grid.Add(self.editname, pos=(2, 1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Month:(mm)")
        grid.Add(self.lblname, pos=(3, 0))
        self.editmonth = wx.TextCtrl(self, value="", size=(140, -1))
        grid.Add(self.editmonth, pos=(3, 1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editmonth)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editmonth)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Date:(dd)")
        grid.Add(self.lblname, pos=(3, 2))
        self.editdate = wx.TextCtrl(self, value="", size=(140, -1))
        grid.Add(self.editdate, pos=(3, 3))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editdate)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editdate)

        hSizer.Add(grid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button1, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)

    def Read(self):
        controller = Controller()
        return controller.readAll()

    def OnSave(self, event):        
        controller = Controller()
        print ("Clicked on object with Id %d\n" % event.GetId())
        controller.save(self.editname.Value)
        controller.readAll()

    def EvtText(self, event):
        print ('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        print ('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Remind Me", size=(700, 300))
panel = InputPanel(frame)
frame.Show()
app.MainLoop()
