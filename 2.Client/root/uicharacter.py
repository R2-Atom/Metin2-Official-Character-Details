#Add
if app.ENABLE_DETAILS_UI:
	import uiCharacterDetails
	
#Find
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		
#Change
	def __init__(self):
		if app.ENABLE_DETAILS_UI:
			self.chWndPos = (24 + 45, (wndMgr.GetScreenHeight() / 2) - 200)	##ATOM_FIX_BONUS_WINDOW
			self.chDetailsWnd = None
			self.isOpenedDetailsWnd = False
		ui.ScriptWindow.__init__(self)
			
#Find
	def Show(self):
		self.__LoadWindow()
		
#Add		
		if app.ENABLE_DETAILS_UI:
			self.__InitCharacterDetailsUIButton()
			if self.chDetailsWnd and self.isOpenedDetailsWnd:
				self.chDetailsWnd.Show()
				
#Find
		self.questLastCountList = []
		
#Add
		if app.ENABLE_DETAILS_UI:
			self.MainBoard = self.GetChild("board")
			self.ExpandBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_minimize_normal.tga", "btn_minimize_over.tga", "btn_minimize_down.tga")
			self.ExpandBtn.SetEvent(ui.__mem_func__(self.__ClickExpandButton))
			self.MinimizeBtn = ui.MakeButton(self.MainBoard, 240, 120, "", "d:/ymir work/ui/game/belt_inventory/", "btn_expand_normal.tga", "btn_expand_over.tga", "btn_expand_down.tga")
			self.MinimizeBtn.SetEvent(ui.__mem_func__(self.__ClickMinimizeButton))
			
#Find
	def ActEmotion(self, emotionIndex):
		self.__ClickEmotionSlot(emotionIndex)
		
#Add
	if app.ENABLE_DETAILS_UI:
		def OnTop(self):
			if self.chDetailsWnd:
				self.chDetailsWnd.SetTop()
		def Hide(self):
			if self.chDetailsWnd:
				self.isOpenedDetailsWnd = self.chDetailsWnd.IsShow()
				self.chDetailsWnd.Close()
			wndMgr.Hide(self.hWnd)
		def __InitCharacterDetailsUIButton(self):
			self.ExpandBtn.Show()
			self.MinimizeBtn.Hide()
			
		def __ClickExpandButton(self):
			x, y = self.GetMainBoardPosition()	##ATOM_FIX_BONUS_WINDOW
			if not self.chDetailsWnd:
				self.chDetailsWnd = uiCharacterDetails.CharacterDetailsUI(self)
				self.chDetailsWnd.AdjustPosition(x-45, y-9)	##ATOM_FIX_BONUS_WINDOW	Set (x,y) position bonus_details when press "c" and klick "ExpandButton" 
				self.chDetailsWnd.Show()
			else:
				self.chDetailsWnd.Show()
				
			self.ExpandBtn.Hide()
			self.MinimizeBtn.Show()
				
		def __ClickMinimizeButton(self):			
			self.chDetailsWnd.Hide()
			self.MinimizeBtn.Hide()
			self.ExpandBtn.Show()
			
		def OnMoveWindow(self, x, y):
			self.chWndPos = x + 45, y + 9	##ATOM_FIX_BONUS_WINDOW	Set (x,y) position bonus_details when press "c" and you move main window "uicharachter" then klick "ExpandButton" 
			if self.chDetailsWnd:
				self.chDetailsWnd.AdjustPosition(x, y)
				
		def GetMainBoardPosition(self):		##ATOM_FIX_BONUS_WINDOW	
			x, y = self.chWndPos		##ATOM_FIX_BONUS_WINDOW	
			return x, y			##ATOM_FIX_BONUS_WINDOW

#Find
		for titleBarValue in self.titleBarDict.itervalues():
			titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide))
				
#Change
		for titleBarValue in self.titleBarDict.itervalues():
			if app.ENABLE_DETAILS_UI:
				titleBarValue.SetCloseEvent(ui.__mem_func__(self.Close))
			else:
				titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide))
				
#Find
	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()
			
#Add
		if app.ENABLE_DETAILS_UI:
			if self.chDetailsWnd and self.chDetailsWnd.IsShow():
				self.chDetailsWnd.Hide()
				
#Find
		if self.refreshToolTip:
			self.refreshToolTip()
			
#Add
		if app.ENABLE_DETAILS_UI:
			if self.chDetailsWnd and self.chDetailsWnd.IsShow():
				self.chDetailsWnd.RefreshLabel()
