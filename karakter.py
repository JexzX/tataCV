import cv2
import numpy as np

def create_solar_system():
    canvas = np.zeros((600, 800, 3), dtype=np.uint8)
    
    cv2.circle(canvas, (400, 300), 50, (0, 255, 255), -1)
    
    cv2.circle(canvas, (300, 300), 20, (0, 0, 255), -1)
    cv2.circle(canvas, (500, 200), 30, (255, 100, 0), -1)
    cv2.circle(canvas, (600, 400), 25, (0, 255, 0), -1)
    
    cv2.circle(canvas, (200, 450), 35, (200, 200, 100), -1)
    cv2.ellipse(canvas, (200, 450), (60, 20), 0, 0, 360, (200, 200, 100), 2)
    
    stars = [(100, 100), (700, 150), (150, 500), (650, 550), (50, 300)]
    for star in stars:
        cv2.circle(canvas, star, 3, (255, 255, 255), -1)
    
    cv2.imwrite('output/karakter.png', canvas)
    print("Solar system character created: output/karakter.png")
    
    return canvas

if __name__ == "__main__":
    create_solar_system()

def apply_transformations():
    original_image = cv2.imread('output/karakter.png')
    height, width = original_image.shape[:2]
    
    print("Applying geometric transformations...")
    
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_image = cv2.warpAffine(original_image, rotation_matrix, (width, height))
    cv2.imwrite('output/rotate.png', rotated_image)
    print("Rotation completed: output/rotate.png")
    
    new_size = (width // 2, height // 2)
    resized_image = cv2.resize(original_image, new_size)
    cv2.imwrite('output/resize.png', resized_image)
    print("Resize completed: output/resize.png")
    
    x1, y1 = 150, 400
    x2, y2 = 250, 500
    cropped_image = original_image[y1:y2, x1:x2]
    cv2.imwrite('output/crop.png', cropped_image)
    print("Crop completed: output/crop.png")

if __name__ == "__main__":
    create_solar_system()
    apply_transformations()

def apply_bitwise_operations():
    original_image = cv2.imread('output/karakter.png')
    
    print("Applying bitwise operations...")
    
    background = np.zeros((600, 800, 3), dtype=np.uint8)
    for i in range(600):
        color_value = 150 + int(i * 0.1)
        background[i] = (color_value, color_value, 255)
    
    cv2.imwrite('output/background.png', background)
    print("Background created: output/background.png")
    
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    result_and = cv2.bitwise_and(background, mask_rgb)
    cv2.imwrite('output/bitwise_and.png', result_and)
    print("Bitwise AND completed: output/bitwise_and.png")
    
    result_or = cv2.bitwise_or(background, original_image)
    cv2.imwrite('output/bitwise_or.png', result_or)
    print("Bitwise OR completed: output/bitwise_or.png")

if __name__ == "__main__":
    create_solar_system()
    apply_transformations()
    apply_bitwise_operations()