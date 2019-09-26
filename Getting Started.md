## 快速入门

[MicroPython官方页面](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

翻了好多相关的地方都没有介绍如何通过串口下载文件，如何重启的时候自动运行文件，而且那些教程一看就是互抄的（也可能是我搜索姿势有问题吧），现整理如下

以下指令均在安装有python的计算机上运行

注意先去设备管理器里看清楚esp32连接的是哪个串口，替换下面的`COM5`，原文`/dev/ttyUSB0`是linux系统的

1. 安装esptool<br>`pip install esptool`
1. 清除固件<br>`esptool.py --port COM5 erase_flash`
2. 刷写固件<br>`esptool.py --chip esp32 --port COM5 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin`
3. 安装文件管理工具<br>`pip install adafruit-ampy`

然后使用`ampy`相关的命令下载文件并运行就可以了

其中，esp32里面的`boot.py`是每次启动都会去运行的文件，默认内容如下

```python
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
```

把自己的程序存进去之后在`boot.py`里面`import`之后运行就ok了

例如更新`boot.py`文件：`ampy -p COM5 put mybootfile.py boot.py`，其他操作直接`ampy`看帮助

或者小程序的话直接在`boot.py`里面写也没什么大问题

如果希望使用图形界面的工具，推荐[MicroPython File Uploader](https://www.wbudowane.pl/download/)

附带一个连接wifi的方法

```python
import network
wifi=network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WiFi名称,WiFi密码)
```

## 其他文章
[MicroPython入坑记（三）板子上的Python到底有多快？](https://www.cnblogs.com/yafengabc/p/8681713.html)

