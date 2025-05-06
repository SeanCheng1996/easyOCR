import os.path

import cv2
import easyocr
import matplotlib.patches as patches
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img_path = "../examples/dog_texts.jpg"
    img = cv2.imread(img_path)
    print(type(img))
    print(img.shape)

    reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
    result = reader.readtext(img)
    print(
        result)  # list of tuple. Foe each tuple: ([[topleft_x, topleft_y],[topright_x, topright_y],[botright_x, botright_y],[botleft_x, botleft_y] ], 'word', confidence_level).

    # visualize bounding box
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(img)
    for detection in result:
        points = detection[0]
        poly = patches.Polygon(points, linewidth=2,
                               edgecolor='r', facecolor='none')
        ax.add_patch(poly)

        plt.text(points[0][0], points[0][1], f'{detection[1]} ({detection[2]:.2f})',
                 color='blue', fontsize=10, bbox=dict(facecolor='yellow', alpha=0.5))
    plt.axis('off')
    plt.tight_layout()

    savedir = f"./word_bbox/{os.path.basename(img_path).split('.')[0]}/img_bbox.png"
    os.makedirs(os.path.dirname(savedir), exist_ok=True)
    plt.savefig(savedir)
    plt.show()
