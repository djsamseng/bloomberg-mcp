# TODO

- mock out the responses when BBComm is not available [example](https://github.com/msitt/blpapi-python/blob/master/examples/unittests/market-data-notifier/tests/test_eventprocessor.py)

- LD_LIBRARY_PATH to include blpapi3 shared libraries [link](https://github.com/msitt/blpapi-python?tab=readme-ov-file#writing-bloomberg-api-programs-in-python)
- Add tool for querying ticker names and field names (an search / autocomplete for valid parameters to call other tools)
  - `FLDS<GO>` (query fields available from the API Data Dictionary)
    - `//blp/apiflds`
      ```c++
      Service fieldInfoService = session.getService("//blp/apiflds");
      Request request = fieldInfoService.createRequest("FieldListRequest");
      request.append("fieldType", "All"); // Other options are Static and RealTime
      request.set("returnFieldDocumentation", true);
      std::cout << "Sending Request: " << request << std::endl;
      session.sendRequest(request);
      ```
  - `SECF<GO>` (security lookup)
    - `//blp/instruments`
    - `//blp/mktlist/secids`
  - CUSIP lookup

- Add tests
  - In [pyproject.toml](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/%7B%7Bcookiecutter.project_name%7D%7D/pyproject.toml#L66)
  - In [GitHub workflows](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/.github/workflows/main.yml#L52)
  - Using [pytest](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/tests/test_cookiecutter.py)
    - With pytest as a [dev dependency](https://github.com/fpgmaas/cookiecutter-uv/blob/f27ad09c28e92ff5231291003c0aab2f483fdb4c/%7B%7Bcookiecutter.project_name%7D%7D/pyproject.toml#L28)
      - [dev dependency docs](https://docs.astral.sh/uv/concepts/projects/dependencies/#development-dependencies)
