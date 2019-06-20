from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from database.connection import update_process
import time


class Scraper():

    def __init__(self, **kwargs):
        super(Scraper, self).__init__()

    def get_url(self):
        self.driver.get(self.url)

    def login(self):
        return None

    def set_up(self):
        chrome_options = webdriver.ChromeOptions()

        prefs = {
            "plugins.plugins_list": [{
                "enabled": False,
                "name": "Chrome PDF Viewer"
            }],
            "download.extensions_to_open": "applications/pdf"
        }
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {
            'cmd': 'Page.setDownloadBehavior',
            'params': {
                'behavior': 'allow',
                'downloadPath': './relatorios'
            }
        }
        self.driver.execute("send_command", params)

    def accept_alert(self):
        try:
            time.sleep(1)
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(1)
            return True
        except NoAlertPresentException:
            pass

    def credentials(self):
        self.set_up()
        self.get_url()
        self.login()

    def run(self, processos, base):
        for pro in processos:
            self.credentials()

            numero = pro.get('numero')

            encontrado, andamento = self.scraper(numero)

            pro['encontrado'] = encontrado
            pro['ultimo_andamento'] = andamento

            if encontrado:
                pro['fonte'] = self.fonte
            update_process(pro['_id'], pro, base)
        self.driver.close()
