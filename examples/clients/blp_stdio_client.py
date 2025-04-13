# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mcp",
# ]
# ///

import asyncio
import typing

from mcp import ClientSession, StdioServerParameters
from mcp import types as mcp_types
from mcp.client.stdio import stdio_client

import blp_call_tools

async def run():

  server_params = StdioServerParameters(
    command="uv",
    args=["run", "bloomberg-mcp"],
    env=None,
  )

  async with stdio_client(server_params) as (read_stream, write_stream):
    async with ClientSession(
      read_stream=read_stream,
      write_stream=write_stream,
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
