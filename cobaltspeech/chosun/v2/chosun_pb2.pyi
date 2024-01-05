from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VersionResponse(_message.Message):
    __slots__ = ("chosun",)
    CHOSUN_FIELD_NUMBER: _ClassVar[int]
    chosun: str
    def __init__(self, chosun: _Optional[str] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("domain_sets", "models")
    DOMAIN_SETS_FIELD_NUMBER: _ClassVar[int]
    MODELS_FIELD_NUMBER: _ClassVar[int]
    domain_sets: _containers.RepeatedCompositeFieldContainer[DomainInfo]
    models: _containers.RepeatedCompositeFieldContainer[ModelInfo]
    def __init__(self, domain_sets: _Optional[_Iterable[_Union[DomainInfo, _Mapping]]] = ..., models: _Optional[_Iterable[_Union[ModelInfo, _Mapping]]] = ...) -> None: ...

class DomainInfo(_message.Message):
    __slots__ = ("id", "name", "domains")
    class DomainsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    domains: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., domains: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ModelInfo(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ParseRequest(_message.Message):
    __slots__ = ("model_id", "domain", "text", "nbest", "cnet", "nbest_tokens", "context_features", "intent_whitelist")
    class ContextFeaturesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NBEST_FIELD_NUMBER: _ClassVar[int]
    CNET_FIELD_NUMBER: _ClassVar[int]
    NBEST_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FEATURES_FIELD_NUMBER: _ClassVar[int]
    INTENT_WHITELIST_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    domain: str
    text: str
    nbest: NBest
    cnet: CNet
    nbest_tokens: NBestTokens
    context_features: _containers.ScalarMap[str, float]
    intent_whitelist: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, model_id: _Optional[str] = ..., domain: _Optional[str] = ..., text: _Optional[str] = ..., nbest: _Optional[_Union[NBest, _Mapping]] = ..., cnet: _Optional[_Union[CNet, _Mapping]] = ..., nbest_tokens: _Optional[_Union[NBestTokens, _Mapping]] = ..., context_features: _Optional[_Mapping[str, float]] = ..., intent_whitelist: _Optional[_Iterable[str]] = ...) -> None: ...

class NBest(_message.Message):
    __slots__ = ("hypotheses",)
    HYPOTHESES_FIELD_NUMBER: _ClassVar[int]
    hypotheses: _containers.RepeatedCompositeFieldContainer[Hypothesis]
    def __init__(self, hypotheses: _Optional[_Iterable[_Union[Hypothesis, _Mapping]]] = ...) -> None: ...

class Hypothesis(_message.Message):
    __slots__ = ("text", "confidence")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    text: str
    confidence: float
    def __init__(self, text: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class NBestTokens(_message.Message):
    __slots__ = ("hypotheses",)
    HYPOTHESES_FIELD_NUMBER: _ClassVar[int]
    hypotheses: _containers.RepeatedCompositeFieldContainer[TokenHypothesis]
    def __init__(self, hypotheses: _Optional[_Iterable[_Union[TokenHypothesis, _Mapping]]] = ...) -> None: ...

class TokenHypothesis(_message.Message):
    __slots__ = ("tokens", "confidence")
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[CNetArc]
    confidence: float
    def __init__(self, tokens: _Optional[_Iterable[_Union[CNetArc, _Mapping]]] = ..., confidence: _Optional[float] = ...) -> None: ...

class CNet(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[CNetLink]
    def __init__(self, links: _Optional[_Iterable[_Union[CNetLink, _Mapping]]] = ...) -> None: ...

class CNetLink(_message.Message):
    __slots__ = ("arcs",)
    ARCS_FIELD_NUMBER: _ClassVar[int]
    arcs: _containers.RepeatedCompositeFieldContainer[CNetArc]
    def __init__(self, arcs: _Optional[_Iterable[_Union[CNetArc, _Mapping]]] = ...) -> None: ...

class CNetArc(_message.Message):
    __slots__ = ("word", "confidence")
    WORD_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    word: str
    confidence: float
    def __init__(self, word: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class ParseResponse(_message.Message):
    __slots__ = ("intents",)
    INTENTS_FIELD_NUMBER: _ClassVar[int]
    intents: _containers.RepeatedCompositeFieldContainer[Intent]
    def __init__(self, intents: _Optional[_Iterable[_Union[Intent, _Mapping]]] = ...) -> None: ...

class Intent(_message.Message):
    __slots__ = ("domain", "id", "confidence", "entities", "text")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    domain: str
    id: str
    confidence: float
    entities: _containers.RepeatedCompositeFieldContainer[Entity]
    text: str
    def __init__(self, domain: _Optional[str] = ..., id: _Optional[str] = ..., confidence: _Optional[float] = ..., entities: _Optional[_Iterable[_Union[Entity, _Mapping]]] = ..., text: _Optional[str] = ...) -> None: ...

class Entity(_message.Message):
    __slots__ = ("id", "value", "start", "end", "confidence")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: str
    start: int
    end: int
    confidence: float
    def __init__(self, id: _Optional[str] = ..., value: _Optional[str] = ..., start: _Optional[int] = ..., end: _Optional[int] = ..., confidence: _Optional[float] = ...) -> None: ...
