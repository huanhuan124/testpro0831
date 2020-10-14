from httpbin.zuche_car.api.car import Car

__author__ = 'zenghuan'

import yaml
import requests
import pytest
import random


class Test_zuche_car:

    def setup(self):
        # 登录接口，每个接口调用之前都需要调用
        self.car = Car()
        self._cookies = self.car.login()
        print(self._cookies)
        self._vehicleNo = "京P" + str(random.randint(66666, 99999))
        print(self._vehicleNo)
        self._frameNo = "PYTHONCAR" + str(random.randint(11111111, 99999999))
        print(self._frameNo)
        # CAR20201013
        self._invoiceNo = "PYTHONCAR" + str(random.randint(11, 99))
        print(self._invoiceNo)
        self._header = {
            'content-type': 'application/json;charset=UTF-8',
            'Origin': 'http://carvmscoretest.zuche.com/',
            'Referer': 'http://carvmscoretest.zuche.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.'
        }




    def test_createVehicle(self):
        env = {
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

        self.car.json_to_yaml(env)
        data_yaml = self.car.get_yaml()

        data = {
            "method":"post",
            "url":"http://carvmscoretest.zuche.com/carvmscore/vehiclemanage/readyrun/vehicleReadyRunVueController/createVehicle.do_",
            "json":data_yaml,
            "cookies":self._cookies,
            "headers":self._header
        }

        # res = requests.post(url=url, json=data_yaml, headers=header, cookies=self.cookies)
        res = self.car.send(data)
        print(res.text)







