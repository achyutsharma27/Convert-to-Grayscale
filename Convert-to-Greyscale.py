import cv2 
import os

def convert_to_greyscale(input_path, output_path):
    image = cv2.imread(input_path)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, grey_image)
    
directory = 'D:\My_folder\Python\open CV'

for file in os.listdir(directory):
    if file.endswith('.jpeg') or file.endswith('.png'):
        input_path = os.path.join(directory, file)
        output_path = os.path.join(directory, 'greyscal_' + file)
        
        convert_to_greyscale(input_path, output_path)

print("All Images are converted in grey scale!")
