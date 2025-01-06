def format_history(chat_history: list[dict]) -> str:
    """Formats chat history for inclusion in the prompt."""
    return "\n".join(f"{entry['role']}: {entry['message']}" for entry in chat_history)
