import hashlib


def import_models():
    from src.models.moderation_decision import ModerationDecision  # noqa: F401


def string_hash(string: str) -> int:
    return int.from_bytes(
        hashlib.blake2b(
            string.encode(),
            digest_size=8
        ).digest(),
        "big",
        signed=True
    )