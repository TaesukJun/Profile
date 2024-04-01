#%%

# Import the necessary libraries 
from PIL import Image 
import pytesseract

# If you're on windows, you will need to point pytesseract to the path 
# where you installed Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
language = 'kor'

# Open the image file 
# replace 'test.png' with your image file 
img = Image.open('images/exampleText04.jpg')
 
# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img,lang='jpn_vert')
 
# Print the text print(text)
print(text)
#%%