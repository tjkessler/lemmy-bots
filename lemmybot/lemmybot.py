from plemmy import LemmyHttp


class LemmyBot(object):

    def __init__(self, server: str, username_or_email: str,
                 password: str, headers: dict = None) -> None:
        """ base class for all bots; general behavior is:

        Connect, login -> start method -> loop method -> stop method

        child bots define their own start, loop, and stop methods.

        Args:
            server (str): Lemmy server/instance
            username_or_email (str): login username or email
            password (str): login password
            headers (dict): optional headers

        Returns:
            None
        """

        self._srv = LemmyHttp(server, headers=headers)
        self._srv.login(username_or_email, password)
        self.start()
        self.loop()
        self.stop()

    def start(self) -> None:

        return

    def loop(self) -> None:

        return

    def stop(self) -> None:

        return
