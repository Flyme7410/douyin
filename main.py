from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/redirect_url")
def redirect_url(url: str):
    if not url or url.strip() == "":
        raise HTTPException(status_code=400, detail="URL parameter is required and cannot be empty")

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # 加上 Referer，假装是从抖音官网点进来的
        "Referer": "https://www.douyin.com/",
        # 可选：有些时候加上 Accept-Encoding 会导致响应是 gzip，需要解压，初学者建议先去掉这个头
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type.lower():
            try:
                data = response.json()
                result = {"status_code": response.status_code, "content_type": content_type, "data": data}
            except ValueError:
                text = response.text
                return {"status_code": response.status_code, "content_type": content_type, "text": text}
        text = response.content.decode(response.encoding or "utf-8", errors="replace")
        return {"status_code": response.status_code, "content": response.headers.get("Location"), "content_type": content_type}
    except requests.RequestException as e:
        print(f"Error requesting URL: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error requesting URL: {str(e)}")