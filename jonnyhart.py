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

			else:
				return self.render.portfolio(self.header, self.footer)

		else:
			return self.render.portfolio(self.header, self.footer)


class About(Parent):
	def GET(self):
		return self.render.about(self.header, self.footer)

class Services(Parent):
	def GET(self):
		return self.render.services(self.header, self.footer)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()