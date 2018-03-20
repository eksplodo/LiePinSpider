import requests


class Methon(object):
    def __inti__(self):
        pass

    @staticmethod
    def get_html(url):
        """
        获取网页html
        :return: html或None
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/65.0.3325.162 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                response.encoding = response.apparent_encoding
                return response.text
            else:
                print("错误的状态码来源：{0}",format(response.url))
                return None
        except Exception as e:
            print("出错啦：", e)
            return None
