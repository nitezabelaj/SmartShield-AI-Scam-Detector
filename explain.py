def generate_explanation(message):
    keywords = ["win", "urgent", "click", "money", "free"]

    found = [word for word in keywords if word in message.lower()]

    if found:
        return f"Suspicious keywords detected: {', '.join(found)}"
    else:
        return "No obvious scam keywords detected."