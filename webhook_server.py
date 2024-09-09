from fastapi import FastAPI, Request
import httpx
import uvicorn
import sys

# 创建FastAPI应用

app = FastAPI()

# 定义一个接收POST请求的路由
@app.post("/webhook")
async def receive_webhook(request: Request):
    # 获取请求体中的JSON数据
    data = await request.json()
    # 处理接收到的webhook数据
    print("Received webhook data:", data)

    # 将data中的数据全部发送到msg字段
    msg_content = str(data)

    # 接收到webhook数据后，调用 http://192.168.165.159:10010/text 接口
    # POST请求，请求体为{"msg": "你好啊","receiver": "G446853797","aters": ""}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://192.168.165.159:10010/text",
            json={"msg": msg_content, "receiver": "G446853797", "aters": ""}
        )
        print("Response from http://192.168.165.159:10010/text:", response.json())

    return {"message": "Webhook received successfully"}

# 定义一个POST请求的路由/webhook2
@app.post("/webhook2")
async def receive_webhook2(request: Request):
    # 将下面curl修改为python代码
    # curl --location 'http://118.25.45.230:10056/webhook/msg/v2?token=123456' \
    # --header 'Content-Type: application/json' \
    # --data '{
    #     "to": "鸿",
    #     "data": { "content": "你好👋" }
    # }'
    # 获取请求体中的JSON数据
    data = await request.json()
    # 处理接收到的webhook数据
    print("Received webhook data:", data)

    # 将data中的数据全部发送到msg字段
    msg_content = str(data) 
    # 接收到webhook数据后，调用 http://118.25.45.230:10056/webhook/msg/v2?token=123456 接口
    # POST请求，请求体为{"to": "鸿","data": { "content": msg_content }}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://118.25.45.230:10056/webhook/msg/v2?token=123456",
            json={"to": "鸿","data": { "content": msg_content }}
        )
        print("Response from http://118.25.45.230:10056/webhook/msg/v2?token=123456:", response.json())

    return {"message": "Webhook received successfully"}
    

# 定义一个接收POST请求的路由/msg
@app.post("/msg")
async def receive_msg(request: Request):
    # 获取请求体中的JSON数据
    data = await request.json()
    # 处理接收到的webhook数据
    print("Received msg data:", data)

    return {"message": "Msg received successfully"}

# 运行FastAPI应用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
else:
    sys.argv.append("webhook_server.py")
    uvicorn.run(app, host="0.0.0.0", port=8000)
