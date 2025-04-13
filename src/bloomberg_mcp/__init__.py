
import argparse
import typing

import blpapi
import blpapi.version
import pandas as pd

from xbbg import blp

from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.utilities.logging import get_logger

logger = get_logger(__name__)


def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--sse", action="store_true", help="Run ")
  parser.add_argument("--host", type=str, default=None)
  parser.add_argument("--port", type=int, default=None)

  args = parser.parse_args()
  is_sse = args.sse or args.host != None or args.port != None

  return {
    "transport": "sse" if is_sse else "stdio",
    "host": args.host or "127.0.0.1",
    "port": args.port or 8000,
  }

def main() -> None:
  args = parse_args()
  logger.info("Startup args:" + str(args))
  logger.info("blpapi version:" + blpapi.version()) # type: ignore
  mcp = FastMCP("bloomberg-mcp", host=args["host"], port=args["port"])


  @mcp.tool(
    name="bdp",
    description="Retrieve Bloomberg reference data"
  )
  async def bdp(tickers: typing.List[str], flds: typing.List[str], kwargs: typing.Dict[str, typing.Any]) -> pd.DataFrame:
    logger.info("Running bdp:", tickers, flds)
    return blp.bdp(tickers=tickers, flds=flds, kwargs=kwargs)

  mcp.run(transport=args["transport"])
