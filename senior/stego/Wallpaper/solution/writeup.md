# Wallpaper writeup
After reading conditions, we run `pngcheck` to check if image is really corrupted, we will notice that checksum is incorrect. It means that something in IHDR was changed. Looking at image, we are able to conclude that the vertical size was changed - because in conditions it's said that forest is higher than it looks.
Then change the size of an image (you should do it slowly - increase width step by step to not overdo it, you will see when you are close) and take the flag. The original size is 1920x1080 (you can find original image in Google Images)

Flag: **flag{r351z1ng_15_c00l}**
