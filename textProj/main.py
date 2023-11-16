import pywhatkit as kit

text = input("Please type in your text here:")

# Specify the path for the output image file
output_path = "handwriting.png"

# Use pywhatkit.text_to_handwriting() function
kit.text_to_handwriting(text, output_path, [0, 0, 0])

print(f"Handwriting image saved at: {output_path}")

#THis prints unable to access pywhatkit api right now
