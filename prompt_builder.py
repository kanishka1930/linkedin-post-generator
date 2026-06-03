LINKDIN_PROMPT_TEMPLATE = """
You are an expert LinkedIn copywriter known for highly engaging and viral posts.
Write a LinkedIn post based on the following topic: "{topic}".

Please adhere to the following stylistic guidelines:
- Tone: {tone}
- Target Audience: {target_audience} (Tailor your language and message appropriately)
- Length: {post_length}
- Copywriting Framework: {framework}

Ensure the post incorporates these key elements naturally:
- Emojis: Use a few professional emojis to improve engagement naturally throughout the post.
- Hashtags: Provide 5-8 relevant hashtags at the very end.

Make the output look natural and human-written, avoiding cliches, overly complex jargon,
or generic AI phrasing. Keep it simple, impactful, and structured according to the selected
framework. Use spacing and line breaks to make it easy to read on mobile.
"""

def build_prompt(inputs):
    prompt = LINKDIN_PROMPT_TEMPLATE.format(
        topic            = inputs["topic"],
        tone             = inputs["tone"],
        target_audience  = inputs["audience"],
        post_length      = inputs["length"],
        framework        = inputs["framework"]
    )
    return prompt

def generate_post(model, inputs):
    prompt   = build_prompt(inputs) #pehle we created our prompt.
    response = model.generate_content(prompt) #woh prompt gaya gemini model ke paas aur kuch reponse aaya
    post     = response.text.strip() #we get the required answer.
    return post