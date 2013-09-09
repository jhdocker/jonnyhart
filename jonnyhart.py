import web

urls = (
	'/', 'Home',
	'/pics', 'Portfolio',
	'/about', 'About',
	'/services', 'Services',
	)

class Parent:
	def __init__(self):
		self.render = web.template.render('templates/')
		self.header = self.render.header()
		self.footer = self.render.footer()
		self.request_data = web.input()


class Home(Parent):
	def GET(self):
		return self.render.home(self.header, self.footer)

class Portfolio(Parent):
	def GET(self):
		action=""
		if self.request_data:

			if self.request_data.action == "concept-art":
				return self.render.concept(self.header, self.footer)

			elif self.request_data.action =="whiteboard":
				return self.render.whiteboard(self.header, self.footer)

			elif self.request_data.action =="video":
				return self.render.video(self.header, self.footer)

			elif self.request_data.action =="websites":
				return self.render.websites(self.header, self.footer)

			elif self.request_data.action =="illustration":
				return self.render.illustration(self.header, self.footer)
				
			else:
				return self.render.portfolio(self.header, self.footer)

		else:
			return self.render.portfolio(self.header, self.footer)


class About(Parent):
	def GET(self):
		return self.render.about(self.header, self.footer)

class Services(Parent):
	def GET(self):
		action=""
		if self.request_data:
			if self.request_data.action=="contact":
				return self.render.contact(self.header, self.footer)

			else:
				return self.render.services(self.header, self.footer)
		
		else:
			return self.render.services(self.header, self.footer)


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()