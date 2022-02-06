from zulip_bots.test_lib import BotTestCase, DefaultTests


class TestHelpBot(BotTestCase, DefaultTests):
    bot_name = "mule"  # type: str

    def test_bot(self) -> None:
        dialog = [
            ("", "from Mule Bot"),
            ("help", "from Mule Bot"),
            ("foo", "from Mule Bot"),
        ]

        self.verify_dialog(dialog)
