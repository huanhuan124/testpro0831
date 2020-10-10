from httpbin.wework_requests.api.get_token import Get_token

__author__ = 'zenghuan'



class Test_get_token:

    def setup(self):
        self.token = Get_token()


    def test_get_token(self):
        self.token.get_token()

        # print(res.json())

   # 只是用来方便把json转换为yaml
   #  def test_json_to_yaml(self):
   #      self.token.json_to_yaml()
