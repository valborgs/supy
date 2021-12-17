import requests
import json
from datetime import date, timedelta

# 이달의 마지막 날 구하기
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)

def findNotices(st="공고중"):
    # fd = f"{date.today().year}-{date.today().month}-01"
    # ld = last_day_of_month(date.today())
    
    url = 'http://apis.data.go.kr/B552555/lhLeaseNoticeInfo1/lhLeaseNoticeInfo1'

    # servicekey = requests.utils.unquote('CCyHbj1LLKwj5YjI7ycFHNZJNNlRmz06H4SBg0PHzStJzHDKzYVc%2FqMWsM95qQkuUy90qT7NHjJRxDnL4DdldQ%3D%3D')
    servicekey = 'CCyHbj1LLKwj5YjI7ycFHNZJNNlRmz06H4SBg0PHzStJzHDKzYVc/qMWsM95qQkuUy90qT7NHjJRxDnL4DdldQ=='

    queryParams = { 'serviceKey' : servicekey
                   , 'PG_SZ' : '10' # 한페이지 결과 수
                   , 'PAGE' : '1'
                   , 'CNP_CD' : '11' # 서울 지역
                   , 'PAN_SS' : st # 공고 상태
                   , 'UPP_AIS_TP_CD' : '06' # 공고유형-임대주택
                  }

    request = requests.get(url, params=queryParams)
    tree = json.loads(request.text)
    lh_list = tree[1]['dsList']
    
    return lh_list
