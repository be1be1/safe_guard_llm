# 配置文件

# 摄像头配置
PEOPLE_CAMERA_STREAMS = [
    {"url": "rtsp://example.com/camera1", "id": "cam001", "location": "入口"},
    {"url": "rtsp://example.com/camera2", "id": "cam002", "location": "主通道"},
]

VEHICLE_CAMERA_STREAMS = [
    {"url": "rtsp://example.com/camera3", "id": "cam003", "location": "停车场入口"},
    {"url": "rtsp://example.com/camera4", "id": "cam004", "location": "停车场出口"},
]

# 传感器配置
TEMPERATURE_SENSORS = [
    {"id": "temp001", "location": "主馆"},
    {"id": "temp002", "location": "副馆"},
]

SMOKE_SENSORS = [
    {"id": "smoke001", "location": "主馆"},
    {"id": "smoke002", "location": "副馆"},
]

# AI模型配置, 也可以使用dotenv配置
AI_MODEL_API_URL = "https://api.example.com/ai-model"
AI_MODEL_API_KEY = "your_api_key_here"

# 数据处理配置
DATA_PROCESSING_INTERVAL = 10  # 秒
DECISION_MAKING_INTERVAL = 600  # 秒 (10分钟)

# 数据库配置
DATABASE_URL = "postgresql://user:password@localhost/stadium_security"

