from PIL import Image
import os


def create_spritesheet(input_folder, output_path="spritesheet.png"):
    # Get all image filenames sorted numerically
    images = sorted(
        [
            f
            for f in os.listdir(input_folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg"))
        ]
    )

    # Open all images
    opened_images = [Image.open(os.path.join(input_folder, img)) for img in images]
    widths, heights = zip(*(img.size for img in opened_images))

    # Compute total width and max height
    total_width = sum(widths)
    max_height = max(heights)

    # Create new image
    spritesheet = Image.new("RGBA", (total_width, max_height))

    # Paste images one after another
    x_offset = 0
    for img in opened_images:
        spritesheet.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save final spritesheet
    spritesheet.save(output_path)
    print(f"Spritesheet saved as {output_path} ({total_width}x{max_height})")


path = input("Path to images folder: ")
create_spritesheet(path)
