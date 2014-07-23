import kivy
kivy.require('1.8.1')

from kivy.app import App

from kvlang.ast import AST

root = AST.load_string('''
#:kivy 1.0
#:set txt 'hi'

<MyLabel@Label>:
	canvas.before:
		Color:
			rgba: 1, 0, 0, 0.4
		Rectangle:
			pos: self.pos
			size: self.size

#comment here
BoxLayout:
	orientation: 'vertical'
	
	Button:
		text: txt
	
	canvas.after:
		Color:
			rgba: 1, 1, 1, 1
		Line:
			points: [self.x, self.y, self.right, self.top]
	
	MyLabel:
		size_hint_y: 1.5
		text: '!!!!!!'
''')

class TestApp(App):
	def build(self):
		return root

if __name__ == '__main__':
	TestApp().run()
