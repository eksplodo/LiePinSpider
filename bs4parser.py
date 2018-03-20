# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


class BsParser:
    def __init__(self):
        pass

    @staticmethod
    def get_page_count(html):
        """
        获取招聘信息的页码总数
        :param html: 招聘信息返回结果的html
        :return: 页码总数
        """
        soup = BeautifulSoup(html, "lxml")
        page_count = soup.select("div.pagerbar a.last")[0].attrs["href"][-2:]
        return int(page_count)

    @staticmethod
    def parse_job_list(html):
        """
        解析工作的总条数
        :param html: 每个页面返回的html
        :return: 工作列表链接生成器
        """
        soup = BeautifulSoup(html, "lxml")
        job_list = soup.select("ul.sojob-list li div div.job-info h3 a")
        for job in job_list:
            yield job.attrs["href"]

    @staticmethod
    def parse_job_detail(html):
        """
        解析工作详情
        :param html: 根据得到的每条工作的链接请求得到的html
        :return: 工作信息字典格式
        """
        soup = BeautifulSoup(html, "lxml")
        # 工作标题
        title_result = soup.select("div.title-info h1")
        title = title_result[0].text.strip() if title_result else ''
        # 薪水
        wage_result = soup.select("div.job-title-left p")
        wage = ''
        if wage_result:
            wage = ''.join(wage_result[0].stripped_strings)
            if len(wage) == 11 or len(wage) == 12:
                wage = wage[:6]
        location_result = soup.select("div.job-title-left p.basic-infor span a")    # 工作地点
        location = location_result[0].text.strip() if location_result else ''
        # 学历要求
        education_result = soup.select("div.job-qualifications > span:nth-of-type(1)")
        education = education_result[0].text.strip() if education_result else ''
        # 经验
        experience_result = soup.select("div.job-qualifications > span:nth-of-type(2)")
        experience = experience_result[0].text.strip() if experience_result else ''
        # 公司名称
        company_result = soup.select("div.company-logo p a")
        company = company_result[0].text.strip() if company_result else ''
        # 公司行业
        industry_result = soup.select("ul.new-compintro li a")
        industry = industry_result[0].text.strip() if industry_result else ''
        # 职位描述
        desc_result = soup.select("div.about-position > div.job-item.main-message.job-description > div")
        desc = ''.join(desc_result[0].stripped_strings) if desc_result else ''

        return {
            '职位名称': title,
            '待遇范围': wage,
            '公司地点': location,
            '学历要求': education,
            '工作经验': experience,
            '公司名称': company,
            '公司行业': industry,
            '职位描述': desc,
        }
