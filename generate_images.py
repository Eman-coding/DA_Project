"""
Script to generate placeholder product images
Creates 20 product images with different colors and simple designs
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Product image configurations
products = [
    {'filename': 'modern_laptop_setup.jpg', 'color': (70, 130, 180), 'text': 'Laptop'},
    {'filename': 'sleek_smartphone_minimal.jpg', 'color': (60, 60, 60), 'text': 'Phone'},
    {'filename': 'wireless_speaker_lifestyle.jpg', 'color': (255, 99, 71), 'text': 'Speaker'},
    {'filename': 'overear_headphones_studio.jpg', 'color': (138, 43, 226), 'text': 'Headphones'},
    {'filename': 'smartwatch_clean_design.jpg', 'color': (34, 139, 34), 'text': 'Watch'},
    {'filename': 'powerbank_desk_minimal.jpg', 'color': (255, 215, 0), 'text': 'PowerBank'},
    {'filename': 'aesthetic_coffee_cup.jpg', 'color': (139, 69, 19), 'text': 'Coffee'},
    {'filename': 'premium_catfood_pack.jpg', 'color': (255, 140, 0), 'text': 'Pet Food'},
    {'filename': 'mechanical_keyboard_workspace.jpg', 'color': (25, 25, 112), 'text': 'Keyboard'},
    {'filename': 'ergonomic_mouse_setup.jpg', 'color': (128, 128, 128), 'text': 'Mouse'},
    {'filename': 'tablet_productivity_scene.jpg', 'color': (72, 61, 139), 'text': 'Tablet'},
    {'filename': 'ultra_monitor_workspace.jpg', 'color': (0, 100, 0), 'text': 'Monitor'},
    {'filename': 'digital_camera_studio.jpg', 'color': (105, 105, 105), 'text': 'Camera'},
    {'filename': 'home_printer_setup.jpg', 'color': (192, 192, 192), 'text': 'Printer'},
    {'filename': 'wifi_router_modern.jpg', 'color': (0, 191, 255), 'text': 'Router'},
    {'filename': 'true_wireless_earbuds.jpg', 'color': (255, 20, 147), 'text': 'Earbuds'},
    {'filename': 'bluetooth_speaker_modern.jpg', 'color': (0, 206, 209), 'text': 'BT Speaker'},
    {'filename': 'gaming_controller_console.jpg', 'color': (220, 20, 60), 'text': 'Controller'},
    {'filename': 'usb_flash_drive_clean.jpg', 'color': (255, 165, 0), 'text': 'USB Drive'},
    {'filename': 'fast_charging_adapter.jpg', 'color': (50, 205, 50), 'text': 'Charger'},
]

def create_product_image(filename, color, text):
    """Create a simple product placeholder image"""
    # Create image with gradient background
    width, height = 300, 300
    image = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(image)
    
    # Add gradient effect
    for i in range(height):
        alpha = int(255 * (1 - i / height * 0.3))
        r, g, b = color
        r = min(255, r + int(i / height * 20))
        g = min(255, g + int(i / height * 20))
        b = min(255, b + int(i / height * 20))
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Add a simple shape (rectangle) to represent product
    shape_size = 120
    x = (width - shape_size) // 2
    y = (height - shape_size) // 2 - 20
    draw.rectangle([x, y, x + shape_size, y + shape_size], 
                   fill=(255, 255, 255, 180), outline=(255, 255, 255), width=3)
    
    # Add text
    try:
        # Try to use a nice font
        font = ImageFont.truetype("arial.ttf", 32)
    except:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 32)
        except:
            font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Draw text centered
    text_x = (width - text_width) // 2
    text_y = y + shape_size + 15
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)
    
    # Save image
    image_path = os.path.join('static/images', filename)
    image.save(image_path, 'JPEG', quality=85)
    print(f"Created: {image_path}")

if __name__ == '__main__':
    print("Generating product images...")
    for product in products:
        create_product_image(product['filename'], product['color'], product['text'])
    print(f"\nSuccessfully created {len(products)} product images in static/images/")





