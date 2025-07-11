import requests
import json
import yaml
import time

def get_file_list():
    try:
        start = time.time()
        url = 'https://api.github.com/repos/changfengoss/pub/git/trees/main?recursive=1'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        rawdata = json.loads(response.text)
        data = rawdata.get('tree', [])
        dirlist = []
        for item in data:
            dirlist.append(item['path'])
        count = len(dirlist)
        end = time.time()
        print(f"Fetch changfengoss/pub succeeded in {end - start:.2f} seconds")
        return dirlist, count
    except requests.exceptions.RequestException as e:
        print(f"网络错误，无法获取 changfengoss/pub: {e}")
        return [], 0
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return [], 0
    except Exception as e:
        print(f"未知错误: {e}")
        return [], 0

def get_proxies(date, file):
    baseurl = 'https://raw.githubusercontent.com/changfengoss/pub/main/data/'
    working = yaml.safe_load(requests.get(url=baseurl+date+'/'+file).text)
    data_out = []
    for x in working['proxies']:
        data_out.append(x)
    return data_out
