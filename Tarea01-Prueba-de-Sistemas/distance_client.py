import grpc
import distance_unary_pb2_grpc as pb2_grpc
import distance_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson
import json

def main(source, destination, unit):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DistanceServiceStub(channel)

        message = pb2.SourceDest(
            source=pb2.Position(
                latitude=source[0], longitude=source[1]
            ),
            destination=pb2.Position(
                latitude=destination[0], longitude=destination[1]
            ),
            unit=unit
        )

        print(f"Message sent:\n{MessageToJson(message)}\n")

        response = stub.geodesic_distance(message)

        try:
            print("-----Response-----")
            print("Distance:", json.loads(MessageToJson(response))["distance"])
            print("Method:", json.loads(MessageToJson(response))["method"])
            print("Distance unit:", json.loads(MessageToJson(response))["unit"])
        except KeyError:
            print("One or more keys are missing!")

if __name__ == "__main__":
    main(
        source=(-33.0351516, -70.5955963),
        destination=(-33.0348327, -71.5980458),
        unit="sdfghjkl"
    )
