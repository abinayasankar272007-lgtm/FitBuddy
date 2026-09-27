import os
import google.generativeai as genai

def generate_story(outline, user_prompt, character, setting, tone):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or "Your-Real-Key" in api_key:
        story = ""
        for p in outline:
            story += f"---PANEL {p['panel']}---\n[Narration: {p['scene_description']}]\n{character}: \"This {tone} adventure is amazing!\"\n\n"
        return story
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    outline_text = "\n".join([f"Panel {p['panel']}: {p['title']} - {p['scene_description']}" for p in outline])
    prompt = f"You are comic writer. Expand outline into narration and dialogues. Idea: {user_prompt} Character: {character} Setting: {setting} Tone: {tone} Outline: {outline_text} For each panel write [Narration:...] Character: dialogue. Separate with ---PANEL X---"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(e)
        return "\n\n".join([f"---PANEL {p['panel']}---\n[Narration: {p['scene_description']}]" for p in outline])