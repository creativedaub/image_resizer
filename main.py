from os import system
try:
    from PIL import Image
except ModuleNotFoundError:
    system("pip install pillow")


def resize_image(input_path: str, output_path: str, width: int, height: int):

    """
    Resizes an image file to the given width and height and saves the result to the output path.
    """
    # Open the image file
    image = Image.open(input_path)

    # Resize the image
    resized_image = image.resize((width, height))

    # Save the resized image to the output path
    resized_image.save(output_path)


def crop_image(file_path, width, height):
    """Crops an image to the given width and height."""
    # Open the image file
    with Image.open(file_path) as im:
        # Get the current size of the image
        image_width, image_height = im.size

        # Calculate the new size of the image based on the given width and height
        new_width = min(image_width, width)
        new_height = min(image_height, height)

        # Calculate the new top-left corner of the image based on the center of the original image
        left = (image_width - new_width) // 2
        top = (image_height - new_height) // 2

        # Crop the image
        im = im.crop((left, top, left + new_width, top + new_height))

        # Save the cropped image to a file
        im.save(file_path)


if __name__ == "__main__":
    ques = input("Crop or Resize? ")
    if ques:
        inpt = input("Enter image name/path: ")
        output = f"cropped_{inpt}"
        wt, ht = int(input("Enter desired width: ")), int(input("Enter desired height: "))
        if "c" in ques or "C" in ques:
            crop_image(inpt, wt, ht)
        if "r" in ques or "R" in ques:
            resize_image(inpt, output, wt, ht)
    else:
        print("Invalid Response!")
