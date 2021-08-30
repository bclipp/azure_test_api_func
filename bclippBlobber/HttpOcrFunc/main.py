import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    url: str = "https://my.api.mockaroo.com/fake_data_poc_csv.json?key=56c5cc10"
    response: requests = requests.get(url)
    logging.info('Python HTTP trigger function processed a request.')


    return response.text

if __name__ == "__main__":
    main()