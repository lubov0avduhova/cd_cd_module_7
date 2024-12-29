from concurrent import futures
import grpc
import review_service_pb2
import review_service_pb2_grpc

class ReviewService(review_service_pb2_grpc.ReviewServiceServicer):
    def AddReview(self, request, context):
        return review_service_pb2.ReviewResponse(review_id="1", status="Added")

    def GetReviews(self, request, context):
        return review_service_pb2.ReviewsResponse(reviews=[review_service_pb2.Review(review_id="1", user_id="123", review_text="Great product!", rating=5)])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    review_service_pb2_grpc.add_ReviewServiceServicer_to_server(ReviewService(), server)
    server.add_insecure_port('[::]:5005')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()