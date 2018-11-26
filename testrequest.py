# -*- coding: utf-8 -*-

import json
import requests
from logger import logger

hlist = []
header = {
    "content-type": "application/json;charset=UTF-8"

}


def TestPostRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):
    hr = requests.post(hurl, data=hdata, headers=headers)
    hresult = hr.json()
    hstatus = str(hresult['status'])
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "POST",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + hstatus + "实际结果: " + str(hresult),
            "t_result": "通过"
        }
        hlist.append(hhhdata)
        logger.info("Case: " + htestcassname + " PASS")
    else:
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "POST",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + hstatus + "实际结果: " + str(hresult),
            "t_result": "失败"
        }
        hlist.append(hhhdata)
        logger.info("Case: " + htestcassname + " FAIL: " + str(hresult))


def TestGetRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):
    if hdata:
        hr = requests.get(hurl, params=hdata, headers=headers, verify=False)
    else:
        hr = requests.get(hurl, headers=headers)
    hresult = hr.text
    hstatus = "200"
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "GET",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + hstatus + "实际结果: " + str(hresult),
            "t_result": "通过"
        }
        hlist.append(hhhdata)
        logger.info("Case: " + htestcassname + " PASS")
    else:
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "GET",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + str(hstatus) + "实际结果: " + str(hresult),
            "t_result": "失败"
        }
        hlist.append(hhhdata)
        logger.info("Case: " + htestcassname + " FAIL: " + str(hresult))


def TestDeleteRequest(hurl, hdata, headers, htestcassid, htestcassname, htesthope, fanhuitesthope):
    if hdata:
        hr = requests.delete(hurl, params=hdata, headers=headers)
    else:
        hr = requests.delete(hurl, headers=headers)
    hresult = hr.json()
    hstatus = hresult['status']
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "DELETE",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + hstatus + "实际结果: " + str(hresult),
            "t_result": "通过"
        }
        logger.info("Case: " + htestcassname + " PASS")
        hlist.append(hhhdata)
    else:
        hhhdata = {
            "t_id": htestcassid,
            "t_name": htestcassname,
            "t_method": "DELETE",
            "t_url": hurl,
            "t_param": "测试数据: " + str(hdata),
            "t_hope": "status:" + htesthope + "期望结果: " + fanhuitesthope,
            "t_actual": "status" + hstatus + "实际结果: " + str(hresult),
            "t_result": "失败"
        }
        hlist.append(hhhdata)
        logger.info("Case: " + htestcassname + " FAIL: " + str(hresult))
