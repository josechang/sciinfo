import wx
class window(wx.Frame):
    def __init__(self,parent=None,id=1234,name="Upload"):
        wx.Frame.__init__(self,parent,id,name,size = (800,500))
        panel = wx.Panel(self)
        button = wx.Button(panel, 1, 'Open', pos=(30,30), size= (63,30))
        self.Bind(wx.EVT_BUTTON,self.file, button)
    def file(self,event):
        style = wx.FD_OPEN
        fdialog=wx.FileDialog(self,'Open',style= style)
        if fdialog.ShowModal()==wx.ID_OK:
            path = fdialog.GetPath()
            import os
            os.strtfile(path)

#if __name__ =='__main__':
app = wx.App()
frame = window()
frame.Show()
app.MainLoop()
