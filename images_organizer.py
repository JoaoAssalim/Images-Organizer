import os
import shutil

search_dir = input('Enter a directory: ')
#create the directororys
jpg_images_dir = f'{search_dir}\\jpg_images'
jpeg_images_dir = f'{search_dir}\\tjpeg_images'
gif_dir = f'{search_dir}\\gif'
png_images_dir = f'{search_dir}\\png_images'

#if don't exists directorys with there names above, it will create
if not os.path.isdir(jpg_images_dir):
    os.mkdir(jpg_images_dir)

if not os.path.isdir(jpeg_images_dir):
    os.mkdir(jpeg_images_dir)

if not os.path.isdir(gif_dir):
    os.mkdir(gif_dir)

if not os.path.isdir(png_images_dir):
    os.mkdir(png_images_dir)

#Move images(.jpg, .png, .jpeg, .gif) to determinated folder
for root, dirs, files in os.walk(search_dir):

    for file in files:
        move_file = os.path.join(root, file)
        if '.jpg' in file:
            move_jpg_images = os.path.join(jpg_images_dir, file)
            shutil.move(move_file, move_jpg_images)
            print(f'{file} moved to jpg_images')

        if '.png' in file:
            move_png_images = os.path.join(png_images_dir, file)
            shutil.move(move_file, move_png_images)
            print(f'{file} moved to png_images')

        if '.jpeg' in file:
            move_jpeg_iamges = os.path.join(jpeg_images_dir, file)
            shutil.move(move_file, move_jpeg_iamges)
            print(f'{file} moved to jpeg_images')

        if '.gif' in file:
            move_gif = os.path.join(gif_dir, file)
            shutil.move(move_file, move_gif)
            print(f'{file} moved to gif')

