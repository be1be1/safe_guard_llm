import json
from datetime import datetime
import random

class SensorData:
    def __init__(self, sensor_id, location, sensor_type):
        self.sensor_id = sensor_id
        self.location = location
        self.sensor_type = sensor_type

    def read_data(self):
        if self.sensor_type == "temperature":
            data = self.read_temperature()
        elif self.sensor_type == "smoke":
            data = self.read_smoke()
        else:
            raise ValueError("Invalid sensor type")

        return self.format_data(data)

    def read_temperature(self):
        # 模拟温度读数，实际应该从真实传感器读取
        return {"temperature": round(random.uniform(15, 35), 1)}

    def read_smoke(self):
        # 模拟烟雾浓度读数，实际应该从真实传感器读取
        return {"smoke_level": random.randint(0, 100)}

    def format_data(self, data):
        return json.dumps({
            "timestamp": datetime.now().isoformat(),
            "sensor_id": self.sensor_id,
            "location": self.location,
            "sensor_type": self.sensor_type,
            "data": data
        })

