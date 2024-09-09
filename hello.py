import json
import pandas as pd
import requests

# 创建JSON数据结构
data = {
    "名字": ["张三", "李四", "王五"],
    "年龄": [25, 30, 35],
    "城市": ["北京", "上海", "广州"],
}

another_piece_of_data = {
    "name": ["a", "b", "c"],
    "age": [1, 2, 3],
    "city": ["a", "b", "c"],
}

# 创建pandas DataFrame
df = pd.DataFrame(another_piece_of_data)

# 打印DataFrame
print(df)

# 将DataFrame转换为JSON
json_data = df.to_json(orient="records", force_ascii=False)

# 打印JSON数据
print(json_data)

# 发送JSON数据到外部API
api_url = "https://jsonplaceholder.typicode.com/posts"  # 替换为实际的API端点
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(api_url, data=json_data, headers=headers)
    response.raise_for_status()
    print("数据成功发送到API")

    # 打印响应状态码
    print(f"响应状态码: {response.status_code}")

    # 打印响应的JSON内容
    print("响应JSON内容:")
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))

except requests.exceptions.RequestException as e:
    print(f"发送数据到API时出错: {e}")
