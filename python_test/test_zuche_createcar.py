__author__ = 'zenghuan'

import yaml
import requests
import pytest
import random

class Test_zuche_createcar:
    # def test_car_get(self):
    # pass
    #     url = "http://carvmscoretest.zuche.com/carvmscore/vehiclemanage/readyrun/vehicleReadyRunVueController/getVehicleBusinessInfoByVehicleId.do_?vehicleId=379439"


    def setup(self):
        # 登录接口，每个接口调用之前都需要调用
        url = "http://caradmintest.zuche.com/system/login.do_"
        data = {
            "loginId":"UA244Y8SbzJRKNVluixyKA==",
            "password":"qLpmhT5PIxYdFCh/kZ+dcw=="

        }
        lg_res = requests.post(url=url,data=data)
        print(lg_res.content)
        print(lg_res.cookies)
        self.cookies = lg_res.cookies
        self._vehicleNo = "京P"+str(random.randint(66666,99999))

        print(self._vehicleNo)
        self._frameNo = "PYTHONCAR"+str(random.randint(11111111,99999999))
        print(self._frameNo)
        # CAR20201013
        self._invoiceNo = "PYTHONCAR"+str(random.randint(11,99))
        print(self._invoiceNo)

    def test_createVehicle(self):
        url = "http://carvmscoretest.zuche.com/carvmscore/vehiclemanage/readyrun/vehicleReadyRunVueController/createVehicle.do_"
        # params = yaml.safe_load(open("D:/SoftwareInstall/pycharmworkspace/testpro0831/python_test/data/params.yaml"))
        # print(params)
        # print(type(params))
        self.json_to_yaml()
        data_yaml = self.get_yaml()
        print(data_yaml)
        print(type(data_yaml))
        header = {
            'content-type':'application/json;charset=UTF-8',
            'Origin':'http://carvmscoretest.zuche.com/',
            'Referer':'http://carvmscoretest.zuche.com/',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.'
        }
        res = requests.post(url=url,json=data_yaml,headers=header,cookies=self.cookies)
        print(res.text)
        assert 0 == res['status']

    # def test_createVehicle2(self):
    #
    #     para = {
    #         "companyId":"46",
    #         "brandId":"67",
    #         "vehicleSeriesId":"",
    #
    #     }
    #
    #     url = "http://carvmscoretest.zuche.com/carvmscore/vehiclemanage/readyrun/vehicleReadyRunVueController/createVehicle.do_"
    #     self.json_to_yaml()

    def get_yaml(self):
        return yaml.safe_load(open("D:/SoftwareInstall/pycharmworkspace/testpro0831/python_test/data/para2"))

    #把env的json格式转换为yaml格式并存入yaml文件中
    def json_to_yaml(self):

        env2 = {
        "baseInfoVo": {
        "vehicleId": "",
        "companyId": 46,
        "brandId": 67,
        "vehicleSeriesId": 560,
        "vehiclenoCityId": 1,
        "vehiclenoCityName": "北京",
        "vehicleNo": self._vehicleNo,
        "frameNo": self._frameNo,
        "engineNo": self._frameNo,
        "envStandard": 1,
        "modelId": 1221,
        "vehicleLicensemode": "",
        "vehicleModel300Name": "",
        "color": 10,
        "registerNo": "",
        "useNature": 0,
        "carUseType": 0,
        "vehicleRemark": "",
        "checkTime": "",
        "contractNo": self._frameNo
        },
        "operatingInfoVo": {
        "shortModelId": 1103,
        "shortModelName": "宝马BMW9/三厢/2.8自动",
        "businessType": 1,
        "isUCar": 0,
        "isHertz": 0,
        "isLease": 0,
        "onLineTime": "",
        "lastQuitRunTime": "",
        "handleTime": "",
        "ucarRentType": "",
        "oilVolume": None,
        "oilVolumeLatticeNum": 0,
        "orderCar": 0,
        "cityId": "",
        "nowCityId": "",
        "nowCityName": "",
        "parkCityId": "",
        "departmentId": "",
        "nowDepartmentId": "",
        "parkDeptId": "",
        "runMilesInput": "1000",
        "nextInspecteTime": "",
        "regTime": "",
        "firstLevelStatus": 100000,
        "selfFirstLevelStatus": 100000
        },
        "assetInfoVo": {
        "bussLineId": 1,
        "bussLineTime": "",
        "willBussLineId": "",
        "willBussLineTime": "",
        "checkResultName": "",
        "allocationStatusName": "",
        "isInsideScrapName": "",
        "lastApproveSaleTime": "",
        "firstTransferOwnershipTime": "",
        "vehicleNoBeforeTransfer": ""
        },
        "financeInfoVo": {
        "carOwnerId": 32,
        "purchasePrice": "500000",
        "registrationAndPettyExpenses": "1000",
        "taxAmount": "2000",
        "incrementTaxExpenses": "100000",
        "monthDepreciationRate": "",
        "originalValue": "603000",
        "taxInvoiceDate": "",
        "purchaseDate": "",
        "remainderPrice": "",
        "vehicleAndVesselTax": "",
        "estimatedRemainderPrice": "",
        "realHandlePrice": "",
        "handlePettyExpenses": "",
        "realSellOutPrice": "",
        "handlePettyIncrementTax": "",
        "invoiceNo": self._invoiceNo
        },
        "garageInfoVo": {
        "lastTimeAttendMile": "",
        "nextTimeAttendMile": "",
        "vehicleFrom": ""
        },
        "deviceInfoVo": {
        "gps": 0,
        "deviceNo": "",
        "deviceType": ""
        },
        "noInfoPo": {
        "vehicleNoColor": 0
        },
        "colorPo": {
        "interiorColorId": ""
        },
        "modifyEmpName": None,
        "createEmpName": None,
        "createTime": None,
        "modifyTime": None
        }

        env3 = {
        "baseInfoVo": {
        "vehicleId": "",
        "companyId": "$companyId",
        "brandId": "$brandId",
        "vehicleSeriesId": "$vehicleSeriesId",
        "vehiclenoCityId": "$vehiclenoCityId",
        "vehiclenoCityName": "$vehiclenoCityName",
        "vehicleNo": "$vehicleNo",
        "frameNo": "$frameNo",
        "engineNo": "$engineNo",
        "envStandard": 1,
        "modelId": "$modelId",
        "vehicleLicensemode": "",
        "vehicleModel300Name": "$vehicleModel300Name",
        "color": 10,
        "registerNo": "",
        "useNature": 0,
        "carUseType": 0,
        "vehicleRemark": "",
        "checkTime": "",
        "contractNo": "$contractNo"
        },
        "operatingInfoVo": {
        "shortModelId": "$shortModelId",
        "shortModelName": "$shortModelName",
        "businessType": 1,
        "isUCar": 0,
        "isHertz": 0,
        "isLease": 0,
        "onLineTime": "",
        "lastQuitRunTime": "",
        "handleTime": "",
        "ucarRentType": "",
        "oilVolume": None,
        "oilVolumeLatticeNum": 0,
        "orderCar": 0,
        "cityId": "",
        "nowCityId": "",
        "nowCityName": "",
        "parkCityId": "",
        "departmentId": "",
        "nowDepartmentId": "",
        "parkDeptId": "",
        "runMilesInput": "1000",
        "nextInspecteTime": "",
        "regTime": "",
        "firstLevelStatus": 100000,
        "selfFirstLevelStatus": 100000
        },
        "assetInfoVo": {
        "bussLineId": 1,
        "bussLineTime": "",
        "willBussLineId": "",
        "willBussLineTime": "",
        "checkResultName": "",
        "allocationStatusName": "",
        "isInsideScrapName": "",
        "lastApproveSaleTime": "",
        "firstTransferOwnershipTime": "",
        "vehicleNoBeforeTransfer": ""
        },
        "financeInfoVo": {
        "carOwnerId": "$carOwnerId",
        "purchasePrice": "500000",
        "registrationAndPettyExpenses": "1000",
        "taxAmount": "2000",
        "incrementTaxExpenses": "100000",
        "monthDepreciationRate": "",
        "originalValue": "603000",
        "taxInvoiceDate": "",
        "purchaseDate": "",
        "remainderPrice": "",
        "vehicleAndVesselTax": "",
        "estimatedRemainderPrice": "",
        "realHandlePrice": "",
        "handlePettyExpenses": "",
        "realSellOutPrice": "",
        "handlePettyIncrementTax": "",
        "invoiceNo": "CAR20201013"
        },
        "garageInfoVo": {
        "lastTimeAttendMile": "",
        "nextTimeAttendMile": "",
        "vehicleFrom": ""
        },
        "deviceInfoVo": {
        "gps": 0,
        "deviceNo": "",
        "deviceType": ""
        },
        "noInfoPo": {
        "vehicleNoColor": 0
        },
        "colorPo": {
        "interiorColorId": ""
        },
        "modifyEmpName": None,
        "createEmpName": None,
        "createTime": None,
        "modifyTime": None
        }



        env = {
        "baseInfoVo": {
        "vehicleId": "",
        "companyId": 46,
        "brandId": 67,
        "vehicleSeriesId": 560,
        "vehiclenoCityId": 1,
        "vehiclenoCityName": "北京",
        "vehicleNo": "京J12362",
        "frameNo": "CAR20201013165702",
        "engineNo": "CAR20201013165702",
        "envStandard": 1,
        "modelId": 1221,
        "vehicleLicensemode": "",
        "vehicleModel300Name": "",
        "color": 10,
        "registerNo": "",
        "useNature": 0,
        "carUseType": 0,
        "vehicleRemark": "",
        "checkTime": "",
        "contractNo": "CAR20201013165702"
        },
        "operatingInfoVo": {
        "shortModelId": 1103,
        "shortModelName": "宝马BMW9/三厢/2.8自动",
        "businessType": 1,
        "isUCar": 0,
        "isHertz": 0,
        "isLease": 0,
        "onLineTime": "",
        "lastQuitRunTime": "",
        "handleTime": "",
        "ucarRentType": "",
        "oilVolume": None,
        "oilVolumeLatticeNum": 0,
        "orderCar": 0,
        "cityId": "",
        "nowCityId": "",
        "nowCityName": "",
        "parkCityId": "",
        "departmentId": "",
        "nowDepartmentId": "",
        "parkDeptId": "",
        "runMilesInput": "1000",
        "nextInspecteTime": "",
        "regTime": "",
        "firstLevelStatus": 100000,
        "selfFirstLevelStatus": 100000
        },
        "assetInfoVo": {
        "bussLineId": 1,
        "bussLineTime": "",
        "willBussLineId": "",
        "willBussLineTime": "",
        "checkResultName": "",
        "allocationStatusName": "",
        "isInsideScrapName": "",
        "lastApproveSaleTime": "",
        "firstTransferOwnershipTime": "",
        "vehicleNoBeforeTransfer": ""
        },
        "financeInfoVo": {
        "carOwnerId": 32,
        "purchasePrice": "500000",
        "registrationAndPettyExpenses": "1000",
        "taxAmount": "2000",
        "incrementTaxExpenses": "100000",
        "monthDepreciationRate": "",
        "originalValue": "603000",
        "taxInvoiceDate": "",
        "purchaseDate": "",
        "remainderPrice": "",
        "vehicleAndVesselTax": "",
        "estimatedRemainderPrice": "",
        "realHandlePrice": "",
        "handlePettyExpenses": "",
        "realSellOutPrice": "",
        "handlePettyIncrementTax": "",
        "invoiceNo": "CAR20201013"
        },
        "garageInfoVo": {
        "lastTimeAttendMile": "",
        "nextTimeAttendMile": "",
        "vehicleFrom": ""
        },
        "deviceInfoVo": {
        "gps": 0,
        "deviceNo": "",
        "deviceType": ""
        },
        "noInfoPo": {
        "vehicleNoColor": 0
        },
        "colorPo": {
        "interiorColorId": ""
        },
        "modifyEmpName": None,
        "createEmpName": None,
        "createTime": None,
        "modifyTime": None
        }



        # with open("D:/SoftwareInstall/pycharmworkspace/testpro0831/python_test/data/para", "w") as f:
        #     yaml.safe_dump(data=env, stream=f)
        #     f.close()

        with open("D:/SoftwareInstall/pycharmworkspace/testpro0831/python_test/data/para2", "w") as f:
            yaml.safe_dump(data=env2, stream=f)
            f.close()

