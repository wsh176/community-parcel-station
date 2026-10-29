
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Parcel:
    tracking_number: str
    recipient_name: str
    phone: str
    status: str = "待取件"
    stored_at: str = ""


class ParcelManager:
    def __init__(self):
        self.parcels = {}

    def add_parcel(self, tracking_number, recipient_name, phone):
        """登记包裹入库"""
        if tracking_number in self.parcels:
            raise ValueError("该快递单号已存在")

        parcel = Parcel(
            tracking_number=tracking_number,
            recipient_name=recipient_name,
            phone=phone,
            stored_at=datetime.now().isoformat(timespec="seconds")
        )
        self.parcels[tracking_number] = parcel
        return parcel
