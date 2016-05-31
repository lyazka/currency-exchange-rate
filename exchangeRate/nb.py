import requests
from xml.etree import cElementTree as etree


class NBParser():
    """
    Parser of nationalbank.kz
    """
    url = 'http://nationalbank.kz/rss/rates_all.xml'

    @classmethod
    def parse(cls):
        data = {}
        response = requests.get(cls.url)
        root = etree.fromstring(response.content)
        items = root.findall('.//item')
        for item in items:
            code = item.find('.//title').text
            value = float(item.find('.//description').text.strip())
            quant = float(item.find('.//quant').text.strip())
            data[code] = value / quant

        return data


if __name__ == '__main__':
    print (NBParser.parse())
