@echo off
ffmpeg -y -r 60 -i "out/image/%%d.png" -c:v libx264 -vf fps=60 -pix_fmt yuv420p "out/out.mp4"