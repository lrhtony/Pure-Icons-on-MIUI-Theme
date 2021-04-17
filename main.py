# -*- coding:utf-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import re, os, shutil, zipfile

print('清空缓存文件夹...')
try:
    shutil.rmtree('cache')
    print('成功')
except:
    print('文件夹不存在或其他错误')

print('Decoding apk...')
os.system('src\\apktool.bat d base.apk -o cache\\base -f')    #使用apktool解压安装包

try:
    os.makedirs('cache\\icons_dir\\res\\drawable-xxhdpi')
    print('成功创建目录！')
except:
    print('目录已存在或创建失败！')


DOMTree = xml.dom.minidom.parse('cache\\base\\res\\xml\\appfilter.xml')   #打开匹配规则文件
collection = DOMTree.documentElement
items = collection.getElementsByTagName('item')
print('规则加载成功！')

print('Cloning icons...')
for item in items:
    if item.hasAttribute('component'):
        component = item.getAttribute('component')  #获取component
        try:
            appName = re.findall('''ComponentInfo{(.*?)/''', component)[0]  #提取应用名
            print('''包名:''' + appName)
            drawable = item.getAttribute('drawable')
            iconFile_target = '''cache\\base\\res\drawable-nodpi\\''' + drawable + '.png'
            print('文件地址:' + iconFile_target)
            iconFile_destination = 'cache\\icons_dir\\res\\drawable-xxhdpi\\' + appName + '.png'
            print('复制到:' + iconFile_destination)
            shutil.copyfile(iconFile_target, iconFile_destination)
        except:
            print('pass')     #末尾的内容排掉


shutil.copytree('src\\others', 'cache\\icons_dir\\res\drawable-xxhdpi\\')    #复制文件夹以及主题中无相关图标的样式，特殊照顾
shutil.copytree('src\\icons', 'cache\\icons_dir\\')    #复制icons中的其他文件，此处的shutil.copytree模块经过改动

#添加icons_dir中的文件到icons压缩文件中，此处参考了https://www.cnblogs.com/cmnz/p/7052589.html
print('打包成icons文件...')
fp = zipfile.ZipFile('cache\\icons', mode='a')    #以追加模式打开或创建zip文件
def addFileIntoZipfile(srcDir, fp, replaceDir):
    for subPath in os.listdir(srcDir):
        subPath = os.path.join(srcDir, subPath)    #目标文件
        subpath = subPath.replace(replaceDir, '')    #替换压缩包里的路径
        if os.path.isfile(subPath):
            fp.write(subPath, subpath)   #写入文件
        elif os.path.isdir(subPath):
            fp.write(subPath, subpath)   #写入文件夹
            addFileIntoZipfile(subPath, fp, replaceDir)  #递归调用

addFileIntoZipfile('cache\\icons_dir', fp, 'cache\\icons_dir\\')
fp.close()

print('重新打包新主题文件...')
oldZip = zipfile.ZipFile('src\\Pure 轻雨.mtz', mode='r')    #打开旧主题
oldZip.extractall('cache\\Pure 轻雨_old')    #解压旧主题
shutil.copyfile('cache\\icons', 'cache\\Pure 轻雨_old\\icons')    #添加新的文件
shutil.copyfile('src\\description.xml', 'cache\\Pure 轻雨_old\\description.xml')

fp = zipfile.ZipFile('cache\\Pure 轻雨.mtz', mode='a')    #以追加模式打开或创建新的主题文件
addFileIntoZipfile('cache\\Pure 轻雨_old', fp, 'cache\\Pure 轻雨_old\\')    #调用之前的函数打包新的主题
fp.close()

print('复制新主题文件...')
shutil.copyfile('cache\\Pure 轻雨.mtz', 'Pure 轻雨.mtz')
print('完成！')
os.system('pause')
