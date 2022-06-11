# ابحث عن الكلاس التالي

class GameWindow(ui.ScriptWindow):

#أسفل :
self.playerGauge = None

#أضف :
		self.fpsLine = None
		self.fpsLine = ui.TextLine()
		self.fpsLine.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		self.SetPosition((wndMgr.GetScreenWidth() - 130) / 2, 237) ## قم بتغير الإحدثيات من هنا 
			
#ابحث عن دالة
def Close(self):
#ابحث داخلها عن :
			self.interface=None

#أضف في الأسفل :
 		self.fpsLine = None

#إبحث عن
def __BuildDebugInfo(self):
#داخلها ابحث عن :
		self.ViewDistance.SetPosition(0, 0)
		
#أضف اسفلها
 		self.fpsLine.SetWindowHorizontalAlignCenter()
 		self.fpsLine.SetHorizontalAlignCenter()
 		self.fpsLine.SetFeather()
 		self.fpsLine.SetOutline()
		self.fpsLine.SetFontName(localeInfo.UI_DEF_FONT)
 		self.fpsLine.Show()
			
#إبحث عن :
def OnUpdate(self):
#أسفل :
		self.interface.BUILD_OnUpdate()

#أضف اسفلها :
 		fFps = app.GetRenderFPS()
 		self.fpsLine.SetText("FPS : %s" % (fFps))
