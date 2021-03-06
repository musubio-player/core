"""ProtoRPC message class definitions for Musubio API."""

from protorpc import messages


class ThumbnailMessage(messages.Message):
    """Thumbnail image object."""
    default = messages.StringField(1, required=True)
    high = messages.StringField(2, required=True)
    medium = messages.StringField(3, required=True)


class Video(messages.Message):
    """YouTube Video data object."""
    id = messages.StringField(1, required=True)
    title = messages.StringField(2, required=True)
    url = messages.StringField(3, required=True)
    channel_id = messages.StringField(4, required=True)
    published_at = messages.StringField(5, required=True)
    live_broadcast_content = messages.StringField(6, required=True)
    channel_title = messages.StringField(7, required=True)
    description = messages.StringField(8, required=True)
    thumbnail = messages.MessageField(ThumbnailMessage, 9, required=True)
    duration_ISO = messages.StringField(10)
    duration = messages.IntegerField(11)


class SearchResultsMessage(messages.Message):
    """Collection of search results."""
    videos = messages.MessageField(Video, 1, repeated=True)


class SearchRequestMessage(messages.Message):
    """ProtoRPC message definition to represent a search query."""
    q = messages.StringField(1, required=True)
    limit = messages.IntegerField(2, default=25)


class VideoListRequestMessage(messages.Message):
    """ProtoRPC message definition to represent a video list query"""
    id = messages.StringField(1, required=True)


class VideoList(messages.Message):
    """Collection of videos"""
    videos = messages.MessageField(Video, 1, repeated=True)