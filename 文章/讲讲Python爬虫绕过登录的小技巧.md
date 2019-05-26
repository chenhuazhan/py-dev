**前言**

很多时候我们做 Python 爬虫时或者自动化测试时需要用到 selenium 库，我们经常会卡在登录的时候，登录验证码是最头疼的事情，特别是如今的文字验证码和图形验证码。文字和图形验证码还加了干扰线，本文就来讲讲怎么绕过登录页面。

登录页面的验证，比如以下的图形验证码。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESARGmyOqiauL9ib9aNNjS40e9rSCO1YfNH0YJPFIbBdZKQOHP6icAjMSTyg/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

还有我们基本都看过的 12306 的图形验证码。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAic9vfWF7GEibxvgAR0PLm7neUiaFxgMg8LWtfBFGg0cPmY1J98Au3fv0g/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



## **绕过登录方法**

绕过登录基本有两种方法，第一种方法是登录后查看网站的 cookie，请求 url 的时候把 cookie 带上，第二种方法是启动浏览器带上浏览器的全部信息，包括添加的书签和访问网页的 cookie 信息。

第一种 cookie 方法我们要分析别人网站的 cookie 值，找出相应的值然后添加进去，对于我们不熟的网站，他们可能也会做加密或者动态处理，所以有些网站也不是那么好操作。如果是自己公司的网站需要测试，我们可以询问对应的开发那个 cookie 值是区分独立用的值，拿出来放在请求里面就行。

## **添加 cookie 绕过登录**

比如我们登录百度账号比较费劲，每次都需要登录也比较繁琐，我们 F12 打开页面调试工具，登录后找到www.baidu.com文件，在 cookie 中，我们发现很多值，其中图中圈起来的就是我们要找的值。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESARNbpZiavXIZ4pibqPtUaXGdeoBT7SzxFHU5tRT1tvhnpDT6hLibb1bSAg/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我们在访问 baidu 链接的时候加上这个 cookie 值，这样就是直接登录后的百度账号了。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAGpdRWOqfIDQl3ldNUTn61mP8fJDibpKI6DGOevb8lic3ZzEkaea84Odg/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **下载浏览器驱动**

我们要 selenium 启动浏览器时，需要下载后对应的驱动文件并放在 Python 安装的根目录下，比如我会用到谷歌 Chrome 浏览器和 Firefox 火狐浏览器。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAkvgx5KkVhVQlwMEFypECayTMIiaiaAEnqc2shWzILcyjsIjWxaVBuvug/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)谷歌浏览器驱动下载地址：

```
http://chromedriver.storage.googleapis.com/index.html
```

火狐浏览器驱动下载地址：

```
https://github.com/mozilla/geckodriver/releases/
```

## 

## **启动 Chrome 浏览器绕过登录**



我们每次打开浏览器做相应操作时，对应的缓存和 cookie 会保存到浏览器默认的路径下，我们先查看个人资料路径，以 chrome 为例，我们在地址栏输入 chrome://version/

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAo1F4YpPt5DBIDm29icISAhjp4qr5EutpdfNjQQhKpFpPtZJDcq47Few/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

图中的个人资料路径就是我们需要的，我们去掉后面的 \Default，然后在路径前加上「–user-data-dir=」就拼接出我们要的路径了。

```
profile_directory = r'--user-data-dir=C:\Users\xxx\AppData\Local\Google\Chrome\User Data'
```

接下来，我们启动浏览器的时候采用带选项时的启动，这种方式启动浏览器需要注意，运行代码前需要关闭所有的正在运行 chrome 程序，不然会报错。全部代码如下。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESALviawibAtIjUY4RLjxqgjddfjaLGDLPL3AL355mibylSROacVSal0Rn1w/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

selenium 自动化启动浏览器后我们会发现我之前保存的书签完整在浏览器上方，baidu 账号也是登录的状态。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESANqUoj3Th0M7NgCrc8Fb3xWTqtnMVWk2NRfUYHGtv8oPFMicBKQMMwXw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**启动 Firfox 浏览器****绕过登录**

Firfox 火狐浏览也可以这样启动它，设置略有不同。

首先，查看配置文件的存储路径，查看方法：帮助–故障排除信息–配置文件夹，把里面的路径复制过来就行。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAyroe7wE2OSDibFiaIhKuqJJupT307yE4hIHTrTQf5ywtgEjgNFPicicWyw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

同样，我们把路径放在变量中。

```
profile_path = <span class="hljs-string">r'C:\Users\guixianyang\AppData\Roaming\Mozilla\Firefox\Profiles\dvm6wqam.default'</span>
```

我们也在火狐浏览器中登录好百度的账号，用 selenium 自动化启动带配置文件的火狐浏览器，也会发现启动时已经启动了浏览器安装的插件和登录好的百度账号。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESAUZz8dGuuFmEld0PeSx3hhibibYCL1mbFkmSSfQnL3Weia1ZszMdwiarVxA/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **绕过图形验证码的网站**

文中第一个图是简书登录时的图形验证码，我们登录简书后（cookie 有一定的时效，貌似有 10 天半个月左右），把上面代码中的链接换成简书的，再用上面的方法觉可以实现绕过登录页的图形验证码。

比如我直接打开我的简书个人主页

```
https://www.jianshu.com/u/52353ffa8b86
```

自动化启动后也是保留了登录的状态。

![img](https://mmbiz.qpic.cn/mmbiz_png/US10Gcd0tQGY9ddd5GpbmVRuaRfuaESA4scQlDSpjtQZAicOgzaM7NFib1ib6aVLUOj8AI0f7QwsUjBMtJwCOoJSQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

网站的登录大门已被打开，接下来就可以做自己想做的事情了，比如爬虫、自动化测试验证之类的。

PS：以上技巧对有些网站可能不管用，但是对大部分网站还有适用的，觉得本文小技巧有用的自己赶紧试试吧。