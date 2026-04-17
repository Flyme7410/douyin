# douyin

这是一个使用FastAPI构建的简单API项目。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行应用

```bash
uvicorn main:app --reload
```

应用将在 http://127.0.0.1:8000 启动。

## API端点

- `GET /`: 返回 {"Hello": "World"}
- `GET /items/{item_id}`: 返回指定item_id的项目信息，可选查询参数 q
- `GET /redirect_url?url=<URL>`: 接收一个URL参数，检查是否为空字符串，然后请求该URL并返回JSON结果，包含 `status_code`、`content_type` 和 `data` 或 `text`

## 文档

访问 http://127.0.0.1:8000/docs 查看自动生成的API文档。