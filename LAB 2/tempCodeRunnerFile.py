     # get the current pixel value
            current_pixel_value2 = im_rot_pixels[row, col,zed]
            # Manipulating your pixel values
            # for example: print pixel values that are greater than 200
            if current_pixel_value2 > 240:
                print("Max Pixel Value is: ", current_pixel_value2)