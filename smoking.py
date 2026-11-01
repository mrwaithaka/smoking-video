
import subprocess
from pathlib import Path

image = Path("a_realistic_outdoor_scene_in_front_of_a_house_door.png")
output = Path("man_outside_door.mp4")

if not image.exists():
    raise FileNotFoundError(
        f"Image not found: {image.resolve()}\n"
        "Put the generated image in this folder."
    )

# Create an 8-second video with a gentle cinematic zoom.
command = [
    "ffmpeg",
    "-y",
    "-loop", "1",
    "-framerate", "24",
    "-i", str(image),
    "-t", "8",
    "-vf",
    (
        "scale=1920:1080:force_original_aspect_ratio=increase,"
        "crop=1920:1080,"
        "zoompan=z='min(zoom+0.00035,1.035)':"
        "x='iw/2-(iw/zoom/2)':"
        "y='ih/2-(ih/zoom/2)':"
        "d=1:s=1920x1080:fps=24,"
        "format=yuv420p"
    ),
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "20",
    "-an",
    str(output)
]

subprocess.run(command, check=True)
print(f"Video created: {output.resolve()}")

