from crawl import Crawler
from bs4parser import BsParser
from xpathparse import XpathParse
from reparse import ReParse

if __name__ == '__main__':
    util = {
        1: BsParser,
        2: XpathParse,
        3: ReParse
    }
    while True:
        choice = input('Please select the way you want to get job info:\n'
                       '1: BeautifulSoup\n'
                       '2: Xpath\n'
                       '3: Re\n'
                       ':'
                       )
        if int(choice) in [1, 2, 3]:
            break
        else:
            print('Please entry right number.')
    spider = Crawler(util[int(choice)])
    print('Spider started')
    spider.start()
    print('Spider is over. thank you')
