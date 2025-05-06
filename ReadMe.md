This repo is for a tutorial environment setup and usage for word detection and inpainting for the word.
The model is [EasyOCR](https://github.com/JaidedAI/EasyOCR) and [Inpaint-Anything](https://github.com/geekyutao/Inpaint-Anything?tab=readme-ov-file).

The code examples are in the usage_example folder, containing 3 separate Python codes.
After you have prepared the environment, each Python file can run alone.

# 1. Create Conda Environment
> conda create -n easyocr python=3.10
> 
> conda activate easyocr

# 2. EasyOCR
First install torch with the right cuda version.
Find the corresponding command from pytorch official website.
https://pytorch.org/get-started/locally/
> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
> 
>  pip install easyocr

Now, you can run the step1 and step2

# 3. FillAnything
> pip install git+https://github.com/facebookresearch/segment-anything.git
> 
> pip install diffusers transformers scipy
> 
> pip install opencv-python matplotlib

go into your project folder
> cd /path/to/your/project
> 
> git clone https://github.com/geekyutao/Inpaint-Anything.git
> 
> cd Inpaint-Anything
> 
> python -m pip install -r lama/requirements.txt 
> 

Then, go to "./path/to/your/project/Inpaint-Anything/lama/saicinpainting/training/trainers/__init__.py", and modify the line 27:
from
> state = torch.load(path, map_location=map_location)

to
> to "state = torch.load(path, map_location=map_location, weights_only=False)"

Finally, go to https://drive.google.com/drive/folders/1ST0aRbDRZGli0r7OVVOQvXwtadMCuWXg

> Download the pretrained_models folder

Put the contents under:
> "./path/to/your/project/Inpaint-Anything/pretrained_models/" 

Now, you are able to run the step3.

You will see a "masks" folder and a "results" folder generated.

# 4. Example
Original Image: <img src="./examples/dog_texts.jpg">
Word bounding box: <img src="./usage_example/word_bbox/dog_texts/img_bbox.png">
Mask Image: <img src="./usage_example/masks/dog_texts/mask.png">
Filled Image: <img src="./usage_example/results/dog_texts/inpainted_with_mask.png">
