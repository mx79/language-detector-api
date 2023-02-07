from fastapi import APIRouter, Request
from . import Sentence, auth_required
from ..controllers.language import get_language

LanguageRouter = APIRouter(prefix="/v1/language", tags=["Language", "Detection"])


@LanguageRouter.post("")
@auth_required
async def language(request: Request, sentence: Sentence):
    """Give a context for a given sentence.

    :param request: Request object checked by the auth_required decorator
    :param sentence: Given sentence
    :return: JSON response which contains the language detected in the input sentence
    """
    return get_language(sentence.text)
