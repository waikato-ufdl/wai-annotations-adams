from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SinkStageSpecifier


class ADAMSODOutputFormatSpecifier(SinkStageSpecifier):
    """
    Specifier of the components for writing the ADAMS report-based
    object detection format.
    """
    @classmethod
    def description(cls) -> str:
        return "Writes image object-detection annotations in the ADAMS report-format"

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from ...base.component import ADAMSBaseWriter
        from ..component import ToADAMSReport
        return ToADAMSReport, ADAMSBaseWriter

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.image.object_detection import ImageObjectDetectionDomainSpecifier
        return ImageObjectDetectionDomainSpecifier
