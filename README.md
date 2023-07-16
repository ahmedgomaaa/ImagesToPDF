# Image PDF Creator

![Project Image](images/project-image.jpg)

## Description

The Image PDF Creator is a Python script that allows you to quickly generate a PDF file from a collection of images. It arranges the images in a specified directory into multiple pages, with each page containing three images. The script uses the Python Imaging Library (Pillow) for image processing and ReportLab for PDF generation.

## Features

- Automatically arranges images into a multi-page PDF document
- Maintains aspect ratio of images while fitting them within page dimensions
- Customizable margins and image placement
- Easy-to-use Python script

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)
- ReportLab library (`pip install reportlab`)

## Usage

1. Place your images in a single directory.
2. Update the `image_directory` variable in the script with the path to your image directory.
3. Run the script using Python: `python image_pdf_creator.py`.
4. The script will generate a PDF file with the arranged images.

## Examples

Here are a few examples of how the images will be arranged in the generated PDF:

![PDF Example 1](images/pdf-example-1.jpg)
![PDF Example 2](images/pdf-example-2.jpg)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

