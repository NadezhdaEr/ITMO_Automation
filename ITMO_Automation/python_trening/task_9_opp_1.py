from task_9_checks import Checks
class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
        self.loc = loc
buttons = Button('#кнопка', 'нажми')
print(buttons.loc)
print(buttons.text)
print(buttons.check_text())
class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
        self.loc = loc
titles = Title('#title', 'заголовок')
print(titles.loc)
print(titles.text)
print(titles.check_text())

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text
        self.loc = loc

links = Link('#url','ссылка')
print(links.loc)
print(links.text)
print(links.check_text())

#class Input:

 #   def __init__(self, loc, text):
#      self.loc = loc
#        self.text = text

#search = Input('input#search')

#print(search.loc)
#print(search.text)

#class Button:

 #   def __init__(self, loc, text):
#        self.loc = loc
 #       self.text = text

#search = Button('input#search')

#print(search.loc)
#print(search.text)

#class Title:

 #   def __init__(self, loc, text):
  #      self.loc = loc
#        self.text = text

#search = Title('input#search')

#print(search.loc)
#print(search.text)

#class Link:

 #   def __init__(self, loc, text):
 #       self.loc = loc
 #       self.text = text

#search = Link('input#search')

#print(search.loc)
#print(search.text)

