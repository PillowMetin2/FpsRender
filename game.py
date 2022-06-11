#إبحث عن :

class GameWindow(ui.ScriptWindow):

#أسفل :
self.__ProcessPreservedServerCommand()

#أضف :
		self.pingLine = None
		if app.ENABLE_PINGTIME:
			self.pingLine = ui.TextLine()
			self.pingLine.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
			self.pingLine.SetFontColor(1.0,1.0,1.0)
			self.pingLine.SetPosition((wndMgr.GetScreenWidth() - 130) / 2, 207)
			
#إبحث عن
def Close(self):
#أسفل :
			self.interface=None

#أضف :
		if app.ENABLE_PINGTIME:
			self.pingLine = None

#إبحث عن
def __BuildDebugInfo(self):
#اسفل :
		self.ViewDistance.SetPosition(0, 0)
		
#أضف اسفلها
		if app.ENABLE_PINGTIME:
			self.pingLine.SetWindowHorizontalAlignCenter()
			self.pingLine.SetHorizontalAlignCenter()
			self.pingLine.SetFeather()
			self.pingLine.SetOutline()
			self.pingLine.Show()
			
#إبحث عن :
def OnUpdate(self):
#أسفل :
		self.interface.BUILD_OnUpdate()

#أضف اسفلها :
		if app.ENABLE_PINGTIME:
			nPing = app.GetPingTime()
			self.pingLine.SetText("PING: %s" % (nPing))