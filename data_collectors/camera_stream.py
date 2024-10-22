import cv2
import json
import time
from datetime import datetime
import numpy as np

class CameraStream:
    def __init__(self, url, camera_id, location, stream_type):
        self.url = url
        self.camera_id = camera_id
        self.location = location
        self.stream_type = stream_type
        self.cap = cv2.VideoCapture(url)

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        if self.stream_type == "people":
            data = self.detect_people(frame)
        elif self.stream_type == "vehicle":
            data = self.detect_vehicles(frame)
        else:
            raise ValueError("Invalid stream type")

        return self.format_data(data)

    def detect_people(self, frame):
        # 这里应该使用实际的人流检测算法
        # 为了示例，我们只返回一个随机数
        return {"count": np.random.randint(0, 100)}

    def detect_vehicles(self, frame):
        # 这里应该使用实际的车流检测和车牌识别算法
        # 为了示例，我们只返回一个随机车牌号
        return {"plate": f"京A{np.random.randint(10000, 99999)}"}

    def format_data(self, data):
        return json.dumps({
            "timestamp": datetime.now().isoformat(),
            "camera_ip": self.url.split("//")[1].split("/")[0],
            "camera_id": self.camera_id,
            "location": self.location,
            "data": data
        })

    def __del__(self):
        self.cap.release()

