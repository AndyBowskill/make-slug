def check_for_errors(sentence: str) -> tuple[bool, str]:
    """
    Check for errors on the sentence.

    Args:
        sentence: The sentence to check.

    Returns:
        error bool and error text message.
    """

    error = True
    error_text = None

    if sentence:
        error = False
    else:
        error_text = "The sentence must be populated. Please try again."

    return error, error_text


def generate(sentence: str) -> str:
    """
    Generate a slug from a sentence.

    Args:
        sentence: The sentence to check.

    Returns:
        generated slug value.
    """

    slug = sentence.strip()
    slug = slug.lower()
    slug = slug.replace(" ", "-")

    return slug
