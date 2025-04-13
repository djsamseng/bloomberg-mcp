
import collections
import json
import enum
import typing


class Transport(enum.Enum):
  SSE="sse"
  STDIO="stdio"

class StartupArgs:
  transport: Transport
  host: str
  port: int

  def __init__(self, transport: Transport, host: str, port: int) -> None:
    self.transport = transport
    self.host = host
    self.port = port

  def __str__(self) -> str:
    return json.dumps({
      "transport": self.transport.value,
      "host": self.host,
      "port": self.port,
    })

BloombergKWArgs = typing.Union[None, typing.Dict[str, typing.Any]]
