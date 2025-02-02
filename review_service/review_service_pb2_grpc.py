# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import review_service_pb2 as review__service__pb2


class ReviewServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddReview = channel.unary_unary(
                '/review.ReviewService/AddReview',
                request_serializer=review__service__pb2.AddReviewRequest.SerializeToString,
                response_deserializer=review__service__pb2.ReviewResponse.FromString,
                )
        self.GetReviews = channel.unary_unary(
                '/review.ReviewService/GetReviews',
                request_serializer=review__service__pb2.GetReviewsRequest.SerializeToString,
                response_deserializer=review__service__pb2.ReviewsResponse.FromString,
                )


class ReviewServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddReview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReviews(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReviewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddReview': grpc.unary_unary_rpc_method_handler(
                    servicer.AddReview,
                    request_deserializer=review__service__pb2.AddReviewRequest.FromString,
                    response_serializer=review__service__pb2.ReviewResponse.SerializeToString,
            ),
            'GetReviews': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReviews,
                    request_deserializer=review__service__pb2.GetReviewsRequest.FromString,
                    response_serializer=review__service__pb2.ReviewsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'review.ReviewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReviewService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddReview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/review.ReviewService/AddReview',
            review__service__pb2.AddReviewRequest.SerializeToString,
            review__service__pb2.ReviewResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReviews(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/review.ReviewService/GetReviews',
            review__service__pb2.GetReviewsRequest.SerializeToString,
            review__service__pb2.ReviewsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
