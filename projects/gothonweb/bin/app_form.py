# just create a new app file for the form format website app
import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base = 'layout')
# it first loads the layout.html, and passed the hello_form.html file on top of it.

class Index(object):

    def GET(self):
        return render.hello_form()

    def POST(self):
        # it's just another way the browser hides the form filds and shows the inputs.
        form = web.input(name = "Nobody", greet = "hello")

        greeting = "%s, %s" % (form.greet, form.name)

        return render.index(greeting = greeting)
        # .index should be one of the attributes for the render class instance...

if __name__ == "__main__":
    app.run()
