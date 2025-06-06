import google.generativeai as genai
import os
from dotenv import load_dotenv

# 配置API密钥 (建议使用环境变量)
load_dotenv() # 加载 .env 文件中的环境变量
# genai.configure(api_key="YOUR_API_KEY")
# 或者从环境变量读取
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY 环境变量未设置。")
genai.configure(api_key=api_key)

# 选择模型 (实验性模型ID可能随时间变化，请查阅官方文档)
# 例如 'gemini-2.5-pro-exp-03-25' 或最新的 'gemini-2.5-pro-latest'
model = genai.GenerativeModel('gemini-2.5-pro-preview-05-06') 

# 创建文本提示
prompt = "请用简单的语言解释一下什么是神经网络，并举一个生活中的例子。"

# 发送请求并获取响应
try:
    response = model.generate_content(prompt)
    print("Gemini 2.5 Pro的回应：")
    print(response.text)
except Exception as e:
    print(f"API调用失败：{e}")

# 多轮对话示例
chat = model.start_chat(history=[])
user_message = "你好，Gemini！你今天感觉怎么样？"
print(f"\n用户：{user_message}")
response = chat.send_message(user_message)
print(f"Gemini：{response.text}")

user_message_2 = "你能帮我写一首关于春天的五言绝句吗？"
print(f"\n用户：{user_message_2}")
response = chat.send_message(user_message_2)
print(f"Gemini：{response.text}")