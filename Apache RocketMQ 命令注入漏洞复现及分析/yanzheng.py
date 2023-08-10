import requests


class RocketMQ():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'}

    def get_HTML(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response

    def parse(self):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    rocketMQ = RocketMQ()
    rocketMQ.main()
