import requests
import xml.etree.ElementTree as elemTree


def findStocks(name):
    url = 'http://api.seibro.or.kr/openapi/service/StockSvc/getStkIsinByNmN1'

    servicekey= requests.utils.unquote('CCyHbj1LLKwj5YjI7ycFHNZJNNlRmz06H4SBg0PHzStJzHDKzYVc%2FqMWsM95qQkuUy90qT7NHjJRxDnL4DdldQ%3D%3D')

    secnNm = name

    queryParams = { 'serviceKey' : servicekey
                   , 'secnNm' : secnNm
                   , 'numOfRows' : '10'
                   , 'pageNo' : '1'
                  }

    request = requests.get(url,params=queryParams)
    tree = elemTree.fromstring(request.text)
    iter_element = tree.iter(tag="item")
    
    array=[]
    idx=1
    for i in iter_element:
        stock_dict={}
        stock_dict['eltscYn'] = i.find("eltscYn").text
        if i.find("engSecnNm") is None:
            stock_dict['engSecnNm'] = ""
        else:
            stock_dict['engSecnNm'] = i.find("engSecnNm").text
        stock_dict['isin'] = i.find("isin").text
        stock_dict['issuDt'] = i.find("issuDt").text
        stock_dict['issucoCustno']= i.find("issucoCustno").text
        stock_dict['korSecnNm']=i.find("korSecnNm").text
        stock_dict['secnKacdNm']=i.find("secnKacdNm").text
        array.append(stock_dict)
        idx+=1
    return array