

import json
import typing

import blpapi
import blpapi.version
import pandas as pd
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.utilities.logging import get_logger
from xbbg import blp

from . import types



def serve(args: types.StartupArgs):
  mcp = FastMCP("bloomberg-mcp", host=args.host, port=args.port)

  logger = get_logger(__name__)
  logger.info("startup args:" + str(args))
  logger.info("blpapi version:" + blpapi.version()) # type: ignore

  @mcp.tool(
    name="bdp",
    description="Retrieve Bloomberg reference data"
  )
  async def bdp(tickers: typing.List[str], flds: typing.List[str], kwargs: typing.Dict[str, typing.Any]) -> pd.DataFrame:
    logger.info("Running bdp:", tickers, flds)
    return blp.bdp(tickers=tickers, flds=flds, kwargs=kwargs)

  mcp.run(transport=args.transport.value)
