from PIL import ImageTk, Image

img=Image.open("C:\\Users\\KK JADAUN\\Desktop\\images png\\books.png")
size_image=(90,90)
img.thumbnail(size_image)
img.save('books.png')
print("image resize done")
    
