from typing import Any, Dict, List
import logging
from zulip_bots.lib import BotHandler

class MuleHandler:

    def usage(self) -> str:
        return """
        This is a MuleSoft bot, which can get the environment details,
        Servers and Clusters. This can manage the instances and
        the Clusters. It can get the details of CPU and memory usage
        of any instance and can other details that might be required

        It will also show details of any API  requested in the environment.

        @-mention the bot with 'help' to see available commands.
        """

    def handle_message(self,message: Dict[str, Any], bot_handler: BotHandler) -> None:
        content = "from Mule Bot"  # type: str
        bot_handler.send_reply(message, content)

        emoji_name = "wave"  # type: str
        bot_handler.react(message, emoji_name)
        return


handler_class = MuleHandler
