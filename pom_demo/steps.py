class GoogleSteps(object):

    def __init__(self, app):
        self.app = app

    def search(self, query):
        with self.app.page_search as page:
            page.open()
            page.field_search.value = query
            page.button_search.click()

            page.list_search.wait_for_presence()
            assert page.list_search.is_visible
