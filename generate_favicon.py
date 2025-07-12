#!/usr/bin/env python3
"""
Generate favicon files from SVG using PIL/Pillow
"""

from PIL import Image, ImageDraw
import os

def create_favicon():
    """Create a large, prominent 3D cube favicon"""
    
    # Create a 32x32 image with transparent background
    size = 32
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a larger 3D cube that fills most of the space
    center_x, center_y = size // 2, size // 2
    
    # Much larger cube dimensions - use most of the available space
    cube_size = 22  # Increased from 10 to 22
    offset = 5      # Isometric offset for 3D effect
    
    # Define cube points (isometric view with better proportions)
    # Front face (main visible face)
    front_points = [
        (center_x - cube_size//2, center_y - cube_size//3),      # top-left
        (center_x + cube_size//2, center_y - cube_size//3),      # top-right
        (center_x + cube_size//2, center_y + cube_size//3),      # bottom-right
        (center_x - cube_size//2, center_y + cube_size//3)       # bottom-left
    ]
    
    # Top face (visible top)
    top_points = [
        (center_x - cube_size//2, center_y - cube_size//3),          # front-left
        (center_x - cube_size//2 + offset, center_y - cube_size//3 - offset),  # back-left
        (center_x + cube_size//2 + offset, center_y - cube_size//3 - offset),  # back-right
        (center_x + cube_size//2, center_y - cube_size//3)            # front-right
    ]
    
    # Right face (visible right side)
    right_points = [
        (center_x + cube_size//2, center_y - cube_size//3),          # top-front
        (center_x + cube_size//2 + offset, center_y - cube_size//3 - offset),  # top-back
        (center_x + cube_size//2 + offset, center_y + cube_size//3 - offset),  # bottom-back
        (center_x + cube_size//2, center_y + cube_size//3)           # bottom-front
    ]
    
    # Draw cube faces with better colors and contrast
    # Front face - brightest (main face)
    draw.polygon(front_points, fill=(255, 255, 255, 255))  # Pure white front
    
    # Top face - medium brightness
    draw.polygon(top_points, fill=(200, 220, 255, 255))    # Light blue top
    
    # Right face - darker for depth
    draw.polygon(right_points, fill=(150, 180, 255, 255))  # Darker blue right
    
    # Add strong edge lines for better definition
    draw.polygon(front_points, outline=(0, 123, 255, 255), width=2)  # Bootstrap blue edges
    draw.polygon(top_points, outline=(0, 123, 255, 255), width=2)
    draw.polygon(right_points, outline=(0, 123, 255, 255), width=2)
    
    # Add internal edges for more 3D definition
    draw.line([front_points[1], top_points[3]], fill=(0, 123, 255, 255), width=2)  # top-right edge
    draw.line([front_points[2], right_points[3]], fill=(0, 123, 255, 255), width=2)  # bottom-right edge
    
    return img

def save_favicon_formats(img):
    """Save favicon in multiple formats"""
    
    # Save as ICO (16x16 and 32x32)
    favicon_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    favicon_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    
    # Create ICO file with multiple sizes
    favicon_16.save('static/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32)])
    
    # Save as PNG for modern browsers
    img.save('static/favicon-32x32.png', format='PNG')
    favicon_16.save('static/favicon-16x16.png', format='PNG')
    
    # Save larger sizes for mobile/app icons
    img.resize((192, 192), Image.Resampling.LANCZOS).save('static/android-chrome-192x192.png', format='PNG')
    img.resize((180, 180), Image.Resampling.LANCZOS).save('static/apple-touch-icon.png', format='PNG')
    
    print("✓ Generated favicon.ico")
    print("✓ Generated favicon-16x16.png")
    print("✓ Generated favicon-32x32.png")
    print("✓ Generated android-chrome-192x192.png")
    print("✓ Generated apple-touch-icon.png")

if __name__ == "__main__":
    try:
        print("Generating favicon files...")
        
        # Ensure static directory exists
        os.makedirs('static', exist_ok=True)
        
        # Create the base favicon image
        favicon_img = create_favicon()
        
        # Save in multiple formats
        save_favicon_formats(favicon_img)
        
        print("\n🎉 Favicon generation complete!")
        print("Files saved in the 'static' directory.")
        
    except ImportError:
        print("❌ PIL/Pillow not installed. Installing...")
        import subprocess
        import sys
        
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
            print("✓ Pillow installed. Please run the script again.")
        except:
            print("❌ Failed to install Pillow. You can install it manually with: pip install pillow")
    except Exception as e:
        print(f"❌ Error generating favicon: {e}")
        print("Using SVG favicon instead.")