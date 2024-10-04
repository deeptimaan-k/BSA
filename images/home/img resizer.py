from PIL import ImageTk, Image

img=Image.open("C:\\Users\\KK JADAUN\\Desktop\\images png\\sport.png")
size_image=(120,120)
img.thumbnail(size_image)
img.save('sport.png')
print("image resize done")
    
