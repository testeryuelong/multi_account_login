# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

def readLoginData(filePath):
    "读取登陆信息数据文件,以字典的形式返回"
    if  not os.path.exists(filePath):
        return None
    with open(filePath) as fp:
        loginInfoDict={}
        for line in fp:
            if line.strip()!="":
                info=line.strip().split("/")
                loginInfoDict[info[0]]=info[1]
    return loginInfoDict

def readStepData(filePath):
    "读取操作步骤信息数据文件"
    if  not os.path.exists(filePath):
        return None
    with open(filePath) as fp:
        dataList=[]
        for line in fp:
            lineList=line.strip().split("-->")
            dataList.append(lineList)
    return dataList



if __name__=="__main__":
    print(readStepData("step.txt"))
    print(readLoginData("loginInfo.txt"))