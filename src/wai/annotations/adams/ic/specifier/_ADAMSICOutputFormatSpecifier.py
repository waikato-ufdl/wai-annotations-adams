from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SinkStageSpecifier


class ADAMSICOutputFormatSpecifier(SinkStageSpecifier):
    """
    Specifier of the components for writing the ADAMS report-based
    image classification format.
    """
    @classmethod
    def description(cls) -> str:
        return "Writes image classification annotations in the ADAMS report-format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ...base.component import ADAMSBaseWriter
        from ..component import ToADAMS
        return ToADAMS, ADAMSBaseWriter

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.classification import ImageClassificationDomainSpecifier
        return ImageClassificationDomainSpecifier
