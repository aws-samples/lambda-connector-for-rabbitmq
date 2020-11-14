import boto3
import json


class LambdaIvk:
    def __init__(self):
        self.client = boto3.client('lambda')
        pass

    def route(self, payload):
        fn_name = "mq_event_handler"
        args = {"payload": json.loads(payload)}
        self._invoke(fn_name=fn_name, args=args)

    def _invoke(self, fn_name, args):
        response = self.client.invoke_async(
            FunctionName=fn_name,
            InvokeArgs=json.dumps(args)
        )
        print("completed invoke of " + fn_name)
