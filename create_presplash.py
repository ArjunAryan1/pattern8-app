from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGBA', (1080, 1920), (0x1A, 0x1A, 0x2E, 255))
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype('arial.ttf', 96)
except:
    font = ImageFont.load_default()

text = 'Pattern 8'
bbox = draw.textbbox((0, 0), text, font=font)
x = (1080 - (bbox[2]-bbox[0])) // 2
draw.text((x, 500), text, font=font, fill=(0x00, 0xD4, 0xFF, 255))

try:
    font2 = ImageFont.truetype('arial.ttf', 48)
except:
    font2 = ImageFont.load_default()

text2 = "So / That's why + Result"
bbox2 = draw.textbbox((0, 0), text2, font=font2)
x2 = (1080 - (bbox2[2]-bbox2[0])) // 2
draw.text((x2, 630), text2, font=font2, fill=(0xFF, 0xFF, 0xFF, 255))

text3 = "Home & Family"
bbox3 = draw.textbbox((0, 0), text3, font=font2)
x3 = (1080 - (bbox3[2]-bbox3[0])) // 2
draw.text((x3, 720), text3, font=font2, fill=(0xB0, 0xB0, 0xB0, 255))

draw.ellipse([490, 1200, 590, 1300], outline=(0x00, 0xD4, 0xFF, 255), width=6)

img.save('presplash.png')
print('presplash.png created successfully')