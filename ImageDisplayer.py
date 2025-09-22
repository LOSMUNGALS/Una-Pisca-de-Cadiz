import cv2
import os

if __name__ == "__main__":
    img_path = r"C:\Users\nicol\Documents\AP SoftwareD 1\skull.jpg" #Cambie esto a decir su ubicación de imagen.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(script_dir, "skull.jpg") #Cambie "skull.jpg" por el exacto nombre del archivo, incluyendo el .jpg, .jpeg o .png.

    img = cv2.imread(img_path)

    if img is None:
        print("Error: Could not read the image at", img_path)
    else:
        cv2.imshow("Skull Image", img) #Cambie "Skull Image" por el nombre que quiera que el archivo diga cuando salga.
        cv2.waitKey(0)
        cv2.destroyAllWindows()
