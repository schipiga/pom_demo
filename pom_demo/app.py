import pom

from .pages import PageSearch


@pom.register_pages([PageSearch])
class App(pom.App):

    def __init__(self, url, *args, **kwgs):
        super(App, self).__init__(url, 'firefox', *args, **kwgs)
        self.webdriver.maximize_window()
        self.webdriver.implicitly_wait(5)
        self.webdriver.set_page_load_timeout(30)
