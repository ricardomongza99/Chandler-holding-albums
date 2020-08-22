from PIL import Image, ImageDraw
import json

# PROPERTIES
ALBUM_SIZE = (250, 250)
ALBUM_POS = (53, 198)
ALBUM_ANGLE = -5

with open('albums.json') as json_file:
    data = json.load(json_file)
    for album in data['album']:
        print(album['name'])

        # load images
        im_chandler: Image.Image = Image.open('resources/chandler.png')
        im_album: Image.Image = Image.open('album_covers/' + album['image'])
        im_final: Image.Image = Image.new('RGBA', im_chandler.size)

        # rotate album image and paste it to the final
        im_album = im_album.resize(ALBUM_SIZE, Image.ANTIALIAS)
        im_album2 = im_album.convert('RGBA')
        rot = im_album2.rotate(ALBUM_ANGLE, expand=1).resize(ALBUM_SIZE)
        im_final.paste(rot, ALBUM_POS, rot)

        # Adds chandler on top with mask
        r, g, b, a = im_chandler.split()
        im_chandler = Image.merge("RGB", (r, g, b))
        mask = Image.merge('L', (a,))
        im_final.paste(im_chandler, (0, 0), mask)

        im_final.save('chandler_albums/Chandler Holding ' + album['name'] + '.png', 'PNG')



"""
# load images
im_chandler: Image.Image = Image.open('resources/chandler.png')
im_album: Image.Image = Image.open('resources/sgtpepper.jpg')
im_final: Image.Image = Image.new('RGBA', im_chandler.size)

# rotate album image and paste it to the final
im_album = im_album.resize(ALBUM_SIZE, Image.ANTIALIAS)
im_album2 = im_album.convert('RGBA')
rot = im_album2.rotate(ALBUM_ANGLE, expand=1).resize(ALBUM_SIZE)
im_final.paste(rot, ALBUM_POS, rot)

# Adds chandler on top with mask
r, g, b, a = im_chandler.split()
im_chandler = Image.merge("RGB", (r, g, b))
mask = Image.merge('L', (a,))
im_final.paste(im_chandler, (0, 0), mask)

im_final.show()

"""
