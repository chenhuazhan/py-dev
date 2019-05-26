### 图片处理

```
pip install pillow
from PIL import Image
import numpy as np

a = np.array(Image.open('test.jpg'))
b = [255,255,255] - a
im = Image.fromarray(b.astype('uint8'))
im.save('new.jpg')
```

### [Parse Redis dump.rdb](https://github.com/sripathikrishnan/redis-rdb-tools/)

```
pip install rdbtools
> rdb --command json /var/redis/6379/dump.rdb

[{
"user003":{"fname":"Ron","sname":"Bumquist"},
"lizards":["Bush anole","Jackson's chameleon","Komodo dragon","Ground agama","Bearded dragon"],
"user001":{"fname":"Raoul","sname":"Duke"},
"user002":{"fname":"Gonzo","sname":"Dr"},
"user_list":["user003","user002","user001"]},{
"baloon":{"helium":"birthdays","medical":"angioplasty","weather":"meteorology"},
"armadillo":["chacoan naked-tailed","giant","Andean hairy","nine-banded","pink fairy"],
"aroma":{"pungent":"vinegar","putrid":"rotten eggs","floral":"roses"}}]
```

### [youtube-dl下载国外视频](https://github.com/rg3/youtube-dl/)

```
pip install youtube-dl #直接安装youtube-dl
pip install -U youtube-dl #安装youtube-dl并更新
youtube-dl "http://www.youtube.com/watch?v=-wNyEUrxzFU"
```

### [asciinema录制命令行操作](http://biezhi.me/2017/08/08/teach-you-how-to-use-asciinema.html)

```
pip3 install asciinema

asciinema rec
asciinema play https://asciinema.org/a/132560
<script type="text/javascript" src="https://asciinema.org/a/132560.js"
id="asciicast-132560" async></script>
```

### 查看对象的全部属性和方法

```
pip install pdir2
>>> import pdir,requests
>>> pdir(requests)
module attribute:
    __cached__, __file__, __loader__, __name__, __package__, __path__, __spec__
other:
    __author__, __build__, __builtins__, __copyright__, __license__, __title__,
__version__, _internal_utils, adapters, api, auth, certs, codes, compat, cookies
, exceptions, hooks, logging, models, packages, pyopenssl, sessions, status_code
s, structures, utils, warnings
special attribute:
    __doc__
class:
    NullHandler: This handler does nothing. It's intended to be used to avoid th
e
    PreparedRequest: The fully mutable :class:`PreparedRequest <PreparedRequest>
` object,
    Request: A user-created :class:`Request <Request>` object.
    Response: The :class:`Response <Response>` object, which contains a
    Session: A Requests session.
exception:
    ConnectTimeout: The request timed out while trying to connect to the remote
server.
    ConnectionError: A Connection error occurred.
    DependencyWarning: Warned when an attempt is made to import a module with mi
ssing optional
    FileModeWarning: A file was opened in text mode, but Requests determined its
 binary length.
    HTTPError: An HTTP error occurred.
    ReadTimeout: The server did not send any data in the allotted amount of time
.
    RequestException: There was an ambiguous exception that occurred while handl
ing your
    Timeout: The request timed out.
    TooManyRedirects: Too many redirects.
    URLRequired: A valid URL is required to make a request.
function:
    delete: Sends a DELETE request.
    get: Sends a GET request.
    head: Sends a HEAD request.
    options: Sends a OPTIONS request.
    patch: Sends a PATCH request.
    post: Sends a POST request.
    put: Sends a PUT request.
    request: Constructs and sends a :class:`Request <Request>`.
    session: Returns a :class:`Session` for context-management.
```

### [Python 玩转网易云音乐](https://github.com/xiyouMc/ncmbot)

```
#https://github.com/ziwenxie/netease-dl pip install netease-dl
pip install ncmbot
import ncmbot
#登录
bot = ncmbot.login(phone='xxx', password='yyy')
bot.content # bot.json()
#获取用户歌单
ncmbot.user_play_list(uid='36554272')
```

### [下载视频字幕](https://github.com/gyh1621/GetSubtitles)

