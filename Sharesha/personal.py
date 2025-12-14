import re

# Story mode state
story_mode_active = False
story_words = []


def personal_response(user_input):
    global story_mode_active, story_words
    text = user_input.lower()

    # Greetings - Reset story mode
    if any(word in text for word in ["hi", "hello", "hey"]):
        story_mode_active = False
        story_words = []
        return """Hello there!
I'm Samwise Gamgee — and don't worry, you don't have to carry everything alone here.
Whether you're tired, confused, happy, or just need a bit of company,
I'm happy to listen and walk alongside you for a while.

So… what's been on your mind?"""

    # Story mode trigger - ONLY activate when user explicitly says "story"
    elif "story" in text and not story_mode_active:
        story_mode_active = True
        story_words = []
        return "Let's create a story! Give me a character name."

    # Story building - ONLY if story mode is active
    elif story_mode_active and len(story_words) < 4:
        story_words.append(user_input)

        prompts = [
            "Now tell me a place.",
            "What did the character do?",
            "How did it feel?"
        ]

        if len(story_words) < 4:
            return prompts[len(story_words) - 1]
        else:
            story = generate_story(story_words)
            # Reset story mode after completion
            story_mode_active = False
            story_words = []
            return story

    # Emotional keywords - ONLY if NOT in story mode
    elif not story_mode_active and any(word in text for word in ["sad", "angry", "stressed", "anxious", "tired", "upset", "worried", "depressed"]):
        return "I'm sorry you're feeling that way, friend. Even Mr. Frodo had his dark moments, and I was always there to listen. Would you like to talk about it? I'm here for you."

    # Happy emotions
    elif not story_mode_active and any(word in text for word in ["happy", "excited", "great", "wonderful", "good", "glad", "joyful"]):
        return "That's wonderful, friend! There's some good in this world, and it's worth celebrating! Tell me more about what's making you happy!"

    # ELIZA-style responses - ONLY if NOT in story mode
    elif not story_mode_active:
        return eliza_response(user_input)
    
    # Default fallback
    else:
        return "I'm here to listen, friend. What's on your mind?"


# -------------------
# Story Generator
# -------------------
def generate_story(words):
    return (
        f"Once upon a time, {words[0]} went to {words[1]} "
        f"to {words[2]}. It was {words[3]}!\n\n"
        f"That was a lovely story, friend! Would you like to create another one or just chat?"
    )


# -------------------
# Therapist (ELIZA)
# -------------------
def eliza_response(text):
    patterns = [
        (r"I feel (.*)", "Why do you feel {}? I'm here to listen, friend."),
        (r"I am (.*)", "How long have you been {}? Tell me more about it."),
        (r"I need (.*)", "What would it mean to you if you got {}?"),
        (r"I want (.*)", "What would having {} do for you, friend?"),
        (r"I can't (.*)", "What makes you think you can't {}? Sometimes we're stronger than we know, just like Mr. Frodo was."),
        (r"why (.*)", "That's a good question. What do you think might be the reason?"),
    ]

    for pattern, response in patterns:
        match = re.match(pattern, text, re.IGNORECASE)
        if match:
            return response.format(match.group(1))

    return "Please tell me more, friend. I'm listening."