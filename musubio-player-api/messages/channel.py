"""ProtoRPC message class definitions for Musubio API."""

from protorpc import messages, message_types
from messages.video import Video, VideoImportRequest


class Channel(messages.Message):
    """Channel that stores a message."""
    id = messages.IntegerField(1, required=True)
    entity_id = messages.IntegerField(2, required=True)
    title = messages.StringField(3, required=True)
    description = messages.StringField(4, required=False)
    videos = messages.MessageField(Video, 5, repeated=True)
    created = message_types.DateTimeField(6, required=False)
    updated = message_types.DateTimeField(7, required=False)


class ChannelDetailsRequest(messages.Message):
    """ProtoRPC message definition to represent a channel to be fetched."""
    id = messages.IntegerField(1, required=True)


class ChannelInsertRequest(messages.Message):
    """ProtoRPC message definition to represent a channel to be inserted."""
    entity_id = messages.IntegerField(1, required=True)
    title = messages.StringField(2, required=True)
    description = messages.StringField(3, required=False)


class ChannelBatchImportRequest(messages.Message):
    """ProtoRPC message definition to represent a channel to be inserted."""
    entity_id = messages.IntegerField(1, required=True)
    title = messages.StringField(2, required=True)
    description = messages.StringField(3, required=False)
    videos = messages.MessageField(VideoImportRequest, 4, repeated=True)


class ChannelListResponse(messages.Message):
    """Collection of Channels."""
    channels = messages.MessageField(Channel, 1, repeated=True)


class ChannelAddVideoRequest(messages.Message):
    """ProtoRPC message definition to represent a videos to be added to a channel."""
    channel_id = messages.IntegerField(1, required=True)
    video_id = messages.IntegerField(2, required=True)