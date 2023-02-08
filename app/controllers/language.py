from typing import Any, Dict


def get_language(audio: bytes) -> Dict[str, Any]:
    """Returns the language for a given audio.

    :param audio: The given audio
    :return: Res dict
    """
    return {"language": "fr"}
