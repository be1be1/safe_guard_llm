from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class CameraData:
    timestamp: str
    camera_ip: str
    camera_id: str
    location: str
    data: Dict[str, Any]

@dataclass
class SensorData:
    timestamp: str
    sensor_id: str
    location: str
    sensor_type: str
    data: Dict[str, Any]

