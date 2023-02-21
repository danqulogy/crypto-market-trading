from json import loads, dumps

from requests import get


class BaseHttpService:
    def get(self, url:str, headers, params=None):
        # Making GET request
        if params is None:
            params = {}
        res = get(url=url, headers=headers, params=params)

        # Checking if API returns any errors in the response
        if res.status_code != 200:
            # Printing custom status error message
            print(res)
            return

        # Printing custom header elements header element
        print(res.headers)

        # Printing a clean JSON response
        print("\nJSON Response:")
        parsed_json = loads(res.content)
        formatted_json = dumps(parsed_json, indent=4)
        print(formatted_json)
        return parsed_json