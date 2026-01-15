import os 
from PIL import Image 
import shutil 


# Main function for resizing image
# For us standard size is 128x128x3

def resize_images(input_dir, output_dir, target_size=(128, 128)):
    """
        Take all the images from the input_dir, transform into
        target_size and save to output_dir

        Arguments:
            input_dir: Original Images
            output_idr: Saved resized images
            target_size: Tuple (W, H)
    """

    os.makedirs(output_dir, exist_ok=True)

    print(f"Input: {input_dir}")
    print(f"Output: {output_dir}")

    if not os.path.exists(input_dir):
        print("Input dir does not exist!")
        return 
    
    files = os.listdir(input_dir) 
    total = len(files)

    print(f"\nTotal: {total} images")

    resized = 0
    errors = 0 

    original_sizes = {}

    for i, filename in enumerate(files, 1):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try: 
            img = Image.open(input_path)
            original_size = img.size

            size_key = f"{original_size[0]}x{original_size[1]}"
            original_sizes[size_key] = original_sizes.get(size_key, 0) + 1

            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Using LANCZOS for high-quality downsampling
            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)

            # Save
            img_resized.save(output_path, 'JPEG', quality=95)

            resized += 1 

        except Exception as e:
            errors += 1 
            print(f"Error {filename}: {str(e)}")


resize_images('PetImages/raw/Cat', 'PetImages/resized/Cat_resized')
resize_images('PetImages/raw/Dog', 'PetImages/resized/Dog_resized')
resize_images('PetImages/raw/Parrot', 'PetImages/resized/Parrot_resized')