from car.models import Car
from car.serializers import CarSerializer
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data).encode("utf-8")


def deserialize_car_object(car_json: str) -> Car:
    car_data = json.loads(car_json)
    serializer = CarSerializer(data=car_data)
    if serializer.is_valid():
        return serializer.create(serializer.validated_data)
    else:
        raise ValueError("Invalid data for Car object")
