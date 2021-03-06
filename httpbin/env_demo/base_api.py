import requests
import yaml

__author__ = 'zenghuan'


class Base_api:
    # 封装request
    def send(self, data):
        # url = http://127.0.0.1:9999/demo_new.txt
        #读取yaml文件
        env = self.get_yaml()
        data['url'] = data['url'].replace('testing', env['testing-studio'][env["default"]])
        # return requests.request(data['method'], data['url'])
        return requests.request(**data)


    def get_yaml(self):
        return yaml.safe_load(open("data/env.yaml"))

    #把env的json格式转换为yaml格式并存入yaml文件中
    def json_to_yaml(self):
        env = {
            "default": "dev",
            "testing-studio": {
                "dev": "127.0.0.1",
                "test": "127.0.0.2"

            }
        }
        with open("data/env.yaml", "w") as f:
            yaml.safe_dump(data=env, stream=f)
            f.close()