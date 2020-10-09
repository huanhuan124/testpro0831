import requests
import yaml
from  string import Template

__author__ = 'zenghuan'


class Base_api:
    def send(self, data):
        return requests.request(**data)

        # 把env的json格式转换为yaml格式并存入yaml文件中

    def json_to_yaml(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "wwed0f3dc9f8233774",
                "corpsecret": "Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0"

            }
        }
        with open("D:/SoftwareInstall/pycharmworkspace/testpro0831/httpbin/wework_requests/data/data.yml", "w") as f:
            yaml.safe_dump(data=data, stream=f)
            f.close()

    def get_yaml(self):
        return yaml.safe_load(open("D:/SoftwareInstall/pycharmworkspace/testpro0831/httpbin/wework_requests/data/data.yml"))

    def template_to(self,data):
        with open("D:/SoftwareInstall/pycharmworkspace/testpro0831/httpbin/wework_requests/data/data.yml") as f:
            re = Template(f.read()).substitute(**data)

        return yaml.safe_load(re)


