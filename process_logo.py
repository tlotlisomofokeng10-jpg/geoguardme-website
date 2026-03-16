from PIL import Image

def process_logo(input_path, output_dark, output_light):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path).convert("RGBA")
        
        # 1. Crop
        bbox = img.getbbox()
        if not bbox:
            print("Empty image.")
            return
        img = img.crop(bbox)
        
        # Save dark version
        img.save(output_dark)
        print(f"Saved {output_dark} (size: {img.size})")
        
        # 2. Convert dark pixels to white for footer
        pixels = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    # The text and shield are very dark blue (almost black)
                    if r < 100 and g < 100 and b < 150:
                        # Map to white, preserving the original alpha
                        pixels[x, y] = (255, 255, 255, a)
                        
        img.save(output_light)
        print(f"Saved {output_light} (size: {img.size})")
    except Exception as e:
        print(f"Error: {e}")

process_logo("/Volumes/Untitled/whitelabel/SM Specialized Security/website/assets/1.png", 
             "/Volumes/Untitled/whitelabel/SM Specialized Security/website/assets/1_trim.png", 
             "/Volumes/Untitled/whitelabel/SM Specialized Security/website/assets/1_footer.png")
