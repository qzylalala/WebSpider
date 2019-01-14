import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image.list')
            for image in images:
                yield{
                    'image': 'http' + image.get('url'),
                    'title': title 
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(response.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Download', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()
    groups = ([x*20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close
    pool.join()
