import xlwt

from utils import Methon


class Crawler(object):
    def __init__(self, methon):
        self.base_url = "https://www.liepin.com/zhaopin/?key=python&curPage={}"
        self.offset = 1
        self.workbook = None
        self.sheet = None
        self.spider = methon()

    def store_data(self, data):
        """
        存储
        :param data:
        :return:
        """
        final_data = [value for value in data.values()]
        if not self.workbook:
            self.create_file('python职位')
            self.write_header()
        self.write_data(final_data)
        self.workbook.save('python职位.xls')

    def create_file(self, sheet_name):
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet(sheet_name)

    def write_header(self):
        header = ['职位名称', '薪酬', '公司地点', '学历', '工作经验', '公司名称', '公司行业', '工作描述']
        for n in range(8):
            self.sheet.write(0, n, header[n])

    def write_data(self, data):
        for row_idx, row in enumerate(data):
            self.sheet.write(self.offset, row_idx, row)
        self.offset += 1

    def get_pages(self, html):
        pages = self.spider.get_page_count(html)
        for page in range(pages+1):
            self.get_job_list(page)

    def get_job_list(self, page):
        html = Methon.get_html(self.base_url.format(str(page)))
        job_list = self.spider.parse_job_list(html)
        self.do_detail(job_list)

    def do_detail(self, arg):
        for url in arg:
            if isinstance(url, str) and url.startswith('https://www.liepin.com'):
                print('Now parseing ', url)
                data = self.spider.parse_job_detail(Methon.get_html(url))
                self.store_data(data)

    def start(self):
        """
        爬虫启动
        """
        html = Methon.get_html(self.base_url.format('0'))
        self.get_pages(html)
