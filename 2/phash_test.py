from PIL import Image,ImageFile
import imagehash,os
from glob import glob
#サイズの大きな画像をスキップしない
ImageFile.LOAD_TRUNCATED_IMAGES = True

hash_a = imagehash.phash(Image.open('./a_resize_cut.png'))
hash_b = imagehash.phash(Image.open('./b_resize_cut.png'))
print('hash_a=')
print(hash_a)
print('hash_b=')
print(hash_b)

