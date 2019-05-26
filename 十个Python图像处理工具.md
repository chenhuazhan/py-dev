**1. scikit-image**

scikit-image是一个与NumPy数组一起使用的开源Python包。它实现了用于研究，教育和行业应用的算法和实用程序。它是一个相当简单直接的库，即使对那些不熟悉Python生态系统的人也是如此。代码质量高，经过同行评审，由一个活跃的志愿者社区编写。

**资源**

scikit-image文档丰富，有很多示例和实际使用方法。

**用法**

该包通过**skimage**导入，大多数功能可以在子模块中找到。

图像过滤：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bpk1WcncalZu6MVEYFfvksjEdQOjNmmC8IGkgU0jiaWkK3QpMAvibkYuw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4b0UdrXmalsAK2nUCDd54oBwQLBYqxf7uVSicBlNaSudw2ZTx2fgUO97w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

使用match_template函数进行模板匹配：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bbLHPRF7VJOOUWDT4PVgzjSib3U34fKFAJJicGJQSFGJlzdksdoD4zpXw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

你可以在gallery中找到更多的例子。

**2. NumPy**

NumPy是Python编程中的核心库之一，并为数组提供支持。图像本质上是包含数据点像素的标准NumPy数组。因此，通过使用基本的NumPy操作（如slicing，masking和fancy indexing），您可以修改图像的像素值。可以使用 **skimage**加载图像并使用 Matplotlib显示。

**资源**

NumPy的官方文档页面提供了完整的资源和文档列表。

**用法**

使用Numpy来mask图片：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bQciczL5J7D5QiafialnGcDwibBmJYXf3dxWVXC5sXLJcHkXjmK14qp5kbg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bXwKgTfMBY2EDgQicPXfXg6pk0uDiaUC64YI9guAkoRdibKHWU2bwvD61A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**3. SciPy**

SciPy是Python的另一个核心科学模块（如NumPy），可用于基本的图像操作和处理任务。特别是，子模块 scipy.ndimage（在SciPy v1.1.0中）提供了在n维NumPy数组上运行的函数。该软件包目前包括线性和非线性滤波，二进制形态，B样条插值和对象测量等功能。

**资源**

有关scipy.ndimage包所提供的完整功能列表，请参阅文档。

**用法**

使用SciPy通过高斯滤波器进行模糊

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4byzcAPVaCBWiaF8rs5lD5MnInqzNv1Vj5IVgYyfriclXXvL2dss1Jen1w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bHOBzqEPIa49zIibBiay2m7AF6btcohHC34m1ODU0olnJt7hdELdVVhQQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**4. PIL/Pillow**

**PIL**（Python Imaging Library）是一个免费的Python编程语言库，它增加了对打开，操作和保存许多不同图像格式的支持。然而，它的发展停滞不前，其最后一版发布于2009年。幸运的是，Pillow是一个积极开发的PIL分支，它更易于安装，可在所有主流操作系统上运行，并支持Python 3。该库包含基本图像处理功能，包括点操作，使用一组内置卷积内核进行过滤以及颜色空间转换。

**资源**

文档包含安装说明以及涵盖库的每个模块的示例。

**用法**

使用ImageFilter增强Pillow中的图像：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bUnNT0cic41DGMLlCAZVvD3cGib25icxFtGfuEz0uBrVKiaS42jGWKu6GxQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**5. OpenCV-Python**

**OpenCV**（Open Source Computer Vision Library）是计算机视觉应用中使用最广泛的库之一。OpenCV-Python是OpenCV的Python API。因为后台由C / C ++编写的代码组成，OpenCV-Python速度很快快，但它也很容易编码和部署（由于前端的Python包装器）。这使其成为执行计算密集型计算机视觉程序的绝佳选择。

**资源**

通过OpenCV2-Python-Guide可以很容易上手OpenCV-Python

**用法**

使用OpenCV-Python中的 Image Blending using Pyramids创建一个“Orapple”：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bic0Qgcic59p8NrDib9Y1eEDneViauc6QjIfyeN2JpBfwvd1RHAggAibJVRg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**6. SimpleCV**

SimpleCV是另一个用于构建计算机视觉应用程序的开源框架。它提供访问几个高性能计算机视觉库，如OpenCV，的接口，但无需了解位深度，文件格式，色彩空间等。它的学习曲线远小于OpenCV，并且（如其标语所示），“它令计算机视觉变得简单。”支持SimpleCV的一些观点是：

