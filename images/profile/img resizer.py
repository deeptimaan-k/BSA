from PIL import ImageTk, Image

img=Image.open("C:\\Users\\KK JADAUN\\Desktop\\images png\\passout1.png")
size_image=(100,96)
img.thumbnail(size_image)
img.save('passout.png')
print("image resize done")
    
