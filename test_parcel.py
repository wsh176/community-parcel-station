
import unittest
from parcel import ParcelManager


class TestParcelManager(unittest.TestCase):

    def setUp(self):
        self.manager = ParcelManager()

    def test_add_parcel(self):
        parcel = self.manager.add_parcel(
            "SF123456", "张三", "13800138000"
        )
        self.assertEqual(parcel.status, "待取件")

    def test_query_parcel(self):
        self.manager.add_parcel(
            "SF123456", "张三", "13800138000"
        )
        parcel = self.manager.get_parcel("SF123456")
        self.assertEqual(parcel.recipient_name, "张三")

    def test_pickup_parcel(self):
        self.manager.add_parcel(
            "SF123456", "张三", "13800138000"
        )
        parcel = self.manager.pickup_parcel("SF123456")
        self.assertEqual(parcel.status, "已取件")

    def test_duplicate_parcel(self):
        self.manager.add_parcel(
            "SF123456", "张三", "13800138000"
        )
        with self.assertRaises(ValueError):
            self.manager.add_parcel(
                "SF123456", "李四", "13900139000"
            )


if __name__ == "__main__":
    unittest.main()

