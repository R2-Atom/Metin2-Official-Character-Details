#Find in def HideAllWindows(self):
		if self.wndCharacter:
			self.wndCharacter.Hide()
			
#Change
		if app.ENABLE_DETAILS_UI:
			if self.wndCharacter:
				self.wndCharacter.Close()
		else:
			if self.wndCharacter:
				self.wndCharacter.Hide()
				
#Find in def ToggleCharacterWindow(self, state):
					self.wndCharacter.Hide()
					
#Change
					if app.ENABLE_DETAILS_UI:
						self.wndCharacter.Close()
					else:
						self.wndCharacter.Hide()