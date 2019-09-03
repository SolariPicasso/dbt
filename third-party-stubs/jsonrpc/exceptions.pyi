# Stubs for jsonrpc.exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Dict

class JSONRPCError:
    serialize: Any = ...
    deserialize: Any = ...
    code: Any = ...
    message: Any = ...
    data: Any = ...
    _data: Dict[str, Any] = ...
    def __init__(self, code: Optional[Any] = ..., message: Optional[Any] = ..., data: Optional[Any] = ...) -> None: ...
    @classmethod
    def from_json(cls, json_str: Any): ...
    @property
    def json(self): ...

class JSONRPCParseError(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCInvalidRequest(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCMethodNotFound(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCInvalidParams(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCInternalError(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCServerError(JSONRPCError):
    CODE: int = ...
    MESSAGE: str = ...

class JSONRPCException(Exception): ...
class JSONRPCInvalidRequestException(JSONRPCException): ...

class JSONRPCDispatchException(JSONRPCException):
    error: Any = ...
    def __init__(self, code: Optional[Any] = ..., message: Optional[Any] = ..., data: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
