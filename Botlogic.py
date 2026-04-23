def generate_reply(text):
    text = text.lower()

    # Music triggers
    if any(word in text for word in ["song", "music", "track", "drop", "link"]):
        return (
            "🔥 Here’s my latest track:\n"
            "https://your-link-here.com\n\n"
            "If you like it, follow me for more drops 💯"
        )

    # Greeting
    elif any(word in text for word in ["hi", "hey", "hello"]):
        return "Yo 👋 send 'song' to hear my latest track"

    # Engagement
    elif "follow" in text:
        return "Appreciate you 🙏 new music coming soon"

    else:
        return "Send 'song' to get my latest release 🔥"
