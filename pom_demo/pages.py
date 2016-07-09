import pom
from pom import ui
from selenium.webdriver.common.by import By


class ListRow(ui.Row):
    cell_xpath = './div[contains(@class, "rc")]'


class ListBody(ui.table.Body):
    row_xpath = './div[contains(@class, "g")]'
    row_cls = ListRow


@ui.register_ui(body=ListBody(By.XPATH, '.'))
class ListSearch(ui.Table):
    columns = {'name': 1}


@ui.register_ui(
    field_search=ui.TextField(By.NAME, 'q'),
    button_search=ui.Button(By.NAME, 'btnG'),
    list_search=ListSearch(By.CSS_SELECTOR, 'div.srg'))
class PageSearch(pom.Page):
    url = "/"
