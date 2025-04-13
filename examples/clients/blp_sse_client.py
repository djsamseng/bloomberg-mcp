# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp",
# ]
# ///

import argparse
import asyncio

from mcp.client.sse import sse_client
from mcp.client.session import ClientSession

import blp_call_tools

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--host", type=str, default="http://127.0.0.1")
  parser.add_argument("--port", type=int, default=8000)
  return parser.parse_args()

async def run() -> None:
  args = parse_args()
  url = "{0}:{1}/sse".format(args.host, args.port)

  print(url)
  async with sse_client(url) as (read_stream, write_stream):
    async with ClientSession(
      read_stream=read_stream,
      write_stream=write_stream
    ) as session:
      await session.initialize()

      resources = await session.list_resources()
      print("Available resources:", resources)

      tools = await session.list_tools()
      print("Available tools:", tools)

      await blp_call_tools.test_bdp(session)
      await blp_call_tools.test_bdh(session)
      await blp_call_tools.test_bds(session)
      await blp_call_tools.test_bdib(session)
      await blp_call_tools.test_earning(session)
      await blp_call_tools.test_dividend(session)

def main() -> None:
  asyncio.run(run())


if __name__ == "__main__":
  main()
