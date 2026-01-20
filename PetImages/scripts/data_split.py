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


    
split_train_val_test("PetImages/resized", "PetImages/splitted")