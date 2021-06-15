from pypresence import Presence
import time

client_id = "your_client_id"

status = 'Github: KonstDev/discord-custom-status'

RPC = Presence(client_id)
RPC.connect()

status1 = status[0] + status[1]
i = 2
while(True):
     RPC.update(state=status1)
     if (len(status1) == len(status)):
          status1 = status[0] + status[1]
          i = 2
          time.sleep(1)
     else:
          status1 += status[i]
          i += 1
          time.sleep(0.15)
