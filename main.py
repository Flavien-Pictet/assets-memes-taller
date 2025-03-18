import json
import os
import random
import sys
import traceback
from PIL import Image, ImageDraw, ImageFont
import textwrap
import glob
from data import generate_data_file

# Constants
OUTPUT_DIR = "output"
CAROUSEL_DIR = os.path.join(OUTPUT_DIR, "carousels")
ASSETS_DIR = "assets"
BACKGROUNDS_DIR = os.path.join(ASSETS_DIR, "backgrounds")
CONTENT_IMAGES_DIR = os.path.join(ASSETS_DIR, "content_images")
FONTS_DIR = "fonts"

# Font paths
TITLE_FONT_PATH = os.path.join(FONTS_DIR, "CabinetGrotesk-Extrabold.ttf")
BODY_FONT_PATH = os.path.join(FONTS_DIR, "5en.ttf")

# Slide dimensions
SLIDE_WIDTH = 1080
SLIDE_HEIGHT = 1080

def print_debug(message):
    """Print debug message"""
    print(f"DEBUG: {message}")

def create_directories():
    """Create necessary directories"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(CAROUSEL_DIR, exist_ok=True)
    print_debug(f"Created output directories: {OUTPUT_DIR}, {CAROUSEL_DIR}")

def find_categorized_images():
    """Find images and categorize them by type"""
    # Define categories
    categories = ["food", "exercises", "sleep", "negative", "symptoms"]
    
    # Initialize image collections
    categorized_backgrounds = {}
    categorized_content = {}
    
    for category in categories:
        categorized_backgrounds[category] = []
        categorized_content[category] = []
    
    # Search in both absolute and relative paths
    base_paths = [
        "/Users/picsou/Projects/Taller/assets",
        "assets"
    ]
    
    for base_path in base_paths:
        if os.path.exists(base_path):
            print_debug(f"Searching in {base_path}")
            
            # Search for background images
            bg_path = os.path.join(base_path, "backgrounds")
            if os.path.exists(bg_path):
                for category in categories:
                    category_path = os.path.join(bg_path, category)
                    if os.path.exists(category_path):
                        for file in os.listdir(category_path):
                            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                                img_path = os.path.join(category_path, file)
                                categorized_backgrounds[category].append(img_path)
                                print_debug(f"Found {category} background: {img_path}")
            
            # Search for content images
            content_path = os.path.join(base_path, "content_images")
            if os.path.exists(content_path):
                for category in categories:
                    category_path = os.path.join(content_path, category)
                    if os.path.exists(category_path):
                        for file in os.listdir(category_path):
                            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                                img_path = os.path.join(category_path, file)
                                categorized_content[category].append(img_path)
                                print_debug(f"Found {category} content image: {img_path}")
    
    # Print summary
    for category in categories:
        bg_count = len(categorized_backgrounds[category])
        content_count = len(categorized_content[category])
        print_debug(f"Category '{category}': {bg_count} backgrounds, {content_count} content images")
    
    return categorized_backgrounds, categorized_content

def create_slide_with_large_title(title, background_path=None, content_image_path=None):
    """Create a slide with a very large title"""
    # Create a blank slide with light background
    slide = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), color=(240, 240, 240))
    draw = ImageDraw.Draw(slide)
    
    # Try to load background if provided
    if background_path and os.path.exists(background_path):
        try:
            print_debug(f"Loading background: {background_path}")
            background = Image.open(background_path).convert('RGB')
            background = background.resize((SLIDE_WIDTH, SLIDE_HEIGHT))
            slide.paste(background, (0, 0))
            print_debug("Background loaded successfully")
            
            # Add a semi-transparent overlay for text readability
            overlay = Image.new('RGBA', (SLIDE_WIDTH, SLIDE_HEIGHT), (255, 255, 255, 100))
            slide = Image.alpha_composite(slide.convert('RGBA'), overlay).convert('RGB')
            draw = ImageDraw.Draw(slide)
        except Exception as e:
            print_debug(f"Error loading background: {e}")
    
    # Try to load content image if provided
    if content_image_path and os.path.exists(content_image_path):
        try:
            print_debug(f"Loading content image: {content_image_path}")
            content_img = Image.open(content_image_path).convert('RGBA')
            
            # Calculate size to maintain aspect ratio
            img_width, img_height = content_img.size
            max_width = SLIDE_WIDTH - 200  # Padding on sides
            max_height = SLIDE_HEIGHT // 2  # Use half the slide height
            
            # Resize while maintaining aspect ratio
            if img_width > max_width:
                ratio = max_width / img_width
                img_width = int(img_width * ratio)
                img_height = int(img_height * ratio)
            
            if img_height > max_height:
                ratio = max_height / img_height
                img_height = int(img_height * ratio)
                img_width = int(img_width * ratio)
            
            content_img = content_img.resize((img_width, img_height))
            
            # Calculate position (center horizontally, below title)
            x_pos = (SLIDE_WIDTH - img_width) // 2
            y_pos = SLIDE_HEIGHT - img_height - 100  # Position at bottom with padding
            
            # Create a temporary image for pasting
            temp = Image.new('RGBA', (SLIDE_WIDTH, SLIDE_HEIGHT), (0, 0, 0, 0))
            temp.paste(content_img, (x_pos, y_pos), content_img if content_img.mode == 'RGBA' else None)
            
            # Composite the content image onto the slide
            slide = Image.alpha_composite(slide.convert('RGBA'), temp).convert('RGB')
            draw = ImageDraw.Draw(slide)
            print_debug("Content image loaded successfully")
        except Exception as e:
            print_debug(f"Error loading content image: {e}")
    
    # Add title text with MUCH larger font
    try:
        # 500% larger font (5x original size)
        font_size = 300  # Increased from 60
        
        if os.path.exists(TITLE_FONT_PATH):
            font = ImageFont.truetype(TITLE_FONT_PATH, font_size)
        else:
            # If custom font not available, use default but still try to make it larger
            font = ImageFont.load_default()
            print_debug("Using default font as title font not found")
        
        # Draw title text
        title_lines = textwrap.wrap(title, width=10)  # Fewer words per line due to larger font
        y_text = 100
        
        for line in title_lines:
            # Center the text
            text_width = draw.textlength(line, font=font)
            x_position = (SLIDE_WIDTH - text_width) // 2
            
            # Draw the text
            draw.text((x_position, y_text), line, fill=(0, 0, 0), font=font)
            y_text += font_size * 1.2
    except Exception as e:
        print_debug(f"Error adding title text: {e}")
    
    return slide

def generate_themed_carousel(title, category, bg_images, content_images):
    """Generate a carousel with images matching the specified category"""
    print_debug(f"Generating {category} carousel: {title}")
    
    # Create directory for this carousel
    carousel_dir = os.path.join(CAROUSEL_DIR, title)
    os.makedirs(carousel_dir, exist_ok=True)
    
    # Create 3 slides with category-specific titles
    slide_titles = []
    if category == "food":
        slide_titles = [
            "Nutrition for Height",
            "Eat to Grow Taller",
            "Download Taller Today"
        ]
    elif category == "exercises":
        slide_titles = [
            "Exercises for Height",
            "Stretch to Grow Taller",
            "Download Taller Today"
        ]
    elif category == "sleep":
        slide_titles = [
            "Sleep for Height",
            "Rest to Grow Taller",
            "Download Taller Today"
        ]
    elif category == "negative":
        slide_titles = [
            "Avoid Height Blockers",
            "Things That Stunt Growth",
            "Download Taller Today"
        ]
    elif category == "symptoms":
        slide_titles = [
            "Signs of Growth",
            "Height Growth Indicators",
            "Download Taller Today"
        ]
    else:
        slide_titles = [
            f"Height Maxxing: {title}",
            "Increase Your Height",
            "Download Taller Today"
        ]
    
    # Ensure we have images for this category
    category_bg_images = bg_images.get(category, [])
    category_content_images = content_images.get(category, [])
    
    if not category_bg_images:
        print_debug(f"No background images for category {category}")
        # Try to use any available background
        for cat, images in bg_images.items():
            if images:
                category_bg_images = images
                print_debug(f"Using {cat} backgrounds instead")
                break
    
    if not category_content_images:
        print_debug(f"No content images for category {category}")
        # Try to use any available content images
        for cat, images in content_images.items():
            if images:
                category_content_images = images
                print_debug(f"Using {cat} content images instead")
                break
    
    # Create each slide
    for i, title in enumerate(slide_titles):
        # Select random images from the appropriate category
        bg_image = random.choice(category_bg_images) if category_bg_images else None
        content_image = random.choice(category_content_images) if category_content_images and i == 1 else None
        
        # Create the slide
        slide = create_slide_with_large_title(title, bg_image, content_image)
        
        # Save the slide
        slide_path = os.path.join(carousel_dir, f"slide_{i+1}.jpg")
        try:
            slide.save(slide_path, quality=95)
            print_debug(f"Saved slide to {slide_path}")
        except Exception as e:
            print_debug(f"Error saving slide: {e}")
    
    print_debug(f"Carousel {title} generated successfully")
    return carousel_dir

def main():
    print("Height Maxxing Carousel Generator")
    print("--------------------------------")
    
    # Create output directories
    create_directories()
    
    # Find and categorize images
    print_debug("Searching for categorized images...")
    categorized_backgrounds, categorized_content = find_categorized_images()
    
    # Define carousels to generate
    carousels = [
        {"title": "Nutrition_Tips", "category": "food"},
        {"title": "Exercise_Routine", "category": "exercises"},
        {"title": "Sleep_Optimization", "category": "sleep"}
    ]
    
    # Generate each carousel
    for carousel in carousels:
        generate_themed_carousel(
            carousel["title"],
            carousel["category"],
            categorized_backgrounds,
            categorized_content
        )
    
    # Verify output
    carousel_count = len(os.listdir(CAROUSEL_DIR))
    print(f"\nGenerated {carousel_count} carousels successfully!")
    print(f"Output saved to: {os.path.abspath(CAROUSEL_DIR)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
