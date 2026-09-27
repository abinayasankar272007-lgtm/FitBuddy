from pydantic import BaseModel
class PromptRequest(BaseModel):
    story_prompt: str
    character_name: str = "Hero"
    setting: str = "forest"
    tone: str = "dramatic"
    art_style: str = "comic book"