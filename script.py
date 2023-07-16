from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(image_paths, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    page_width, page_height = letter
    margin = 20  # Margin between images and page edges

    images_per_page = 3  # Number of images to display per page
    images_count = len(image_paths)
    pages_count = images_count // images_per_page

    for page in range(pages_count):
        for i in range(images_per_page):
            image_path = image_paths[page * images_per_page + i]
            img = Image.open(image_path)

            # Calculate the aspect ratio
            aspect_ratio = img.width / img.height

            # Calculate the available height for each image
            available_height = (page_height - (images_per_page + 1) * margin) / images_per_page

            # Calculate the width based on the available height
            img_width = aspect_ratio * available_height

            # Calculate the x and y coordinates for each image
            x = (page_width - img_width) / 2
            y = page_height - (i + 1) * (margin + available_height)

            # Add the image to the PDF, stretching it to the full width
            c.drawImage(image_path, x, y, img_width, available_height)

        # Add a new page if there are more images
        if page < pages_count - 1:
            c.showPage()

    c.save()
    print("PDF creation complete.")

# Provide the directory path containing your images
image_directory = "C:/Users/ahmed/OneDrive/Desktop/91/91img"

#IMG-20230608-WA0018

image_paths = [f"{image_directory}/IMG-20230608-WA0{str(i).zfill(3)}.jpg" for i in range(10, 99)]
output_pdf = "output4withcutwithfullwidth.pdf"

##edit the string in the path to match the Naming pattern of the images within the folder:^^

create_pdf(image_paths, output_pdf)

