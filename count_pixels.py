from PIL import Image

def count_light_pixels_tiff(image_path, threshold):
    # Load the image
    img = Image.open(image_path)
    pixels = img.load()  # Load the image's pixel data

    # Get the dimensions of the image
    width, height = img.size

    # Initialize the count of light pixels
    light_pixels = 0

    # Check how many channels the image has
    if img.mode == 'RGBA':
        channel_count = 4
    else:
        channel_count = 3

    for i in range(height):
        for j in range(width):
            # Get the pixel's values based on the number of channels
            pixel_values = pixels[j, i]
            if channel_count == 4:
                r, g, b, a = pixel_values
            else:
                r, g, b = pixel_values

            avg_color = (r + g + b) / 3
            #print(avg_color)
            #print(threshold)            
            if avg_color > threshold:
                light_pixels += 1
                # Change the pixel color to green
                if channel_count == 4:
                    pixels[j, i] = (0, 255, 0, a)  # Preserve the alpha channel
                else:
                    pixels[j, i] = (0, 255, 0)

    img.show()  # Display the modified image
    return light_pixels

# Example usage
image_path_1 = 'controlDual.png'
image_path_2 = 'openDual.png'

# Tune this threshold value parameter until accurate
light_pixels_1 = count_light_pixels_tiff(image_path_1, 160)
light_pixels_2 = count_light_pixels_tiff(image_path_2, 160)


print(f"Number of light pixels [controlDual]: {light_pixels_1}")
print(f"Number of light pixels [openDual]: {light_pixels_2}")


