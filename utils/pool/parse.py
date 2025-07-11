def parse(data_in):
    dtp = [x.replace('data/', '') for x in data_in if x.startswith('data/')]
    dtpr1 = [x for x in dtp if "/" in x and x.endswith('.yaml')]
    dtpr2 = [x for x in dtpr1 if len(x.split('/')) == 2]
    textdict = {}
    for x in dtpr2:
        try:
            date, filename = x.split('/')
            if date in textdict:
                textdict[date].append(filename)
            else:
                textdict[date] = [filename]
        except ValueError as e:
            print(f"跳过无效路径: {x}, 错误: {e}")
    return textdict

def makeclash(dictin):
    badprotocols = ['vless']
    proxies = []
    for x in dictin:
        for y in x:
            try:
                if y in proxies:
                    pass
                else:
                    if y['type'] in badprotocols:
                        pass
                    else:
                        proxies.append(y)
            except:
                continue
    return proxies
