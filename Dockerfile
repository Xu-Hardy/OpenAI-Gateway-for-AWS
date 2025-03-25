# Dockerfile

FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 安装依赖（避免重新安装时缓存失效）
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝应用代码
COPY .. .

# 指定入口：Gunicorn 启动 Flask 应用（run.py 中 app 为 Flask 实例名）
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
