
import argparse
import typing

from . import types
from . import blp_mcp_server

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--sse", action="store_true", help="Run ")
  parser.add_argument("--host", type=str, default=None)
  parser.add_argument("--port", type=int, default=None)

  args = parser.parse_args()
  is_sse = args.sse or args.host != None or args.port != None

  transport = types.Transport.SSE if is_sse else types.Transport.STDIO
  host = args.host if args.host != None else "127.0.0.1"
  port = args.port if args.port != None else 8000
  return types.StartupArgs(transport=transport, host=host, port=port)

def main() -> None:
  args = parse_args()
  blp_mcp_server.serve(args)
