import os
import time
import zipfile
import psutil
import subprocess

##pip install obs-websocket-py

from obswebsocket import obsws, requests

# OBS WebSocket服务器的配置
host = 'localhost'
port = 14454   #自定义
password = ''
process_name = "SGame.exe"
src_dir = "battle-86055-abs-wp98J"  ##包含obs录像的压缩包的文件夹目录。  【在任务明细处可以下载所有的录像，解压之后，把目录地址复制过来。】
dest_dir = r"XXXXXX\ABSParsingTool_hok_g_shelled_v1.0.1\PC\auto_replay"  ##auto_replay的地址，也就是王者荣耀的auto_replay地址
process_path = r"XXXXXX\ABSParsingTool_hok_g_shelled_v1.0.1\PC\SGame.exe"  ##输入你的SGame地址

def start_process(process_path):
    subprocess.Popen(process_path)


def start_obs():
    # 创建一个WebSocket连接
    ws = obsws(host, port, password)
    ws.connect()
    # 启动场景
    ws.call(requests.SetCurrentScene())  
    print("OBS已启动并切换到场景")
    ws.call(requests.StartRecord())  # 开始录制
    print("已经启动录制")
    monitor_process(ws)


def monitor_process(ws):
    while True:
        if not check_process_running(process_name):
            print(f"{process_name} 已结束，正在断开OBS...")
            stop_obs(ws)
            break
        time.sleep(1)


def check_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False


def stop_obs(ws):
    ws.call(requests.StopRecord())
    print("录制已停止")
    ws.disconnect()


if __name__ == "__main__":


    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"源目录 {src_dir} 不存在。")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    items = os.listdir(src_dir)
    zip_files = [item for item in items if item.endswith('.zip')]

    total_files_unzipped = 0
    for zip_file in zip_files:
        folder_name = zip_file[:-4]
        print(f"开始启动{folder_name}对局")
        folder_path = os.path.join(dest_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        with zipfile.ZipFile(os.path.join(src_dir, zip_file), 'r') as zip_ref:
            zip_ref.extractall(folder_path)

        # 启动SGame.exe
        start_process(process_path)

        start_obs()
