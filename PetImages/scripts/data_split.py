import os
import shutil 
import random 
from pathlib import Path

def split_train_val_test(source_dir, output_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=42):
    """
    Splitting images into train/val/test sets

    Arguments:
        source_dir: Directory with class folders (cat_resized, dog_resized, parrot_resized)
        output_dir: Where we save split data
        train_ratio: Proportion for training
        val_ratio: Proportion for validation
        test_ratio: Proportion for test
        seed: reproducibility

    """

    random.seed(seed)

    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 0.001, "Ratios sum must be 1!"

    classes = [d for d in os.listdir(source_dir)
               if os.path.isdir(os.path.join(source_dir, d)) and not d.startswith('.')]
    
    print(f"\nFound Classes: {', '.join(classes)}")

    splits = ['train', 'val', 'test']
    for split in splits:
        for class_name in classes:
            split_dir = os.path.join(output_dir, split, class_name)
            os.makedirs(split_dir, exist_ok=True)

    print(f"\nOutput directory: {output_dir}/")

    print("\nStarting processing - ")

    total_stats = {'train': 0, 'val': 0, 'test': 0}

    for class_name in classes:
        print(f"Class: ", {class_name})

        class_dir = os.path.join(source_dir, class_name)
        images = [f for f in os.listdir(class_dir)
                  if f.lower().endswith('.jpg')]
        
        total_images = len(images)
        print(f"All Images: {total_images}")

        # we shuffly all the images randomly
        random.shuffle(images)

        train_end = int(total_images * train_ratio)
        val_end = train_end + int(total_images * val_ratio )

        # Splitting images 
        train_images = images[:train_end]
        val_images = images[train_end:val_end]
        test_images = images[val_end:]

        print(f" -> Train: {len(train_images)} ")
        print(f" -> Val: {len(val_images)} ")
        print(f" -> Test: {len(test_images)} ")

        # Copy all the images to folders

        for split_name, image_list in [('train', train_images),
                                       ('val', val_images),
                                       ('test', test_images)]:
            for image_name in image_list:
                src = os.path.join(class_dir, image_name)
                dst = os.path.join(output_dir, split_name, class_name, image_name)
                shutil.copy2(src, dst)

            total_stats[split_name] += len(image_list)
        print()
    
    return total_stats


split_train_val_test("PetImages/resized", "PetImages/splitted")