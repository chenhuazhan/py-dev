**1 准备基本材料**

在**/home/ziptest/目录下**，我创建了两个文件，一个**test.zip**，是一个设置了密码的zip包，密码为456789。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaFqSwK6Wbw6GgKafoibiaGkaokx2nibCuiap67MADmfZtYsPeg8ENyJFp2g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**dict.txt文件**是一个字典文件，简单的配置了几个密码。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iayebouv9icBHxmxkicYVnFDwAgayoFYTJPwyGW2q5B6tIgebLpwaGgrgA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

下面我们打开开发工具，开始编写测试代码。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaNCic9ian4BpP78q0zGSiafTkMTh0HoLn7icdUhicfHTFib7ia3GCjbBL5zsbg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



**2 ZIPFILE**

在python中操作zip文件，最简单的方式就是使用zipfile模块，使用该模块可以用来判断一个文件是否是压缩文件，创建、解压文件，获取zip文件的元数据信息。可以使用python的help方法查看该模块的使用方法。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iado5riaicTnWrsxvaHXsnesEhC1t9Bp3098LEkMfu3K6HIBfDCLgsGxNg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaQd3JFQWhLE4sZH7bPpEOFBAZRgCgoJ4zjxyXSzYd5DXTLjhe1UPw8Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这里我们首先关注下**ZipFile类**。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaAwzuS0rvo4pNDj6ZvKNHUOPG0abkpGQWHy8yN4wlSW3AJ0iaYGZhia5g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**该类用来打开，读取，修改，解压zip文件**。我们想要操作一个zip文件，第一步就是**初始化ZipFile实例**。下面我们打开我们准备好的text.zip文件。



**import  zipfile**



```
zFile = zipfile.ZipFile("/HOME/TEST.ZIP");
```

我们只传了一个路径参数进去，从帮助文档我们可以看到，后面三个参数都有默认值，这里我们使用默认值就够了。

下面我们关注下ZipFile类的**extractall**方法。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaVsTVC3icnYnY78eA4kbcFB59mwUicKRFdWc3BgTxMLuDOvTUdfZDToGQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**extractall方法**，是把压缩包里面的内容都解压出来，三个参数，path是解压的路径，**members**是需要解压出来的文件，pwd是密码。

现在我们可以测试下文件解压了。



**import  zipfile**



```
zFile = zipfile.ZipFile("/HOME/ZIPTEST/TEST.ZIP");

zFile.extractall("/HOME/",pwd="456789");
```

运行这个脚本。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaW7pXMl4yJY0qQtWdfzEqTXlDWrpnYr104ibib9PKj2fbluuicqPoq8I5w/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

密码正确的话，会正常解压文件。如果密码不正确会出现什么情况呢？我们在代码中输入一个错误的密码。



**import  zipfile** 



```
zFile = zipfile.ZipFile("/HOME/ZIPTEST/TEST.ZIP");

zFile.extractall(path="/HOME/ZIPTEST",pwd="4567890");
```

结果如下：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4ia9LdhABEHvHictcgPNO3PIxhxSU9DTCBmfLYXqJRa4cglgiaqF2v25tew/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)**程序会抛出****“bad password”****的异常。**

**我们可以通过捕获异常，测试多个密码。**

**3  读取字典文件**

在Python中打开文件，使用**open方法**，这是一个内置方法，查看open的帮助文档，可以看到该方法的参数说明。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iauvdSs6XicPhZgYcs4HhdJc7TxUz810m1BicpIUFhpPDVS77IbUADR0lQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

open方法返回一个file对象，**利用file对象**，我们可以读取文件的具体内容。下面我们在代码中测试一下。



**import  zipfile**



```
passFile = open('/HOME/ZIPTEST/DICT.TXT');

for line in passFile.readlines():

password = line.strip('N');

print(password);
```

运行结果如下：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaLeteJG2woWN389fKE2wpia82KwsHJzomBFlS1j1F24cUa9QZRrHP6mA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

下面我们利用读取到的密码来暴力测试zip文件。



**import  zipfile**



