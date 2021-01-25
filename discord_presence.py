from pypresence import Presence
import time
import threading as th


class UrsinaCraft_presence(th.Thread):
    def __init__(self):
        th.Thread.__init__(self)

    def run(self):
        """
        You need to upload your image(s) here:
        https://discordapp.com/developers/applications/<APP ID>/rich-presence/assets
        """

        client_id = "803323887390818404"  # Enter your Application ID here.
        RPC = Presence(client_id=client_id)
        RPC.connect()

        # Make sure you are using the same name that you used when uploading the image
        print(RPC.update(large_text="Large Text Here!", small_text="Small Text Here!"))

        while 1:
            time.sleep(15)  # Can only update presence every 15 seconds