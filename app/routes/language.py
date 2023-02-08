from fastapi import APIRouter, Request, File
from . import auth_required
from ..controllers.language import get_language

LanguageRouter = APIRouter(prefix="/v1/language", tags=["Language", "Detection"])


@LanguageRouter.post("")
@auth_required
async def language(request: Request, file: bytes = File()):
    """Give a context for a given audio.

    :param request: Request object checked by the auth_required decorator
    :param file: Given audio
    :return: JSON response which contains the language detected in the input audio
    """
    return get_language(file)