```
pip install getsub
```

![clipboard.png](https://segmentfault.com/img/bVQyrj?w=764&h=394)

### [Python 财经数据接口包](https://github.com/waditu/tushare)

```
pip install tushare
import tushare as ts
#一次性获取最近一个日交易日所有股票的交易数据
ts.get_today_all()

代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率
      code    name     changepercent  trade   open   high    low  settlement \  
0     002738  中矿资源         10.023  19.32  19.32  19.32  19.32       17.56   
1     300410  正业科技         10.022  25.03  25.03  25.03  25.03       22.75   
2     002736  国信证券         10.013  16.37  16.37  16.37  16.37       14.88   
3     300412  迦南科技         10.010  31.54  31.54  31.54  31.54       28.67   
4     300411  金盾股份         10.007  29.68  29.68  29.68  29.68       26.98   
5     603636  南威软件         10.006  38.15  38.15  38.15  38.15       34.68   
6     002664  信质电机         10.004  30.68  29.00  30.68  28.30       27.89   
7     300367  东方网力         10.004  86.76  78.00  86.76  77.87       78.87   
8     601299  中国北车         10.000  11.44  11.44  11.44  11.29       10.40   
9     601880   大连港         10.000   5.72   5.34   5.72   5.22        5.20   
10    000856  冀东装备         10.000   8.91   8.18   8.91   8.18        8.10  
```

### [开源漏洞靶场](https://github.com/phith0n/vulhub)

```
# 安装pip
curl -s https://bootstrap.pypa.io/get-pip.py | python3

# 安装docker
apt-get update && apt-get install docker.io

# 启动docker服务
service docker start

# 安装compose
pip install docker-compose 
# 拉取项目
git clone git@github.com:phith0n/vulhub.git
cd vulhub

# 进入某一个漏洞/环境的目录
cd nginx_php5_mysql

# 自动化编译环境
docker-compose build

# 启动整个环境
docker-compose up -d
#测试完成后，删除整个环境
docker-compose down
```

### [北京实时公交](https://github.com/wong2/beijing_bus)

```
pip install -r requirements.txt 安装依赖
python manage.py build_cache 获取离线数据，建立本地缓存
#项目自带了一个终端中的查询工具作为例子，运行： python manage.py cli
>>> from beijing_bus import BeijingBus
>>> lines = BeijingBus.get_all_lines()
>>> lines
[<Line: 运通122(农业展览馆-华纺易城公交场站)>, <Line: 运通101(广顺南大街北口-蓝龙家园)>, ...]
>>> lines = BeijingBus.search_lines('847')
>>> lines
[<Line: 847(马甸桥西-雷庄村)>, <Line: 847(雷庄村-马甸桥西)>]
>>> line = lines[0]
>>> print line.id, line.name
541 847(马甸桥西-雷庄村)
>>> line.stations
[<Station 马甸桥西>, <Station 马甸桥东>, <Station 安华桥西>, ...]
>>> station = line.stations[0]
>>> print station.name, station.lat, station.lon
马甸桥西 39.967721 116.372921
>>> line.get_realtime_data(1) # 参数为站点的序号，从1开始
[
    {
        'id': 公交车id,
        'lat': 公交车的位置,
        'lon': 公交车位置,
        'next_station_name': 下一站的名字,
        'next_station_num': 下一站的序号,
        'next_station_distance': 离下一站的距离,
        'next_station_arriving_time': 预计到达下一站的时间,
        'station_distance': 离本站的距离,
        'station_arriving_time': 预计到达本站的时间,
    },
    ...
]
```

### [文章提取器](https://github.com/grangier/python-goose)

```
git clone https://github.com/grangier/python-goose.git
cd python-goose
pip install -r requirements.txt
python setup.py install

>>> from goose import Goose
>>> from goose.text import StopWordsChinese
>>> url  = 'http://www.bbc.co.uk/zhongwen/simp/chinese_news/2012/12/121210_hongkong_politics.shtml'
>>> g = Goose({'stopwords_class': StopWordsChinese})
>>> article = g.extract(url=url)
>>> print article.cleaned_text[:150]
香港行政长官梁振英在各方压力下就其大宅的违章建筑（僭建）问题到立法会接受质询，并向香港民众道歉。

梁振英在星期二（12月10日）的答问大会开始之际在其演说中道歉，但强调他在违章建筑问题上没有隐瞒的意图和动机。

一些亲北京阵营议员欢迎梁振英道歉，且认为应能获得香港民众接受，但这些议员也质问梁振英有
```

### [Python 艺术二维码生成器](https://github.com/sylnsfar/qrcode)

```
pip  install  MyQR
myqr https://github.com
myqr https://github.com -v 10 -l Q
```

![clipboard.png](https://segmentfault.com/img/bVQyu7?w=520&h=245)

### [伪装浏览器身份](https://github.com/hellysmile/fake-useragent)

```
pip install fake-useragent
from fake_useragent import UserAgent
ua = UserAgent()

ua.ie
# Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US);
ua.msie
# Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)'
ua['Internet Explorer']
# Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)
ua.opera
# Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11
ua.chrome
# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
```

### [美化 curl](https://github.com/reorx/httpstat)

```
pip install httpstat
httpstat httpbin.org/get
```

![clipboard.png](https://segmentfault.com/img/bVQywG?w=865&h=521)

### [python shell](https://github.com/amoffat/sh)

```
pip install sh
from sh import ifconfig
print ifconfig("eth0")
```

### [处理中文文本内容](https://github.com/isnowfy/snownlp)

```
pip install -U textblob#英文文本的情感分析
pip install snownlp#中文文本的情感分析
from snownlp import SnowNLP
text = "I am happy today. I feel sad today."
from textblob import TextBlob
blob = TextBlob(text)
TextBlob("I am happy today. I feel sad today.")
blob.sentiment
Sentiment(polarity=0.15000000000000002, subjectivity=1.0)


s = SnowNLP(u'这个东西真心很赞')

s.words         # [u'这个', u'东西', u'真心',
                #  u'很', u'赞']

s.tags          # [(u'这个', u'r'), (u'东西', u'n'),
                #  (u'真心', u'd'), (u'很', u'd'),
                #  (u'赞', u'Vg')]

s.sentiments    # 0.9769663402895832 positive的概率

s.pinyin        # [u'zhe', u'ge', u'dong', u'xi',
                #  u'zhen', u'xin', u'hen', u'zan']

s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

s.han           # u'「繁体字」「繁体中文」的叫法
                # 在台湾亦很常见。'
```

### [抓取发放代理](https://github.com/fate0/proxylist)

```
pip install -U getproxy
➜ ~ getproxy --help
Usage: getproxy [OPTIONS]

Options:
--in-proxy TEXT Input proxy file
--out-proxy TEXT Output proxy file
--help Show this message and exit.
```

- `--in-proxy` 可选参数，待验证的 proxies 列表文件
- `--out-proxy` 可选参数，输出已验证的 proxies 列表文件，如果为空，则直接输出到终端

`--in-proxy` 文件格式和 `--out-proxy` 文件格式一致

### [zhihu api](https://github.com/lzjun567/zhihu-api)

```
pip install git+git://github.com/lzjun567/zhihu-api --upgrade
from zhihu import Zhihu
zhihu = Zhihu()
zhihu.user(user_slug="xiaoxiaodouzi")

{'avatar_url_template': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_{size}.jpg',
     'badge': [],
     'name': '我是小号',
     'headline': '程序员',
     'gender': -1,
     'user_type': 'people',
     'is_advertiser': False,
     'avatar_url': 'https://pic1.zhimg.com/v2-ca13758626bd7367febde704c66249ec_is.jpg',
     'url': 'http://www.zhihu.com/api/v4/people/1da75b85900e00adb072e91c56fd9149', 'type': 'people',
     'url_token': 'xiaoxiaodouzi',
     'id': '1da75b85900e00adb072e91c56fd9149',
     'is_org': False}
```

### [Python 密码泄露查询模块](https://github.com/lauixData/leakPasswd)

```
pip install leakPasswd
import leakPasswd
leakPasswd.findBreach('taobao')
```

![clipboard.png](https://segmentfault.com/img/bVQyMN?w=1702&h=1304)

### [解析 nginx 访问日志并格式化输出](https://github.com/lebinh/ngxtop)

```
pip install ngxtop
$ ngxtop
running for 411 seconds, 64332 records processed: 156.60 req/sec

Summary:
|   count |   avg_bytes_sent |   2xx |   3xx |   4xx |   5xx |
|---------+------------------+-------+-------+-------+-------|
|   64332 |         2775.251 | 61262 |  2994 |    71 |     5 |

Detailed:
| request_path                             |   count |   avg_bytes_sent |   2xx |   3xx |   4xx |   5xx |
|------------------------------------------+---------+------------------+-------+-------+-------+-------|
| /abc/xyz/xxxx                            |   20946 |          434.693 | 20935 |     0 |    11 |     0 |
| /xxxxx.json                              |    5633 |         1483.723 |  5633 |     0 |     0 |     0 |
| /xxxxx/xxx/xxxxxxxxxxxxx                 |    3629 |         6835.499 |  3626 |     0 |     3 |     0 |
| /xxxxx/xxx/xxxxxxxx                      |    3627 |        15971.885 |  3623 |     0 |     4 |     0 |
| /xxxxx/xxx/xxxxxxx                       |    3624 |         7830.236 |  3621 |     0 |     3 |     0 |
| /static/js/minified/utils.min.js         |    3031 |         1781.155 |  2104 |   927 |     0 |     0 |
| /static/js/minified/xxxxxxx.min.v1.js    |    2889 |         2210.235 |  2068 |   821 |     0 |     0 |
| /static/tracking/js/xxxxxxxx.js          |    2594 |         1325.681 |  1927 |   667 |     0 |     0 |
| /xxxxx/xxx.html                          |    2521 |          573.597 |  2520 |     0 |     1 |     0 |
| /xxxxx/xxxx.json                         |    1840 |          800.542 |  1839 |     0 |     1 |     0 |
```

### [火车余票查询](https://github.com/protream/iquery)

```
pip install iquery
 Usage:
        iquery (-c|彩票)
        iquery (-m|电影)
        iquery -p <city>
        iquery -l song [singer]
        iquery -p <city> <hospital>
        iquery <city> <show> [<days>]
        iquery [-dgktz] <from> <to> <date>

    Arguments:
        from             出发站
        to               到达站
        date             查询日期

        city             查询城市
        show             演出的类型
        days             查询近(几)天内的演出, 若省略, 默认15

        city             城市名,加在-p后查询该城市所有莆田医院
        hospital         医院名,加在city后检查该医院是否是莆田系


    Options:
        -h, --help       显示该帮助菜单.
        -dgktz           动车,高铁,快速,特快,直达
        -m               热映电影查询
        -p               莆田系医院查询
        -l               歌词查询
        -c               彩票查询

    Show:
        演唱会 音乐会 音乐剧 歌舞剧 儿童剧 话剧
        歌剧 比赛 舞蹈 戏曲 相声 杂技 马戏 魔术
```

### [电脑之间传文件](https://github.com/warner/magic-wormhole/blob/master/README.md)

```
pip install magic-wormhole
Sender:

% wormhole send README.md
Sending 7924 byte file named 'README.md'
On the other computer, please run: wormhole receive
Wormhole code is: 7-crossover-clockwork
 
Sending (<-10.0.1.43:58988)..
100%|=========================| 7.92K/7.92K [00:00<00:00, 6.02MB/s]
File sent.. waiting for confirmation
Confirmation received. Transfer complete.
Receiver:

% wormhole receive
Enter receive wormhole code: 7-crossover-clockwork
Receiving file (7924 bytes) into: README.md
ok? (y/n): y
Receiving (->tcp:10.0.1.43:58986)..
100%|===========================| 7.92K/7.92K [00:00<00:00, 120KB/s]
Received file written to README.md
```

### [Python 数据可视化](https://github.com/chenjiandongx/pyecharts)

```
pip install pyecharts
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()#在根目录下生成一个 render.html 的文件,用浏览器打开
#pyecharts制作词云图
from pyecharts import WordCloud

wordlist = ['Sam', 'Club','Macys', 'Amy Schumer', 'Jurassic World', 'Charter','Communications','Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp','Lena Dunham', 'Lewis', 'Hamilton','KXAN', 'Mary Ellen Mark', 'Farrah','Abraham','Rita Ora', 'Serena Williams', 'NCAA', ' baseball',' tournament','Point Break']

#对应于wordlist中每个元素的词频
freq = [10000, 6181, 6000, 4386, 4055, 2467, 2244, 1898, 1484, 1112,1112,1112, 965, 847, 847, 555, 555,555,550, 462, 366, 360, 282, 273, 265]

#设置图标尺寸大小 
wordcloud = WordCloud(width=1000, height=620)

wordcloud.add(name="", 
              attr=wordlist, 
              shape='circle', 
              value=freq, 
              word_size_range=[20, 100])

#notebook上渲染出词云图
wordcloud

#将词云图渲染并保存到html文件中
#wordcloud.render(path='词云图.html')



freq = [7000, 6181, 6000, 4386, 4055, 2467, 2244, 1898, 1484, 1112,1112,1112, 965, 847, 847, 555, 555,555,550, 462, 366, 360,299, 10000, 7000]

wordcloud = WordCloud(width=1000, height=620)

wordcloud.add(name="", 
              attr=wordlist, 
              shape='star', 
              value=freq, 
              word_size_range=[20, 100])

wordcloud
```

![clipboard.png](https://segmentfault.com/img/bVRpF3?w=824&h=390)

### [微信公众号爬虫接口](https://github.com/Chyroc/WechatSogou)

```
pip install wechatsogou
from wechatsogou import *
wechats = WechatSogouApi()
name = '南京航空航天大学'
wechat_infos = wechats.search_gzh_info(name)
```

### [优雅的重试](http://tenacity.readthedocs.io/en/latest/)

```
pip install tenacity 
#限制重试次数为3次
from tenacity import retry, stop_after_attempt
@retry(stop=stop_after_attempt(3))
def extract(url):
    info_json = requests.get(url).content.decode()
    info_dict = json.loads(info_json)
    data = info_dict['data']
    save(data)
```

### [查找IP地址归属地](https://pypi.python.org/pypi/qqwry-py3)

```
pip install qqwry-py3 
from qqwry import QQwry 
q = QQwry() 
q.load_file('qqwry.dat', loadindex=False) 
result = q.lookup('8.8.8.8') 
```

### [导出 python 库列表](https://github.com/bndr/pipreqs)

```
#pip freeze 导出当前环境中所有的 python 库列表
$ pip install pipreqs
$ pipreqs /home/project/location
Successfully saved requirements file in /home/project/location/requirements.txt
```

### [Google Chrome Dev Protocol](https://github.com/fate0/pychrome)

```
pip install -U pychrome
google-chrome --remote-debugging-port=9222
# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

# list all tabs (default has a blank tab)
tabs = browser.list_tab()

if not tabs:
    tab = browser.new_tab()
else:
    tab = tabs[0]


# register callback if you want
def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))

tab.Network.requestWillBeSent = request_will_be_sent

# call method
tab.Network.enable()
# call method with timeout
tab.Page.navigate(url="https://github.com/fate0/pychrome", _timeout=5)

# 6. wait for loading
tab.wait(5)

# 7. stop tab (stop handle events and stop recv message from chrome)
tab.stop()

# 8. close tab
browser.close_tab(tab)
```

### [模糊搜索](https://github.com/seatgeek/fuzzywuzzy)

```
pip install fuzzywuzzy
>>> from fuzzywuzzy import fuzz
>>> from fuzzywuzzy import process
>>> fuzz.ratio("this is a test", "this is a test!")
    97
    >>> choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
>>> process.extract("new york jets", choices, limit=2)
    [('New York Jets', 100), ('New York Giants', 78)]
>>> process.extractOne("cowboys", choices)
    ("Dallas Cowboys", 90)
```

### [算法学习](https://github.com/OmkarPathak/pygorithm)

```
from pygorithm.sorting import bubble_sort
myList = [12, 4, 3, 5, 13, 1, 17, 19, 15]
sortedList = bubble_sort.sort(myList)
print(sortedList)
[1, 3, 4, 5, 12, 13, 15, 17, 19]
```

### [命令行洪流搜索程序](https://kryptxy.github.io/torrench/)

```
pip install torrench --upgrade
$ torrench "ubuntu desktop 16.04"    ## Search Linuxtracker for Ubuntu Desktop 16.04 distro ISO
$ torrench "fedora workstation"    ## Search for Fedora Workstation distro ISO
$ torrench -d "opensuse" ## Search distrowatch for opensuse ISO
$ torrench -d "solus" ## Search distrowatch for solus ISO
```

![clipboard.png](https://segmentfault.com/img/bVTMvo?w=1055&h=646)

### [根据姓名来判断性别](https://github.com/observerss/ngender)

```
pip install ngender
$ ng 赵本山 宋丹丹
name: 赵本山 => gender: male, probability: 0.9836229687547046
name: 宋丹丹 => gender: female, probability: 0.9759486128949907
>>> import ngender
>>> ngender.guess('赵本山')
('male', 0.9836229687547046)
```

### [Python编写的简单的微信客户端](https://github.com/justdoit0823/pywxclient)

```
#https://github.com/pavlovai/match
pip install pywxclient
pip install git+https://github.com/justdoit0823/pywxclient
>>> from pywxclient.core import Session, SyncClient

>>> s1 = Session()

>>> c1 = SyncClient(s1)

>>> c1.get_authorize_url()  # Open the url in web browser

>>> c1.authorize()  # Continue authorize when returning False

>>> c1.login()

>>> c1.sync_check()

>>> msgs = c1.sync_message()  # Here are your wechat messages

>>> c1.flush_sync_key()
```

### [比较相似图片](http://image-match.readthedocs.io/en/latest/start.html)

```
$ pip install numpy
$ pip install scipy
$ pip install image_match
from image_match.goldberg import ImageSignature
gis = ImageSignature()
a = gis.generate_signature('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg/687px-Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
b = gis.generate_signature('https://pixabay.com/static/uploads/photo/2012/11/28/08/56/mona-lisa-67506_960_720.jpg')
gis.normalized_distance(a, b)
```

### [身份证识别OCR](https://github.com/isee15/Card-Ocr)

### [生成各类虚拟数据](https://github.com/lk-geimfari/mimesis)

```
pip install mimesis
>>> import mimesis
>>> person = mimesis.Personal(locale='en')

>>> person.full_name(gender='female')
'Antonetta Garrison'

>>> person.occupation()
'Backend Developer'
```

### [视频处理库](https://github.com/Zulko/moviepy)

```
from moviepy.editor import *

video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...
```

### [微信聊天记录导出、分析工具](https://github.com/humiaozuzu/wechat-explorer)

```
pip install wechat-explorer
wexp list_chatrooms ../Documents user_id
wexp list_friends ../Documents user_id
wexp get_chatroom_stats ../Documents user_id chatroom_id@chatroom 2015-08-01 2015-09-01
wexp export_chatroom_records ../Documents user_id chatroom_id@chatroom 2015-10-01 2015-10-07 ../
wexp get_friend_label_stats ../Documents user_id
wkhtmltopdf --dpi 300 records.html records.pdf
```

### [图片爬虫库](http://icrawler.readthedocs.io/en/latest/install.html)

```
pip install icrawler
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': 'your_image_dir'})
google_crawler.crawl(keyword='sunny', offset=0, max_num=1000,
                     date_min=None, date_max=None,
                     min_size=(200,200), max_size=None)
bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': 'your_image_dir'})
bing_crawler.crawl(keyword='sunny', offset=0, max_num=1000,
                   min_size=None, max_size=None)
baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'your_image_dir'})
baidu_crawler.crawl(keyword='sunny', offset=0, max_num=1000,
                    min_size=None, max_size=None)
from icrawler.builtin import GreedyImageCrawler

storage= {'root_dir': '/'}
greedy_crawler = GreedyImageCrawler(storage=storage)
greedy_crawler.crawl(domains='http://qq.com', 
                     max_num=6)
```

### Python 剪贴板

```
pip install pyperclip  
from pyperclip import copy, paste 

copy('2333') # 向剪贴板写入 2333 

paste() # 值为剪贴板中的内容 
```

### [获取图片的相似度](https://github.com/ageitgey/face_recognition)

```
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
```

![clipboard.png](https://segmentfault.com/img/bVYi2C?w=563&h=366)

### 浏览器自动化splinter

```
#chromedriver.storage.googleapis.com/index.html
>>> from splinter.browser import Browser

>>> xx = Browser(driver_name="chrome")

>>> xx.visit("http://www.zhihu.com/")
```

### [为SQLite数据库生成JSON](https://github.com/simonw/datasette)

```
pip3 install datasette
datasette serve path/to/database.db
http://localhost:8001/History/downloads.json
```

### [numpy 接口直接工作在 CUDA](https://cupy.chainer.org/)

```
>>> import cupy as cp
>>> x = cp.arange(6).reshape(2, 3).astype('f')
>>> x
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.]], dtype=float32)
>>> x.sum(axis=1)
array([  3.,  12.], dtype=float32)
```

### [了解一个命令或程序在执行前会做什么](https://linux.cn/article-9131-1.html)

```
pip install maybe
maybe rm -r ostechnix/
maybe has prevented rm -r ostechnix/ from performing 5 file system operations:
 delete /home/sk/inboxer-0.4.0-x86_64.AppImage
 delete /home/sk/Docker.pdf
 delete /home/sk/Idhayathai Oru Nodi.mp3
 delete /home/sk/dThmLbB334_1398236878432.jpg
 delete /home/sk/ostechnix
Do you want to rerun rm -r ostechnix/ and permit these operations? [y/N] y
```

### [获取ip](https://github.com/cls1991/ng)

```
pip install ng
$ ng ip

local_ip:192.168.1.114
public_ip:49.4.160.250
$ ng wp
$ ng wp flyfish_5g

flyfish_5g:hitflyfish123456
```

### [图床服务](https://github.com/cls1991/qu)

```
$ pip install qu
$ qu up /somewhere/1.png
$ qu up /somewhere/1.png 2.png
```

### [get .gitignore](https://github.com/cls1991/gy)

```
#https://www.gitignore.io/
$ pip install gy
$ gy generate python java lisp
```

### [PyGithub](http://pygithub.github.io/PyGithub/v1/index.html)

```
pip install PyGithub
from github import Github

g = Github("xxxxx", "passwd")
my_forks = []
for repo in g.get_user().get_repos():
    if repo.fork:
        my_forks.append(repo)
        
```

### [爬虫小工具](https://github.com/Ehco1996/lazySpider)

```
pip install lazyspider
from lazyspider.lazyheaders import LazyHeaders

# 注意！字符串要包裹在 三引号 或 双引号 里
curl = "curl 'https://pypi.python.org/pypi' -H 'cookie: .....balabala...."

lh = LazyHeaders(curl)

headers = lh.getHeaders()
cookies = lh.getCookies()

print('*' * 40)
print('Headers: {}'.format(headers))
print('*' * 40)
print('Cookies: {}'.format(cookies))
print('*' * 40)

import requests
r = requests.get('https://pypi.python.org/pypi',
                 headers=headers, cookies=cookies)
print(r.status_code)
```

### [中文近义词工具包](https://github.com/huyingxi/Synonyms)



```
pip install -U synonyms
>>> synonyms.display("飞机")
'飞机'近义词：
  1. 架飞机:0.837399
  2. 客机:0.764609
  3. 直升机:0.762116
  4. 民航机:0.750519
  5. 航机:0.750116
  6. 起飞:0.735736
  7. 战机:0.734975
  8. 飞行中:0.732649
  9. 航空器:0.723945
  10. 运输机:0.720578
```



[原文](https://segmentfault.com/a/1190000010103386)