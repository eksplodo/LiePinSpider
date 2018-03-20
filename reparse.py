import re


class ReParse(object):
    def __init__(self):
        pass

    @staticmethod
    def get_page_count(html):
        pattern = re.compile('<a class="last".*?curPage=(\d+)" title="末页">', re.S)
        pages = int(re.findall(pattern, html)[0])
        return pages

    @staticmethod
    def parse_job_list(html):
        pattern = re.compile('<div class="job-info">.*?href="(.*?)"', re.S)
        job_list = re.findall(pattern, html)
        return job_list

    @staticmethod
    def parse_job_detail(html):
        # 工作标题
        title_result = re.findall('<div class="title-info">.*?title="(.*?)"', html, re.S)
        title = title_result[0] if len(title_result) > 0 else ''
        # 薪水
        wage_result = re.findall('<p class="job-item-title">(\d{1,3}-\d{1,3}[\u4e00-\u9fa5])', html, re.S)
        wage = ''
        if len(wage_result) > 0:
            wage = wage_result[0]
        # 工作地点
        location_result = re.findall('<i class="icons24 icons24-position"></i>.*?>(.*?)</a>', html, re.S)
        location = location_result[0] if len(location_result) > 0 else ''
        # 学历要求
        education_result = re.findall('<div class="job-qualifications">\s+<span>(.*?)</span> <span>(.*?)</span>',
                                      html, re.S)
        education = education_result[0][0] if len(education_result) > 0 else ''
        # 经验
        experience = education_result[0][1] if len(education_result) > 0 else ''
        # 公司名称
        company_result = re.findall('<div class="company-logo">.*?<p>.*?>(.*?)</a>', html, re.S)
        company = company_result[0] if len(company_result) > 0 else ''
        # 公司行业
        industry_result = re.findall('行业.*?>(.*?)</a>', html, re.S)
        industry = industry_result[0] if len(industry_result) > 0 else ''
        # # 职位描述
        desc_result = re.findall('<div class="content content-word">(.*?)</div>', html, re.S)
        desc = desc_result[0].replace('<br/>', '').strip() if len(desc_result) > 0 else ''

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
