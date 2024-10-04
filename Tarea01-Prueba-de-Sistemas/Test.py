import unittest
import grpc
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson
from geo_location import Position

class TestGeodesicDistance(unittest.TestCase):

    def setUp(self):
        self.channel = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.DistanceServiceStub(self.channel)

    def test_valid_coordinates_km(self):
        message = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0348, longitude=-70.5956),
            destination=pb2.Position(latitude=-33.0348, longitude=-71.5980),
            unit="km"
        )
        response = self.stub.geodesic_distance(message)
        expected_distance = 100  # distancia aproximada desde el Google Earth
        self.assertAlmostEqual(response.distance, expected_distance, delta=0.1)
        self.assertEqual(response.unit, "km")

    def test_invalid_latitude(self):
        message = pb2.SourceDest(
            source=pb2.Position(latitude=-90.1, longitude=-70.5956),
            destination=pb2.Position(latitude=-33.0348, longitude=-71.5980),
            unit="km"
        )
        response = self.stub.geodesic_distance(message)
        self.assertEqual(response.distance, -1.0)
        self.assertEqual(response.unit, "invalid")

    def test_invalid_longitude(self):
        message = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0348, longitude=180.1),
            destination=pb2.Position(latitude=-33.0348, longitude=-71.5980),
            unit="km"
        )
        response = self.stub.geodesic_distance(message)
        self.assertEqual(response.distance, -1.0)
        self.assertEqual(response.unit, "invalid")

    def test_invalid_unit(self):
        message = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0348, longitude=-70.5956),
            destination=pb2.Position(latitude=-33.0348, longitude=-71.5980),
            unit="miles"
        )
        response = self.stub.geodesic_distance(message)
        self.assertEqual(response.distance, -1.0)
        self.assertEqual(response.unit, "invalid")

    def test_default_unit(self):
        message = pb2.SourceDest(
            source=pb2.Position(latitude=-33.0348, longitude=-70.5956),
            destination=pb2.Position(latitude=-33.0348, longitude=-71.5980),
            unit=""
        )
        response = self.stub.geodesic_distance(message)
        expected_distance = 100 
        self.assertAlmostEqual(response.distance, expected_distance, delta=0.1)
        self.assertEqual(response.unit, "km")

if __name__ == '__main__':
    unittest.main()
