import time
import re
from datetime import datetime, timedelta

from plemmy.responses import GetCommentsResponse, ModRemoveCommentView

from .lemmybot import LemmyBot


class RemoveCommentBot(LemmyBot):

    def __init__(self, server: str, username_or_email: str, password: str,
                 search_regex: str, reason: str = None,
                 community_name: str = None, community_id: int = None,
                 headers: dict = None, search_interval_sec: int = 300,
                 max_comment_age_hours: int = 24) -> None:

        self._search_regex = search_regex
        self._reason = reason
        self._community_name = community_name
        self._community_id = community_id
        self._search_interval = search_interval_sec
        self._max_age = timedelta(hours=max_comment_age_hours)
        super().__init__(server, username_or_email, password, headers)

    def loop(self) -> None:

        while True:
            self._search_and_remove()
            time.sleep(self._search_interval)

    def _search_and_remove(self) -> None:

        # obtain/parse Lemmy API response
        response = GetCommentsResponse(
            self._srv.get_comments(
                community_id=self._community_id,
                community_name=self._community_name
            )
        )

        # determine current time
        _now = datetime.now()

        # for each comment
        for com_view in response.comments:

            # parse comment publish time
            _pubtime = datetime.fromtimestamp(time.mktime(time.strptime(
                com_view.comment.published, "%Y-%m-%dT%H:%M:%S"
            )))

            # if older than max comment age delta, next comment
            if _now - _pubtime > self._max_age:
                continue

            # if comment contains REGEX, remove it
            if re.search(
                self._search_regex,
                com_view.comment.content
             ) is not None:

                # remove comment
                self._srv.remove_comment(com_view.comment.id, True,
                                         reason=self._reason)
