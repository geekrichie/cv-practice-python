from PIL import Image
pil_im = Image.open(r"..\img\sample.jpg")
#缩略图
#pil_im.thumbnail((128,128))
# box = (100,100,400,400)
# region = pil_im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region,box)
# out = pil_im.resize((128,128))
# out = pil_im.rotate(45)
# out.show()
pil_im.show()