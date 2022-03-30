import os
# pip install pillow
from PIL import Image
from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
    filename = pic_upload.filename                    # "mypicture.jpg"
    ext_type = filename.split('.')[-1]                # "jpg"
    storage_filename = str(username) + '.' + ext_type # "username.jpg"
    filepath = os.path.join(current_app.root_path, 'static\profile_pics', storage_filename)

    # Play Around with this size.
    output_size = (200,200)

    # Open the picture and save it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size) # squeeze the image
    pic.save(filepath)

    return storage_filename