from __future__ import absolute_import, division, print_function

import hedera_mirror_sdk
from six import python_2_unicode_compatible


@python_2_unicode_compatible
class hedera_mirror_sdkError(Exception):
    def __init__(
        self,
        message=None,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
        code=None,
    ):
        super(hedera_mirror_sdkError, self).__init__(message)

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        self.request_id = self.headers.get("request-id", None)


class APIError(hedera_mirror_sdkError):
    pass


class hedera_mirror_sdkErrorWithParamCode(hedera_mirror_sdkError):
    def __repr__(self):
        return (
            "%s(message=%r, param=%r, code=%r, http_status=%r, "
            "request_id=%r)"
            % (
                self.__class__.__name__,
                self._message,
                self.param,
                self.code,
                self.http_status,
                self.request_id,
            )
        )


class InvalidRequestError(hedera_mirror_sdkErrorWithParamCode):
    def __init__(
        self,
        message,
        param,
        code=None,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body, headers, code
        )
        self.param = param


class AuthenticationError(hedera_mirror_sdkError):
    pass


class PermissionError(hedera_mirror_sdkError):
    pass

