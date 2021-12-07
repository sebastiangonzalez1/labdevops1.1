import logging
import azure.functions as func
import memory_profiler

root_logger = logging.getLogger()
root_logger.handlers[0].setFormatter(logging.Formatter("%(name)s: %(message)s"))
profiler_logstream = memory_profiler.LogFile('memory_profiler_logs', True)

@memory_profiler.profile(stream=profiler_logstream)
def exec(value):
    logging.info(value)

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
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
        exec(value)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
