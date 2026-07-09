import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "chatbi_mvp"),
    "charset": "utf8mb4"
}

LLM_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "base_url": os.getenv("OPENAI_BASE_URL", "https://ws-m71z8s6gl9pvodik.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"),
    "model": os.getenv("LLM_MODEL", "qwen3-max"),
    "temperature": 0.1,
    "max_tokens": 1000
}