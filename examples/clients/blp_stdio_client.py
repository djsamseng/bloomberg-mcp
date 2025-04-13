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


async def test_bdp(session: ClientSession):
  res = await session.call_tool(
    name="bdp",
    arguments={
      "tickers": ["AAPL US Security"],
      "flds": ["Security_Name", "Eqy_Weighted_Avg_Px"],
      "kwargs": {
        "VWAP_Dt": "20181224",
      },
    },
  )
  print("bdp result:", res)

async def test_bdh(session: ClientSession):
  res = await session.call_tool(
    name="bdh",
    arguments={
      "tickers": ["SPX Index"],
      "flds": ["high", "low", "last_price"],
      "start_date": "2018-10-10",
      "end_date": "2018-10-20",
    }
  )

  print("bdh results:", res)

async def test_bds(session: ClientSession):
  res = await session.call_tool(
    name="bds",
    arguments={
      "tickers": ["BHP AU Equity"],
      "flds": ["DVD_Hist_All"],
      "kwargs": {
        "DVD_Start_Dt": "20180101",
        "DVD_End_Dt": "20180531"
      }
    }
  )

  print("bds results:", res)

async def test_bdib(session: ClientSession):
  res = await session.call_tool(
    name="bdib",
    arguments={
      "ticker": "BHP AU Equity",
      "dt": "2018-10-17"
    }
  )

  print("bdib results:", res)

async def test_earning(session: ClientSession):
  res = await session.call_tool(
    name="earning",
    arguments={
      "ticker": "AMD US Equity",
      "by": "Geo",
      "kwargs": {
        "Eqy_Fund_Year": 2017,
        "Number_Of_Periods": 1,
      }
    }
  )

  print("earning results:", res)

async def test_dividend(session: ClientSession):
  res = await session.call_tool(
    name="dividend",
    arguments={
      "tickers": ["C US Equity", "MS US Equity"],
      "start_date": "2018-01-01",
      "end_date": "2018-05-01"
    }
  )

  print("dividend results:", res)

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

      await test_bdp(session)
      await test_bdh(session)
      await test_bds(session)
      await test_bdib(session)
      await test_earning(session)
      await test_dividend(session)


def main() -> None:
  asyncio.run(run())


if __name__ == "__main__":
  main()
