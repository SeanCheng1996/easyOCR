import os
from segment_anything import sam_model_registry

# create folders
os.makedirs("../models", exist_ok=True)

# download SAM
SAM_MODEL_URL = "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth"
SAM_MODEL_PATH = "../models/sam_vit_h_4b8939.pth"

if not os.path.exists(SAM_MODEL_PATH):
    os.system(f"wget {SAM_MODEL_URL} -O {SAM_MODEL_PATH}")