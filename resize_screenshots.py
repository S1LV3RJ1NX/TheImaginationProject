"""
App Store Connect Screenshot Resizer

Resizes screenshots from TheImaginationProject/images/ to all required
App Store Connect sizes. Uses macOS built-in `sips` (no dependencies needed).

Required sizes for App Store Connect:
  - 6.7" iPhone (iPhone 15 Pro Max): 1290 x 2796
  - 6.5" iPhone (iPhone 14 Plus):    1284 x 2778
  - 5.5" iPhone (iPhone 8 Plus):     1242 x 2208

Usage:
  python3 resize_screenshots.py
"""

import os
import subprocess
import shutil

# --- Configuration ---

INPUT_DIR = os.path.join(os.path.dirname(__file__), "images")
OUTPUT_BASE = os.path.join(os.path.dirname(__file__), "appstore_screenshots")

# App Store Connect required sizes (width x height, portrait)
SIZES = {
    "6.5_inch": (1284, 2778),   # iPhone 14 Plus / 15 Plus
}

# --- Helpers ---

def resize_image(src_path, dst_path, width, height):
    """Resize image using macOS sips (no pip install needed)."""
    # Copy first, then resize in-place (sips modifies files in-place)
    shutil.copy2(src_path, dst_path)
    
    subprocess.run(
        ["sips", "--resampleHeightWidth", str(height), str(width), dst_path],
        capture_output=True,
        check=True,
    )

def main():
    # Find all PNG screenshots
    images = sorted([
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith(".png")
    ])
    
    if not images:
        print("❌ No PNG images found in", INPUT_DIR)
        return
    
    print(f"📸 Found {len(images)} screenshots in {INPUT_DIR}")
    print()
    
    # Get source dimensions
    first = os.path.join(INPUT_DIR, images[0])
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", first],
        capture_output=True, text=True,
    )
    print(f"📐 Source size: {result.stdout.strip().split(chr(10))[-2].split()[-1]} x {result.stdout.strip().split(chr(10))[-1].split()[-1]}")
    print()
    
    # Create output directories and resize
    for size_name, (w, h) in SIZES.items():
        out_dir = os.path.join(OUTPUT_BASE, size_name)
        os.makedirs(out_dir, exist_ok=True)
        
        print(f"🔄 Resizing to {size_name} ({w}x{h})...")
        
        for img in images:
            src = os.path.join(INPUT_DIR, img)
            dst = os.path.join(out_dir, img)
            resize_image(src, dst, w, h)
            print(f"   ✅ {img} → {w}x{h}")
        
        print()
    
    print(f"✅ Done! Screenshots saved to: {OUTPUT_BASE}/")
    print()
    print("📁 Upload these folders to App Store Connect:")
    for size_name, (w, h) in SIZES.items():
        count = len(images)
        print(f"   {size_name}/ → {count} images ({w}x{h})")

if __name__ == "__main__":
    main()
