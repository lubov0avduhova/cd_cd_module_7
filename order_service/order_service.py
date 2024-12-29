from concurrent import futures
import grpc
import order_service_pb2
import order_service_pb2_grpc

class OrderService(order_service_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        return order_service_pb2.OrderResponse(order_id="1", user_id=request.user_id, product_id=request.product_id, quantity=request.quantity, status="Created")

    def GetOrder(self, request, context):
        return order_service_pb2.OrderResponse(order_id=request.order_id, user_id="123", product_id="456", quantity=2, status="Shipped")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:5002')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()