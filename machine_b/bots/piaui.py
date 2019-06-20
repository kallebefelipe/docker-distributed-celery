import time
from scrap import Scraper
import re


def trat_numero(value):
    value = re.sub(r"\D", "", value)
    value = value.zfill(20)
    return value


class ThemisconsultPi(Scraper):

    def __init__(self, **kwargs):
        super(ThemisconsultPi, self).__init__(**kwargs)
        self.url = 'http://www.tjpi.jus.br/themisconsulta/'
        self.fonte = 'themisconsult_pi'
        self.uf = 'PI'

    def ultimo_andamento(self):
        movs = self.driver.find_element_by_id('tab-movimentacoes')
        return movs.find_element_by_tag_name('tr').text

    def scraper(self, num_processo, arquivado=None):
        num_processo = trat_numero(num_processo)

        arquivado = None
        encontrado = False
        andamento = None

        input_num = self.driver.find_element_by_id("input-numero-unico")

        num_processo = num_processo[0:13] + num_processo[16:20]
        input_num.clear()
        input_num.send_keys(num_processo)

        self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Consultar')]").click()
        time.sleep(1)

        elems = self.driver.find_elements_by_id("tab-movimentacoes")

        if elems:
            text = elems[0].text
            encontrado = True

            andamento = self.ultimo_andamento()

            self.driver.execute_script("window.history.go(-1)")
        return encontrado, andamento
