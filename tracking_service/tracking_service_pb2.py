# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tracking_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16tracking_service.proto\x12\x08tracking\"%\n\x11TrackOrderRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\"0\n\x19GetTrackingDetailsRequest\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\"e\n\x10TrackingResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x1a\n\x12\x65stimated_delivery\x18\x04 \x01(\t2\xaf\x01\n\x0fTrackingService\x12\x45\n\nTrackOrder\x12\x1b.tracking.TrackOrderRequest\x1a\x1a.tracking.TrackingResponse\x12U\n\x12GetTrackingDetails\x12#.tracking.GetTrackingDetailsRequest\x1a\x1a.tracking.TrackingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tracking_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TRACKORDERREQUEST']._serialized_start=36
  _globals['_TRACKORDERREQUEST']._serialized_end=73
  _globals['_GETTRACKINGDETAILSREQUEST']._serialized_start=75
  _globals['_GETTRACKINGDETAILSREQUEST']._serialized_end=123
  _globals['_TRACKINGRESPONSE']._serialized_start=125
  _globals['_TRACKINGRESPONSE']._serialized_end=226
  _globals['_TRACKINGSERVICE']._serialized_start=229
  _globals['_TRACKINGSERVICE']._serialized_end=404
# @@protoc_insertion_point(module_scope)
