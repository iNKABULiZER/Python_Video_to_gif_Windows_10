#pip install moviepy

from moviepy.editor import *

file_name="Tyson Fury vs. Deontay Wilder 2021.mp4"

clip = VideoFileClip(file_name) # Файл видео

#clip = clip.resize(newsize=(800,600)) #Изменить ширину и высоту

#clip =clip.resize(height=600) #Изменить по высоте 

#clip =clip.resize(width=800)	#Изменить по ширене 

clip =clip.resize(0.3) #Процентное изменение 

clip = clip.subclip(0, 4) #  C 0 по 4 секунду
   
final = clip.fx( vfx.speedx, 1) # Скорость 

final.write_gif(file_name+".gif", fps=5) # Записать в файл

