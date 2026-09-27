def build_comic_layout(outline, full_story, image_urls):
    panels = []
    for i, o in enumerate(outline):
        panels.append({
            "panel_number": i+1,
            "title": o.get("title", f"Panel {i+1}"),
            "image_url": image_urls[i] if i < len(image_urls) else "",
            "dialogue": o.get("dialogue", ""),
            "narration": o.get("narration", "")
        })
    return {"panels": panels}