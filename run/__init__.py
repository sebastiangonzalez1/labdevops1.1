import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    value = 'Hello Randall'
    name = req.params.get('name')
    exec(value)
    if not name:
        try:
            exec(value)
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello team, {name}. This HTTP triggered function executed successfully.")
        exec(value)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
