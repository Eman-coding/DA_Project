"""
Create 20 product images
Requires Pillow: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('static/images', exist_ok=True)

products = [
    ('modern_laptop_setup.jpg', (70, 130, 180), 'Laptop'),
    ('sleek_smartphone_minimal.jpg', (60, 60, 60), 'Phone'),
    ('wireless_speaker_lifestyle.jpg', (255, 99, 71), 'Speaker'),
    ('overear_headphones_studio.jpg', (138, 43, 226), 'Headphones'),
    ('smartwatch_clean_design.jpg', (34, 139, 34), 'Watch'),
    ('powerbank_desk_minimal.jpg', (255, 215, 0), 'PowerBank'),
    ('aesthetic_coffee_cup.jpg', (139, 69, 19), 'Coffee'),
    ('premium_catfood_pack.jpg', (255, 140, 0), 'Pet Food'),
    ('mechanical_keyboard_workspace.jpg', (25, 25, 112), 'Keyboard'),
    ('ergonomic_mouse_setup.jpg', (128, 128, 128), 'Mouse'),
    ('tablet_productivity_scene.jpg', (72, 61, 139), 'Tablet'),
    ('ultra_monitor_workspace.jpg', (0, 100, 0), 'Monitor'),
    ('digital_camera_studio.jpg', (105, 105, 105), 'Camera'),
    ('home_printer_setup.jpg', (192, 192, 192), 'Printer'),
    ('wifi_router_modern.jpg', (0, 191, 255), 'Router'),
    ('true_wireless_earbuds.jpg', (255, 20, 147), 'Earbuds'),
    ('bluetooth_speaker_modern.jpg', (0, 206, 209), 'BT Speaker'),
    ('gaming_controller_console.jpg', (220, 20, 60), 'Controller'),
    ('usb_flash_drive_clean.jpg', (255, 165, 0), 'USB Drive'),
    ('fast_charging_adapter.jpg', (50, 205, 50), 'Charger'),
]

for filename, color, text in products:
    width, height = 300, 300
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    
    # Gradient effect
    for i in range(height):
        r, g, b = color
        r = min(255, int(r + i / height * 20))
        g = min(255, int(g + i / height * 20))
        b = min(255, int(b + i / height * 20))
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Rectangle shape
    shape_size = 120
    x = (width - shape_size) // 2
    y = (height - shape_size) // 2 - 20
    draw.rectangle([x, y, x + shape_size, y + shape_size], 
                  fill=(255, 255, 255, 180), outline=(255, 255, 255), width=3)
    
    # Text
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 32)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    text_y = y + shape_size + 15
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)
    
    img_path = os.path.join('static/images', filename)
    img.save(img_path, 'JPEG', quality=85)
    print(f"Created: {img_path}")

print(f"\nSuccessfully created {len(products)} images!")