即使是初学者也可以编写简单的机器视觉测试

摄像机，视频文件，图像和视频流都可以互操作

**资源**

很容易按照官方文档的指导进行操作，并有大量的示例和用例可供遵循。

**用法**

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bztH8aZurvgkPlkleBDKjA13V8XibPJncGzO0kXuB6uJic1yQhtbnAOcg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**7. Mahotas**

Mahotas是另一个用于Python的计算机视觉和图像处理库。它包含传统的图像处理功能，如过滤和形态操作，以及用于特征计算的更现代的计算机视觉功能，包括兴趣点检测和局部描述符。使用Python编写接口，适用于快速开发，但算法是用C ++实现的，并且针对速度进行了优化。Mahotas库运行快速，代码简约，依赖性小。阅读其官方文章以获得更多了解。

**资源**

文档包含安装说明，示例，甚至一些教程帮助您轻松开始使用Mahotas。

**用法**

Mahotas库依靠简单的代码来完成工作。例如，使用最少量的代码Finding Wally问题就可以很好地解决。

解决Finding Wally问题:

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bo8fvITMx9HiaibncicI2ytBroXjNKQaoJwAMOlCrgUaVoRmPJWwibT5Rfg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bnficxnLWNqxjLsobkuezyMwVBpeVmuELZoQozYRL6a4ZzvPGsjQf8cQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**8. SimpleITK**

ITK（Insight Segmentation and Registration Toolkit）是一个“开源，跨平台系统，为开发人员提供了一套用于图像分析的广泛软件工具。SimpleITK是一个基于ITK构建的简化层，旨在促进其在快速原型设计，交易以及解释语言方面的应用。”它也是一个图像分析工具包，具有大量组件，支持一般过滤操作，图像分割和配准。SimpleITK是用C ++编写的，但它可用包括Python在内的大量编程语言进行操作。

**资源**

有大量的Jupyter Notebook说明了SimpleITK在教育和研究活动中的应用。Notebooks使用Python和R编程语言演示如何使用SimpleITK进行交互式图像分析。

**用法**

使用SimpleITK和Python创建可视化的严格CT / MR配准过程：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4buniaSdsrbx3x1NtPauBC1uBhsgLicQsaCOicH6mfV61ZicRjBXeibprEAgg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**9. pgmagick**

pgmagick是基于Python的GraphicsMagick库的包装器。GraphicsMagick图像处理系统，有时也被称为图像处理的瑞士军刀。其强大而高效的工具和库集合支持在超过88种主要格式（包括DPX，GIF，JPEG，JPEG-2000，PNG，PDF，PNM和TIFF）上读取，写入和操作图像。

**资源**

pgmagick的GitHub respository有安装说明和要求。还有一个详细的用户指南。

**用法**

图像缩放：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bJXOSMeZzNxR6ZkWPOo6YiaCPrFw3W0GSNv3ziap1eBa9dwemgjS02z9A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

边缘提取：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bEzmvAeoMB8NRgkxFVficCPTMQ0lAH8EIFSnuKRwb8ywXswJFp95dQug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**10. Pycairo**

Pycairo是Cairo图形库的一组Python绑定。Cairo是一个用于绘制矢量图形的2D图形库。矢量图形很有趣，因为它们在调整大小或变换时不会失去清晰度。Pycairo可以从Python调用Cairo命令。

**资源**

Pycairo GitHub respository是一个很好的资源，包含有关安装和使用的详细说明。还有一个入门指南，有一个关于Pycairo的简短教程。

**用法**

用Pycairo绘制线条，基本形状和径向渐变：

![img](https://mmbiz.qpic.cn/mmbiz_png/GJM4P9zwRq8SLXae4aHAYBGkEcDOJa4bKQJghvjTic4zRlIFsl1XnlKhfyncnCZR4q0rtRICkb9ATfkXQPAW0yA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**结论**

这些是Python中一些有用且免费提供的图像处理库。有些是众所周知的，有些可能对你来说是新的。尝试一下它们以了解更多关于它们的信息！



[原文](http://mp.weixin.qq.com/s?__biz=MjM5NTY1MjY0MQ==&mid=2650745524&idx=4&sn=a47acb39374fca17a7fd3a1308ba7e3b&chksm=befebffa898936ec06d44a25c81d353b6626847db932a42ebf33f8125c9c5524dd0805dd5c74&scene=0&xtrack=1#rd)