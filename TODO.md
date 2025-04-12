# TODO

- First we can simply wrap around xbbg which has already documented parameters which we can turn into tools
  - [xbbg blp](https://github.com/alpha-xone/xbbg/blob/main/xbbg/blp.py#L30)
- mock out the responses [example](https://github.com/msitt/blpapi-python/blob/master/examples/unittests/market-data-notifier/tests/test_eventprocessor.py)

- LD_LIBRARY_PATH to include blpapi3 shared libraries [link](https://github.com/msitt/blpapi-python?tab=readme-ov-file#writing-bloomberg-api-programs-in-python)
- Parse docs and generate tools
  - [blpapi](https://www.bloomberg.com/professional/support/api-library/)
    - [python blpapi docs](https://bloomberg.github.io/blpapi-docs/python/3.25.3/index.html)
  - [tools schema](https://modelcontextprotocol.io/docs/concepts/tools#tool-definition-structure)
- Implement the server using the [example](https://github.com/modelcontextprotocol/servers/blob/main/src/fetch/src/mcp_server_fetch/server.py)
- Add tests
  - In [pyproject.toml](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/%7B%7Bcookiecutter.project_name%7D%7D/pyproject.toml#L66)
  - In [GitHub workflows](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/.github/workflows/main.yml#L52)
  - Using [pytest](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/tests/test_cookiecutter.py)
    - With pytest as a [dev dependency](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/%7B%7Bcookiecutter.project_name%7D%7D/pyproject.toml#L28)
      - [dev dependency docs](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies)
