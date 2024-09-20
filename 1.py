from PIL import Image
import numpy as np

def LZW_encode(data):
    result = []
    w = ""
    dictionary = {chr(i): i for i in range(256)}
    
    for k in data:
        wk = w + k
        if wk in dictionary:
            w = wk
        else:
            result.append(dictionary[w])
            dictionary[wk] = len(dictionary)
            w = k

    if w:
        result.append(dictionary[w])

    return result, dictionary


def LZW_decode(encoded_data):
    dictionary = {i: chr(i) for i in range(256)}
    result = []
    w = str(chr(encoded_data[0]))
    result.append(w)

    for code in encoded_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = w + w[0]

        result.append(entry)
        dictionary[len(dictionary)] = w + entry[0]
        w = entry

    return ''.join(result)


def save_to_txt(data, filename):
    with open(filename, 'w') as file:
        file.write(data)


def read_from_txt(filename):
    with open(filename, 'r') as file:
        return file.read()


def save_dictionary_to_txt(dictionary, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for key, value in dictionary.items():
            key_str = ','.join(str(ord(char)) for char in key)
            value_str = str(value)
            file.write(f"{value_str}:{key_str}\n")

# Load the image (replace "your_image.png" with your image file)
original_image = Image.open("IMG_20190113_223244_482.jpg")

# Convert the image to a numpy array
image_array = np.array(original_image)

save_to_txt(','.join(map(str, image_array.flatten())), "data.txt")
# Flatten the array to a string for encoding
image_data = ''.join(map(chr, image_array.flatten()))

# Part 1: Encoding
encoded_data, dictionary = LZW_encode(image_data)
# Save encoded data to a text file
save_to_txt(','.join(map(str, encoded_data)), "encoded_data.txt")

# Save dictionary to a text file
save_dictionary_to_txt(dictionary, "dictionary.txt")
# Read encoded data from the text file
encoded_data_from_file = list(map(int, read_from_txt("encoded_data.txt").split(',')))

# Part 2: Decoding
decoded_data = LZW_decode(encoded_data_from_file)

# Convert decoded data back to a numpy array
decoded_array = np.array(list(map(ord, decoded_data)), dtype=np.uint8)
decoded_array = decoded_array.reshape(image_array.shape)

# Convert the numpy array back to an image
decoded_image = Image.fromarray(decoded_array)

# Display the original and decoded images
original_image.show(title="Original Image")
decoded_image.show(title="Decoded Image")
decoded_image.save("decoded.jpg")

# Efficiency comparison
original_size = len(image_data)
compressed_size = len(encoded_data) * 12 / 8  # Assuming each code is 12 bits
efficiency = compressed_size / original_size * 100

print("\nEfficiency Comparison:")
print(f"Original Size: {original_size} bytes")
print(f"Compressed Size: {compressed_size} bytes")
print(f"Efficiency: {efficiency:.2f}%")
