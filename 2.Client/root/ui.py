#Find in class Button(Window):
		Window.__init__(self, layer)
		
#Add
		if app.ENABLE_DETAILS_UI:
			self.overFunc = None
			self.overArgs = None
			self.overOutFunc = None
			self.overOutArgs = None
			
#Find in same class
		Window.__del__(self)
		
#Add
		if app.ENABLE_DETAILS_UI:
			self.overFunc = None
			self.overArgs = None
			self.overOutFunc = None
			self.overOutArgs = None
			
#Add functions in same class
	if app.ENABLE_DETAILS_UI:
		def OnMouseOverIn(self):
			if self.overFunc:
				apply(self.overFunc, self.overArgs )
		def OnMouseOverOut(self):
			if self.overOutFunc:
				apply(self.overOutFunc, self.overOutArgs )
		def SetOverEvent(self, func, *args):
			self.overFunc = func
			self.overArgs = args
		def SetOverOutEvent(self, func, *args):
			self.overOutFunc = func
			self.overOutArgs = args
			
#Find in class TitleBar(Window):
	def SetCloseEvent(self, event):
		self.btnClose.SetEvent(event)
		
#Add
	if app.ENABLE_DETAILS_UI:
		def CloseButtonHide(self) :
			if localeInfo.IsARABIC():
				self.imgLeft.LoadImage("d:/ymir work/ui/pattern/titlebar_right_02.tga")
				self.imgLeft.LeftRightReverse()
				self.btnClose.Hide()
			else:
				self.imgRight.LoadImage("d:/ymir work/ui/pattern/titlebar_right_02.tga")
				self.btnClose.Hide()