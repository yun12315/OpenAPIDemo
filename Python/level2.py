#!python3
# -*- coding:utf-8 -*-
import time
import websocket
import zlib
import requests
import json


# 发送订阅
def on_open(ws):
    ws.send("all=lv2_SH600851")


# 接收推送
def on_message(ws, message, type, flag):
    # 命令返回文本消息
    if type == websocket.ABNF.OPCODE_TEXT:
        print(time.strftime('%H:%M:%S', time.localtime(time.time())), "Text响应:", message)
        print(time.strftime('%H:%M:%S', time.localtime(time.time())), "Text响应:", message)
    # 行情推送压缩二进制消息，在此解压缩
    if type == websocket.ABNF.OPCODE_BINARY:
        rb = zlib.decompress(message, -zlib.MAX_WBITS)
        print(time.strftime('%H:%M:%S', time.localtime(time.time())), "Binary响应:", rb.decode("utf-8"))


def on_error(ws, error):
    print(error)


def on_close(ws, code, msg):
    print(time.strftime('%H:%M:%S', time.localtime(time.time())), "连接已断开")


def get_websocket_server_info(token):
    query_url = f"http://jvquant.com/query/server?market=ab&type=websocket&token={token}"
    try:
        response = requests.get(query_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        server_info = response.json()
        if server_info and server_info.get("code") == '0' and server_info.get("server"):
            return server_info.get("server") # 直接返回完整的 WebSocket URL
        else:
            print(f"Error: Could not get server info. Response: {server_info}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching server info: {e}")
        return None, None

# 请将此处的 token 替换为您自己的 jvQuant token
JVQUANT_TOKEN = "b5a4cb77a0a59b89cd672f9269ce9b8b" # 这是一个示例 token，请替换为您的实际 token

full_ws_url = get_websocket_server_info(JVQUANT_TOKEN)

if full_ws_url:
    # 将 token 添加到 URL 的查询参数中
    final_ws_url = f"{full_ws_url}?token={JVQUANT_TOKEN}"
    print(f"连接到服务器: {final_ws_url}")
    ws = websocket.WebSocketApp(final_ws_url,
                                on_open=on_open,
                                on_data=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
else:
    print("无法获取服务器地址，程序退出。")