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