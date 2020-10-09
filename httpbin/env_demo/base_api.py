import requests
import yaml

__author__ = 'zenghuan'


class Base_api:

    # env = {
    #     "default": "dev",
    #     "testing-studio": {
    #         "dev": "127.0.0.1",
    #         "test": "127.0.0.2"
    #
    #     }
    # }

    # 封装request
    def send(self, data):
        # url = http://127.0.0.1:9999/demo_new.txt
        #读取yaml文件

        env = yaml.safe_load(open("data/env.yaml"))

        print(data['url'])
        data['url'] = data['url'].replace('testing', env['testing-studio'][env["default"]])
        print(data['url'])
        return requests.request(data['method'], data['url'])



    #把env转换为yaml格式并存入yaml文件中
    def get_yaml(self):
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