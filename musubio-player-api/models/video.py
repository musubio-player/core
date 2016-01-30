from google.appengine.ext import ndb

from messages.video import Video as VideoMessage


class Video(ndb.Model):
    """Model to store videos that have been inserted by users."""
    video_id = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    description = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

    def to_message(self):
        """Turns the Video entity into a ProtoRPC object.

        This is necessary so the entity can be returned in an API request.

        Returns:
            An instance of Video with the ID set to the datastore
            ID of the current entity, the outcome simply the entity's outcome value.
        """
        video = VideoMessage()
        video.id = self.key.id()
        video.video_id = self.video_id
        video.title = self.title
        video.description = self.description
        video.created = self.created

        return video

    @classmethod
    def get_details(cls, message):
        return cls.get_by_id(message.id)

    @classmethod
    def put_from_message(cls, message):
        """Gets the current user and inserts a Video.

        Args:
            message: A VideoRequest instance to be inserted.

        Returns:
            The Video entity that was inserted.
        """
        # current_user = get_endpoints_current_user()
        # entity = cls(outcome=message.outcome, player=current_user)
        entity = cls(title=message.title, description=message.description, video_id=message.video_id)
        entity.put()
        return entity

    @classmethod
    def get_list(cls):
        return cls.query()