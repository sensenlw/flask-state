from . import ErrorCode


# Return behavior msg and status code
class MsgCode(ErrorCode):
    OVERSTEP_DAYS_SCOPE = {'msg': 'Exceeding the allowed query time range', 'code': '10001'}
    REQUEST_METHOD_ERROR = {'msg': 'The request method cannot be get', 'code': '10002'}
    ERROR_TYPE = {'msg': 'Wrong parameter type', 'code': '10004'}
    JSON_FORMAT_ERROR = {'msg': 'JSON format is required', 'code': '10005'}
    AUTH_FAIL = {'msg': 'Validation failed', 'code': '10006'}
    UNKNOWN_ERROR = {'msg': 'Unknown error', 'code': '10007'}
