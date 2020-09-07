from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask import url_for, current_app
from PIL import Image
import os
import secrets
from wtforms import SubmitField
from PIL import Image
import random


app = Flask(__name__)


app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz'

class UploadForm(FlaskForm):
	picture = FileField('Upload Image',validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Submit')


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
	output_size = (500,500)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn



@app.route('/',methods=['GET','POST'])
def home():
	generate()
	image_file = "static/merged_face.png"
	return render_template('home.html', title='Upload', image_file=image_file)
	# picture_file = url_for('static',filename='profile_pics/'+picture_file)
	# return render_template('home.html', title='Upload', form=form)

def generate():
	face = Image.open("Assets/JW line/j1.png")
	face_size = face.size

	# # print(face_size)

	n = random.randint(1, 3)
	path = "Assets/Eyes/e" + str(n) + ".png"
	# path = "Assets/Eyes/Eye_Almond.png"
	eyes = Image.open(path)
	# resizing
	basewidth = 800
	wpercent = (basewidth / float(eyes.size[0]))
	hsize = int((float(eyes.size[1]) * float(wpercent)))
	eyes = eyes.resize((basewidth, hsize), Image.ANTIALIAS)
	face.paste(eyes, (205, 790), eyes)

	n = random.randint(1, 4)
	path = "Assets/Nose/n" + str(n) + ".png"
	# path = "Assets/Nose/n1.png"
	nose = Image.open(path)
	# resizing
	basewidth = 340
	wpercent = (basewidth / float(nose.size[0]))
	hsize = int((float(nose.size[1]) * float(wpercent)))
	nose = nose.resize((basewidth, hsize), Image.ANTIALIAS)
	face.paste(nose, (435, 845), nose)
	#
	# n = random.randint(1,5)
	# # path = "CartoonImages/m"+str(n)+".png"
	# path = "Assets/Lips/Lips_01.png"
	# mouth = Image.open(path)
	# #resizing
	# basewidth = 200
	# wpercent = (basewidth/float(mouth.size[0]))
	# hsize = int((float(mouth.size[1])*float(wpercent)))
	# mouth = mouth.resize((basewidth,hsize), Image.ANTIALIAS)
	# #coordinates
	# face.paste(mouth,(535,800), mouth)
	#
	# # mouth = Image.open("CartoonImages/m2.png")
	# # #resizing
	# # basewidth = 200
	# # wpercent = (basewidth/float(mouth.size[0]))
	# # hsize = int((float(mouth.size[1])*float(wpercent)))
	# # mouth = mouth.resize((basewidth,hsize), Image.ANTIALIAS)
	# # #coordinates
	# # face.paste(mouth,(535,800), mouth)

	beard = random.randint(1, 2)
	if (beard == 1):
		path = "Assets/Beard/Beard_01.png"
		beard = Image.open(path)
		# resizing
		basewidth = 980
		wpercent = (basewidth / float(beard.size[0]))
		hsize = int((float(beard.size[1]) * float(wpercent)))
		beard = beard.resize((basewidth, hsize), Image.ANTIALIAS)
		# coordinates
		face.paste(beard, (125, 1050), beard)
	# path = "CartoonImages/b"+str(n)+".png"

	# #
	n = random.randint(1, 4)
	path = "Assets/Hairstyle/h" + str(n) + ".png"
	# path = "Assets/Hairstyle/h1.png"
	hair = Image.open(path)
	# resizing
	basewidth = 1250
	wpercent = (basewidth / float(hair.size[0]))
	hsize = int((float(hair.size[1]) * float(wpercent)))
	hair = hair.resize((basewidth, hsize), Image.ANTIALIAS)
	# coordinates
	face.paste(hair, (-20, -50), hair)
	#
	# #eyebrows
	n = random.randint(1, 9)
	path = "Assets/Eyebrow/Eyebrow_0" + str(n) + ".png"
	# path = "Assets/Eyebrow/Eyebrow_01.png"
	eyebrows = Image.open(path)
	# resizing
	basewidth = 730
	wpercent = (basewidth / float(eyebrows.size[0]))
	hsize = int((float(eyebrows.size[1]) * float(wpercent)))
	eyebrows = eyebrows.resize((basewidth, hsize), Image.ANTIALIAS)
	# coordinates
	face.paste(eyebrows, (240, 820), eyebrows)

	n = random.randint(1, 2)
	path = "Assets/Lips/l" + str(n) + ".png"
	# path = "Assets/Lips/l1.png"
	lips = Image.open(path)
	# resizing
	basewidth = 410
	wpercent = (basewidth / float(lips.size[0]))
	hsize = int((float(lips.size[1]) * float(wpercent)))
	lips = lips.resize((basewidth, hsize), Image.ANTIALIAS)
	# coordinates
	face.paste(lips, (415, 1220), lips)

	# face.show()

	face.save("static/merged_face.png", "PNG")




	# return render_template('home.html',title='Upload',image_file=picture_file, form=form)


if __name__ == '__main__':
	app.run(debug=True)