```
zFile = zipfile.ZipFile("/HOME/ZIPTEST/TEST.ZIP");



passFile = open('/HOME/ZIPTEST/DICT.TXT');

for line in passFile.readlines():

password = line.strip('N');

try:

zFile.extractall(path="/HOME/ZIPTEST",pwd=password);

print("PASSWORD IS:"+password);

exit(0);

except:

pass;
```

在上面的代码中，我们使用try—except进行异常捕获，密码不正确的时候，程序跳过继续执行。密码正确的时候打印密码，终止程序。运行结果如下：

![img](data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg==)

到目前为止，我们的脚本已经具备了暴力破解zip文件的功能，大家可以看到只有十几行的代码。下面我们为了提升程序的可用性，重构一下这个脚本，利用函数划分功能。

 **4 重构  用函数划分功能**

首先定义一个**extractFile****函数**，该函数接收三个参数，一个**zipfile对象**，解压的目标路径，密码，如果解密成功则返回密码。

```
def extractFile(toPath,zFile,password):

try:

zFile.extractall(path=toPath,pwd=password);

return password;

except Exception,e:

return;
```

下面我们再声明一个**main方法**。

```
def main():

zFile = zipfile.ZipFile("/HOME/ZIPTEST/TEST.ZIP");

passFile = open('/HOME/ZIP/TEST/DICT.TXT');

for line in passFile.readlines():

password = line.strip('N');

guess = extractFile("/HOME/",zFile,password);

if guess:

print('SCUCESS'+password);

exit(0);
```

在**main方法**中，首先初始化了**zipfile对象**，然后打开字典文件，循环读取密码，传给**extractFile方法**调用。

分离 了两个方法之后，我们需要在程序的入口处调用**main方法**，完整代码如下：



**import  zipfile**



```
def extractFile(toPath,zFile,password):

try:

zFile.extractall(path=toPath,pwd=password);

print('SCUCESS'+password);

return password;

except Exception,e:

return;

def main():

zFile = zipfile.ZipFile("/HOME/ZIPTEST/TEST.ZIP");

passFile = open('/HOME/ZIPTEST/DICT.TXT');

for line in passFile.readlines():

password = line.strip('N');

guess = extractFile("/HOME/",zFile,password);

if guess:

print('SCUCESS'+password);

exit(0);



if __name__=='__MAIN__':

main();
```

这样一来，代码清晰了很多，但是我们更换zip文件和字典文件的时候，还是需要修改代码，很不方便，正常的程序都应该可以传递参数的，ok，下面我们引入**optparse库**。

**5 OPTPARSE**

Python 有两个内建的模块用于处理命令行参数：

一个是 **getopt**，《Deep in python》一书中也有提到，只能简单处理 命令行参数；

另一个是 **optparse**，它功能强大，而且易于使用，可以方便地生成标准的、符合**Unix/Posix规范的命令行说明。**

首先先引入**optparse模块**，然后强制添加两个参数，**zip文件名和字典文件名**。先看代码：

```
def main():

parser = optparse.OptionParser("usage%prog "+

"-f <zipfile> -d <dictFile>");

parser.add_option('-f',dest='zname',type='string',help='specify zip file');

parser.add_option('-d',dest='dname',type='string',help='specify dict file');

(options,args)=parser.parse_args();

if(options.zname==None)|(options.dname==None):

print parse.usage;

exixt(0);

else:

zname=options.zname;

dname=options.dname;



zFile = zipfile.ZipFile(zname);

passFile = open(dname);

for line in passFile.readlines():

password = line.strip(' ');

guess = extractFile("/home/",zFile,password);

if guess:

print('scucess'+password);

exit(0);
```

首先初始化一个**OptionParser对象**，然后添加两个选项——**“-f”和“-d”**。之后在程序运行的时候通过**parse_args方法**获取输入的参数，如果参数为空，则打印使用方法，退出程序。

下面使用终端来测试这个程序。

无参数情况下：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaOuiaATmTcdSAbaA0fA2V7fJCfdoxc4SHa5NPIhgPuzTibSMWr3icWkSGA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

输入参数：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5euicDIXGMhmehwuXbPAN4iaMU5ibkiaPgeWYQXc9mDKzVCdR1rDbg16o7AM21VUza2SgCw4viaKdFAYQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)