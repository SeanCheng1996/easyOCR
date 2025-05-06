import cv2
import easyocr
import matplotlib.patches as patches
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img=cv2.imread("../dog_texts.jpg")
    print(type(img))
    print(img.shape)

    reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
    result = reader.readtext(img)
    print(result) # list of tuple. Foe each tuple: ([[topleft_x, topleft_y],[topright_x, topright_y],[botright_x, botright_y],[botleft_x, botleft_y] ], 'word', confidence_level).

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
    plt.show()

    # do inpaint