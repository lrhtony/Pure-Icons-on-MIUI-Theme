# Pure-Icons-on-MIUI-Theme
将图标程序转为MIUI主题

## 环境
由于使用到了[apktool](https://ibotpeaches.github.io/Apktool/)，因此请提前安装好[Java SE Runtime Environment](https://www.oracle.com/cn/java/technologies/javase-jre8-downloads.html)。

另外，如果遇到了动态库缺失的情况，请尝试安装vc运行库

## 打包
由于包文件shutil的copytree不能复制到已存在的文件夹中，因此作了一定的修改，如图所示![shutil的修改](https://cdn.jsdelivr.net/gh/lrhtony/Pure-Icons-on-MIUI-Theme@master/img/shutil.jpg)

参考：https://www.cnblogs.com/fply/p/8365392.html

## 使用
- 安装好jre
- 将安装包名称改为base.apk，与程序放在同一目录下
- 如果安装包格式为apks或xapk，需将其中的base.apk解压出来放在与程序相同目录下
- 双击运行程序，等待目录下出现`Pure 轻雨.mtz`文件
- 可自定义更改软件图标，将想要替换的软件图标更改名称为软件包名后，复制到`src\others`文件夹下

## 注意
- 该程序仅适用于GooglePlay版本
- 请勿将生成的文件随意传播
- 此程序仅供学习，切勿用于非法用途
