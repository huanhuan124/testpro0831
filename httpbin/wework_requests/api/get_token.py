from httpbin.wework_requests.api.base_api import Base_api

__author__ = 'zenghuan'


class Get_token(Base_api):
    # 企业微信每一个功能都有一个单独的secret，要想使用企业微信api，必须先获得access_token
    # _contacts_secret = 'Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0'
    # _companyID = 'wwed0f3dc9f8233774'
    #
    # data = {
    #     "method":"get",
    #     "url":"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #     "params":{
    #         "corpid":_companyID,
    #         "corpsecret":_contacts_secret
    #
    #     }
    # }

    def get_token(self):
        # 读取yaml文件，测试信息放在yaml文件中
        para = {
            "corpid": "wwed0f3dc9f8233774",
            "corpsecret": "Pt8SBjBFzFLR-_iq9BxRtk47jw7ayhlmgk567ecCKZ0"
        }

        #得到转换后的参数，用para中的内容替换到data.yml文件中的变量
        data = self.template_to(para)
        #发起请求
        r = self.send(data)
        return r