# lemmy-bots
A repository containing useful Lemmy bots built using [Plemmy](https://github.com/tjkessler/plemmy)

Installation/deployment methods to come; examples:

```python
from lemmybot import RespondBot

# bot loop begins on initialization
my_bot = RespondBot(
  "<server>",                # Lemmy server
  "<username_or_email">,     # login username/email
  "<password>",              # login password
  "^Unique.*comment$",       # REGEX to search comments for
  "My reply!",               # if REGEX found, reply with this
  community_name=None,       # communtiy name (optional)
  community_id=None,         # communtiy ID (optional)
  headers=None,              # LemmyHttp API headers (optional)
  search_interval_sec=300,   # searches every `this` seconds (optional)
  max_comment_age_hours=24   # only replies to comments younger than `this` hours (optional)
)
```

```python
from lemmybot import RemoveCommentBot

# bot loop begins on initialization
my_bot = RemoveCommentBot(
  "<server>",                # Lemmy server
  "<username_or_email">,     # login username/email
  "<password>",              # login password
  "^Hateful.*comment$",      # REGEX to search comments for
  reason=None,               # if removed, reason for removal (optional)
  community_name=None,       # communtiy name (optional)
  community_id=None,         # communtiy ID (optional)
  headers=None,              # LemmyHttp API headers (optional)
  search_interval_sec=300,   # searches every `this` seconds (optional)
  max_comment_age_hours=24   # only removes comments younger than `this` hours (optional)
)
```
