import pyperclip
import base64,sys

if len(sys.argv) != 2:
    print("Incorrect argument numbers. Include file to be encoded.")

image = open(sys.argv[1], 'rb') 
image_read = image.read() 
print("Encoding image...")
image_64_encode = base64.encodestring(image_read) if sys.version_info <(3,9) else base64.encodebytes(image_read)
image_string = str(image_64_encode)
image_string = image_string.replace("\\n", "")
image_string = image_string.replace("b'", "")
image_string = image_string.replace("'", "")
image_string = '![image.' + sys.argv[1][sys.argv[1].rfind('.') + 1:] + '](data:image/' + sys.argv[1][sys.argv[1].rfind('.') + 1:] + ';base64,' + image_string + ')'
print("File written. Pasting to clipboard...")
pyperclip.copy(image_string)
print("Done.")