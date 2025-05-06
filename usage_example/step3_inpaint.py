import cv2
import numpy as np
import subprocess
from pathlib import Path
import easyocr
import os

# 1. detect word
reader = easyocr.Reader(['en'])
image_path = Path("../examples/dog_texts.jpg")
results = reader.readtext(str(image_path))

# 2. generate mask
image = cv2.imread(str(image_path))
mask = np.zeros(image.shape[:2], dtype=np.uint8)
for (points, _, _) in results:
    cv2.fillPoly(mask, [np.array(points, dtype=np.int32)], 255)
mask_path = f"./masks/{os.path.basename(image_path)}/mask.png"
os.makedirs(os.path.dirname(mask_path), exist_ok=True)
cv2.imwrite(mask_path, mask)

# 3. 调用LaMa修复（修正参数名称）
subprocess.run([
    "python",
    "../Inpaint-Anything/lama_inpaint.py",
    "--input_img", str(image_path),
    "--input_mask_glob", mask_path,
    "--output_dir", "./results",
    "--lama_config", "../Inpaint-Anything/lama/configs/prediction/default.yaml",
    "--lama_ckpt", "../pretrained_models/big-lama"
], check=True)