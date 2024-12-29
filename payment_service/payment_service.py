from concurrent import futures
import grpc
import payment_service_pb2
import payment_service_pb2_grpc

class PaymentService(payment_service_pb2_grpc.PaymentServiceServicer):
    def ProcessPayment(self, request, context):
        return payment_service_pb2.PaymentResponse(payment_id="1", status="Success")

    def GetPaymentStatus(self, request, context):
        return payment_service_pb2.PaymentResponse(payment_id=request.payment_id, status="Success")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_service_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port('[::]:5003')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()