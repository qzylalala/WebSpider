import requests


def check():
        response = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2019-01-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=XFN&purpose_codes=ADULT')
        response.encoding = 'utf-8'
        result = response.json()
        return result['data']['result']


for i in check():
        tmp_list = i.split('|')
        if tmp_list[26] != '无' and tmp_list[26] != '':
                print(tmp_list[3],  '有票')
