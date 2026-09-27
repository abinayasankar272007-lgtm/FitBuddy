import random

def generate_image_prompt(panel_number, user_plot, setting, character, art_style):
    # Random seed - ithu dhan ore prompt ku kooda vera image vara trick!
    seed = random.randint(1000, 999999)
    
    base = f"{character} in {setting}, {art_style} style"
    
    if panel_number == 1:
        return f"{base}, discovering {user_plot}, beginning, curious face, seed {seed}"
    elif panel_number == 2:
        return f"{base}, shocked seeing future, closeup, dramatic, seed {seed+1}"
    elif panel_number == 3:
        return f"{base}, thinking alone, worried, seed {seed+2}"
    elif panel_number == 4:
        return f"closeup of laptop screen showing {user_plot} in {setting}, futuristic, seed {seed+3}"
    else:
        return f"{base}, happy ending celebrating with friends, joyful, seed {seed+4}"