import os
from PIL import Image

def convert_to_jpg(input_dir, output_dir):
    """
    Convert all images from input_dir to JPG and save in output_dir
    
    Args:
        input_dir: Folder with original images (test/)
        output_dir: Folder to save converted JPGs (Parrot_new/)
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\n{'='*60}")
    print(f"Converting images to JPG")
    print(f"{'='*60}")
    print(f"Input:  {input_dir}")
    print(f"Output: {output_dir}")
    
    # Check if input directory exists
    if not os.path.exists(input_dir):
        print(f"❌ ERROR: Input directory does not exist!")
        return
    
    # Get all files
    files = os.listdir(input_dir)
    print(f"\nFound {len(files)} files")
    
    converted = 0
    already_jpg = 0
    errors = 0
    img_num = 0
    
    for i, filename in enumerate(files, 1):
        file_path = os.path.join(input_dir, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
        
        # Get file extension
        name_without_ext = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1].lower()
        
        # Create output path (always .jpg)
        img_num += 1
        new_filename = f"par_{img_num}.jpg"
        output_path = os.path.join(output_dir, new_filename)  # Fixed: was missing output_dir
        
        try:
            # Open image
            img = Image.open(file_path)
            
            # Convert to RGB if necessary (handles RGBA, grayscale, etc.)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Save as JPG
            img.save(output_path, 'JPEG', quality=95)
            
            if ext == '.jpg':
                already_jpg += 1
                print(f"  [{i}/{len(files)}] ✓ Copied: {filename}")
            else:
                converted += 1
                print(f"  [{i}/{len(files)}] ✓ Converted: {filename} → {new_filename}")
            
        except Exception as e:
            errors += 1
            print(f"  [{i}/{len(files)}] ✗ Error: {filename} - {str(e)}")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"CONVERSION SUMMARY")
    print(f"{'='*60}")
    print(f"  Total files: {len(files)}")
    print(f"  ✓ Already JPG (copied): {already_jpg}")
    print(f"  ✓ Converted to JPG: {converted}")
    print(f"  ✗ Errors: {errors}")
    print(f"  → Total JPG images saved: {already_jpg + converted}")
    print(f"{'='*60}\n")


# ============================================
# MAIN EXECUTION
# ============================================

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths
input_dir = os.path.join(script_dir, 'Parrot')      # Input: PetImages/test/
output_dir = os.path.join(script_dir, 'Parrot_new')  # Output: PetImages/Parrot_new/

# Run conversion
convert_to_jpg(input_dir, output_dir)

print("✓ Conversion complete!")
print(f"Converted images saved to: {output_dir}")