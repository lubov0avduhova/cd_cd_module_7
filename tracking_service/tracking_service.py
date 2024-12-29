from concurrent import futures
import grpc
import tracking_service_pb2
import tracking_service_pb2_grpc

class TrackingService(tracking_service_pb2_grpc.TrackingServiceServicer):
    def TrackOrder(self, request, context):
        return tracking_service_pb2.TrackingResponse(tracking_id="1", order_id=request.order_id, status="In Transit", estimated_delivery="2024-01-01")

    def GetTrackingDetails(self, request, context):
        return tracking_service_pb2.TrackingResponse(tracking_id=request.tracking_id, order_id="1", status="Delivered", estimated_delivery="2024-01-01")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tracking_service_pb2_grpc.add_TrackingServiceServicer_to_server(TrackingService(), server)
    server.add_insecure_port('[::]:5004')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()