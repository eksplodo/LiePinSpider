from lxml import etree


class XpathParse(object):
    def __init__(self):
        pass

    @staticmethod
    def get_page_count(html):
        doc = etree.HTML(html)
        pages = int(doc.xpath('//a[@class="last"]/@href')[0][-2:])
        return pages

    @staticmethod
    def parse_job_list(html):
        doc = etree.HTML(html)
        job_list = doc.xpath('//div[@class="job-info"]/h3/a/@href')
        for job in job_list:
            yield job

    @staticmethod
    def parse_job_detail(html):
        doc = etree.HTML(html)
        # 工作标题
        title_result = doc.xpath("//div[@class='title-info']/h1/text()")
        title = title_result[0] if len(title_result) > 0 else ''
        # 薪水
        wage_result = doc.xpath('//div[@class="job-title-left"]/p')
        wage = ''
        if len(wage_result) > 0:
            # xpath(string(.) 是取得当前标签下的所有文字
            wage = wage_result[0].xpath('string(.)').strip().split('\r')[0]
        # 工作地点
        location_result = doc.xpath('//div[@class="job-title-left"]/p[2]/span/a/text()')
        location = location_result[0] if len(location_result) > 0 else ''
        # 学历要求
        education_result = doc.xpath('//div[@class="job-qualifications"]/span[1]/text()')
        education = education_result[0] if len(education_result) > 0 else ''
        # 经验
        experience_result = doc.xpath("//div[@class='job-qualifications']/span[2]/text()")
        experience = experience_result[0] if len(experience_result) > 0 else ''
        # 公司名称
        company_result = doc.xpath("//div[@class='company-logo']/p/a/text()")
        company = company_result[0] if len(company_result) > 0 else ''
        # 公司行业
        industry_result = doc.xpath("//ul[@class='new-compintro']/li/a/text()")
        industry = industry_result[0] if len(industry_result) > 0 else ''
        # 职位描述
        desc_result = doc.xpath('//div[@class="content content-word"]')
        desc = desc_result[0].xpath('string(.)').strip().split('\n')[0] if len(desc_result) > 0 else ''

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
