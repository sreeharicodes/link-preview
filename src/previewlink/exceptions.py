class PreviewLinkException(Exception):
    pass


class InvalidContentError(PreviewLinkException):
    pass


class InvalidMimeTypeError(InvalidContentError):
    pass


class MaximumContentSizeError(InvalidContentError):
    pass
