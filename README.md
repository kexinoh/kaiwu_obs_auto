# kaiwu_obs_auto
使用obs批量录制视频

kaiwu_obs_auto 配置与使用指南
简介
本指南将帮助您下载并配置 OBS Studio，以及如何使用  kaiwu_obs_auto 插件进行远程控制。

安装步骤

## 1. 下载 OBS Studio

请前往 OBS 官方网站 下载适合您操作系统的 OBS Studio 版本:https://obsproject.com/download

## 2. 启动 OBS Studio 并配置 obs-websocket

安装完成后，启动 OBS Studio。

打开“工具”菜单，选择“obs-websocket 设置”。

在设置对话框中，根据需要启用或禁用身份验证，并设置密码。如果启用身份验证，请确保记住设置的密码，后续操作将需要使用。【也可以选择不设置密码】

![image](https://github.com/user-attachments/assets/240a6c22-168d-4dca-84e2-2a3a731d4e09)

导入hok.json
![image](https://github.com/user-attachments/assets/bd113480-b8e7-4410-ab93-7c35b0f7bdf5)

你可能要在场景集合中选择“未命名2”

当这里为hok的时候则正确。

这一步也可以手动操作，需要你先启动一次SGame.exe，然后选择对应的即可。
![image](https://github.com/user-attachments/assets/33e8bba4-593d-4929-b594-ff973088d531)


## 3. 下载录像文件

在任务明细处下载所有的录像文件。

解压下载的文件。

将解压后的目录地址复制下来，以便后续配置使用。
![image](https://github.com/user-attachments/assets/8199329e-c8ef-445c-ac33-fa2533722a1f)

## 4.配置地址
```
# OBS WebSocket服务器的配置
host = 'localhost'
port = 14454   #自定义
password = ''
process_name = "SGame.exe"
src_dir = "battle-86055-abs-xxx"  ##包含obs录像的压缩包的文件夹目录。  【在任务明细处可以下载所有的录像，解压之后，把目录地址复制过来。】
dest_dir = r"XXXXXX\ABSParsingTool_hok_g_shelled_v1.0.1\PC\auto_replay"  ##auto_replay的地址，也就是王者荣耀的auto_replay地址
process_path = r"XXXXXX\ABSParsingTool_hok_g_shelled_v1.0.1\PC\SGame.exe"  ##输入你的SGame地址
```
## 5. 运行 main.py
配置完成后，运行即可。注意，不要将sgame的窗口最小化。可以放在晚上睡觉之后自动运行。

## 常见问题。

问题一：无法连接到 obs-websocket 插件。

解决方法：请检查是否正确配置了服务器地址和密码，并确保 OBS Studio 正在运行。

问题二：录像文件在哪里。

解决方法：点击文件-->显示录像。
