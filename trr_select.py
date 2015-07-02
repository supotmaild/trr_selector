'''TRR Eyeglasses Selector'''
'''or Sunglasses Selector'''
'''Version 1.0.1 2 Jul 2015'''
'''use with Python 2.7'''
'''with PIL'''
'''and SimpleCV'''
'''Complie with PY2EXE'''
import winsound,sys,threading,time
global winsound,sys,threading,time
from SimpleCV import Camera
import Tkinter as tk
from Tkinter import PhotoImage, Tk, Canvas, Scrollbar, Text, StringVar
import ttk
from PIL import ImageTk, Image
global tk
global canvas,quad,nine,sixteen,clean
global label4002,price,hut,hut_num,cam_num
global plu,plu_pic,plu_tkpi,plu_button,plu_take_a_picture
global nok_air,steve_job,task,nok_air_task,state
# Global Current State 4,9,16 
state=0
cam_num=0
plu=[]
plu_pic=[]
plu_button=[]
plu_tkpi=[]
for i in range(16):
	plu.append('')
	plu_pic.append(False)
	plu_tkpi.append('')
for i in range(36):
	plu_button.append('')	
hut = []
hut_num = 0
hut.append('การที่เธอมีพระพุทธรูป ก็ไม่ได้หมายความว่ามีพระพุทธองค์ประทับอยู่บนรถ พระพุทธรูปมิใช่พระพุทธองค์ ไม่ว่าพระพุทธรูปนั้นจะทำด้วยพลาสติกหรือหยกก็ตาม เพียงแค่มีใครสักคนหนึ่งในรถหายใจและมองในวิถีแห่งสติ พระพุทธองค์ที่แท้จริงก็จะปรากฎขึ้น')
hut.append('ไม่มีใครมอบความไม่กลัวให้แก่เธอได้ ต่อให้พระพุทธเจ้าประทับอยู่ด้วยในขณะนี้ข้างๆเธอก็ตาม เธอต้องฝึกปฏิบัติและรับรู้ด้วยตัวของเธอเอง ถ้าเธอปฏิบัติเจริญสติจนเป็นนิสัย เมื่อความยากลำบากเกิดขึ้น เธอจะรู้ได้ด้วยตัวของเธอเองว่าต้องทำเช่นไร')
hut.append('เมื่อเธอมองเข้าไปในดอกไม้นี้ เธอเห็นว่าจักรวาลทั้งหมดรวมกันอยู่ในดอกไม้ และเธอจะสัมผัสกับจักรวาลในดอกไม้นี้ได้ ดอกไม้เต็มไปด้วยจักรวาล เต็มไปด้วยทุกสิ่งทุกอย่าง มีความว่างจากสิ่งเดียวเท่านั้น คือว่างจากตัวตนแยกออกมาเป็นอิสระ ')
hut.append('อีก ๓๐๐ ปีข้างหน้าเธอก็จะกลายเป็นผงถ่าน คนที่เธอรักก็จะกลายเป็นผงฝุ่น เมื่อเธอสัมผัสกับความเป็นอนิจจังเช่นนี้ เธอก็จะเกิดปัญญาและรู้ว่า เป็นสิ่งที่โง่เขลามากที่เราทำตัวของเราให้เป็นทุกข์ต่อกัน')
hut.append('เมื่อสมองของเราเต็มไปด้วยความคิด เราจะออกจากความคิด ตัดความคิดเหล่านั้นได้อย่างไร พระอาจารย์ ติช นัท ฮันห์')
hut.append('เธอมีเวลาเพื่อจะใช้ชีวิต เธอมีเวลาสำหรับความรัก มีเวลาดูแลคนที่เธอรัก มีเวลาสำหรับดูแลตัวเอง หรือไม่ พระอาจารย์ ติช นัท ฮันห์')
hut.append('อำนาจแรกคืออำนาจที่จะตัดทิ้ง เป็นอำนาจของการปลดปล่อย อำนาจที่สองคืออำนาจที่จะเข้าใจ อำนาจนี้จะมอบเสรีภาพให้กับเรา อำนาจที่สามคืออำนาจที่จะรัก เธอมีความสามารถที่จะรักฝ่ายตรงข้าม รักคนผู้นั้น รักผู้ที่กำลังเป็นทุกข์')
hut.append('ก่อนหน้านี้เราคิดว่า มีเพียงเราที่เป็นเหยื่อและเป็นทุกข์ แต่ขณะนี้เธอรู้แล้วว่าอีกฝ่ายก็เป็นตกเป็นเหยื่อและเต็มไปด้วยความทุกข์เช่นกัน เราต่างตกเป็นเหยื่อของความกลัว ความโกรธ ความระแวง ด้วยกัน')
hut.append('(ต่อ) เมื่อเธอเห็นความทุกข์ ความเศร้าโศกสิ้นหวัง ของอีกฝ่าย ความโกรธในหัวใจของเธอจะหายไป เธอจะเริ่มมองเขาด้วยสายตาของความกรุณา เพราะเธอเห็นความทุกข์นั้น เธอเข้าใจความทุกข์นั้นแล้ว')
hut.append('หนทางและจุดหมายมิใช่สองสิ่งที่แตกต่างกัน ไม่มีเส้นทางไหน พาเรากลับบ้านได้ เพราะ บ้านคือหนทาง เมื่อเราเริ่มก้าวย่างไปบนเส้นทางนี้แล้ว เราก็ได้กลับบ้านในทันที นี่คือการฝึกปฎิบัติในวิถีของหมู่บ้านพลัม')
hut.append('ครูต้องเรียนรู้ที่จะมองอย่างลึกซึ้ง เด็กๆ เหล่านั้นอาจมาจากครอบครัวที่ทุกข์ยาก ถ้าในครอบครัวของเขามีคุณพ่อ-คุณแม่ที่มีความสุข เด็กๆ ก็คงไม่ได้เป็นแบบนี้ เขาคือเหยื่อของความทุกข์')
hut.append('(ต่อ) เมื่อเราเห็นเช่นนี้เราจะไม่โกรธเด็กที่ดื้อรั้นและอารมณ์รุนแรง เรารู้ว่าเขาคือเหยื่อของสิ่งแวดล้อมที่รุนแรง แล้วความกรุณาก็จะบังเกิดขึ้น')
hut.append('การปฏิบัติภาวนาคือการมองอย่างลึกซึ้ง ทำให้เราเห็นความเชื่อมโยงกัน เธอก็อยู่ในตัวฉัน ฉันก็อยู่ในตัวเธอ ความสุขของเขาก็คือความสุขของฉัน ความทุกข์ของเขาก็คือความทุกข์ของฉันด้วย')
hut.append('---ถ้าเรามองเห็นความสัมพันธ์เชื่อมโยงอย่างลึกซึ้งนี้ เราต้องหยุดการกระทำที่จะก่อทุกข์ต่อกัน นี่คือปัญญารู้แจ้งที่จะถอดถอนการแบ่งแยก ความโกรธ เกลียด เราจะเข้ามาหากันและรวมกันเป็นหนึ่งเดียว')
hut.append('ครูเฮนรี่เป็นครูสอนคณิตศาสตร์ที่ดีที่สุดของโรงเรียน เขาเป็นคนดีแต่ก็เป็นคนโกรธง่ายและขี้โมโหมาก เวลาโกรธก็ไม่ค่อยอ่อนโยนต่อลูกศิษย์ ')
hut.append('(ต่อ) เวลาที่โกรธมากๆก็จะดุด่าลูกศิษย์ด้วยถ้อยคำรุนแรง บางครั้งครูก็ขว้างชอล์คใส่นักเรียน  หลังจากครูคนนี้มาฝึกปฏิบัติที่หมู่บ้านพลัม เขาเปลี่ยนไปอย่างสิ้นเชิง')
hut.append('เมื่อมองดอกบัวเราเห็นโคลนตม โคลนตมคือองค์ประกอบที่ไม่ใช่ดอกบัว แต่เป็นองค์ประกอบที่สำคัญยิ่งที่จะสร้างดอกบัวขึ้นมา ความสุขก็เหมือนดอกบัว')
hut.append('(ต่อ) หากไม่มีองค์ประกอบที่เป็นความทุกข์ เธอก็ไม่อาจสร้างความสุขขึ้นมาเมื่อเราเรียนรู้ความทุกข์อย่างดีพอ เธอจะสามารถสร้างความสุขขึ้นมา ใช้โคลนตมนั้นปลูกดอกบัวขึ้นมา')
hut.append('หากเธอหยิบกระดาษสักแผ่นเขียนเงื่อนไขต่างๆ ที่ทำให้เธอมีความสุข และ เงื่อนไขเหล่านี้เธอมีอยู่แล้ว บางทีกระดาษเพียง ๒ หน้าก็อาจจะไม่พอ เรามีเงื่อนไขแห่งความสุขมากมาย ไม่ต้องวิ่งไปข้างหน้าเพื่อจะตามหาความสุขมาเพิ่มอีก')
hut.append('ในสังคมของเราทุกวันนี้ ผู้คนไม่สนใจที่จะฝึกเพื่อลับมาสัมผัสความทุกข์ภายในตนอีกแล้ว เพราะทุกคนกลัวที่จะพบกับความทุกข์ อยากจะวิ่งหนีตัวเอง เราวิ่งหนีด้วยการบริโภคมากขึ้น เพื่อจะลืมหรือหนีความทุกข์เหล่านั้น')
hut.append('(ต่อ) นั่นจึงเป็นเหตุว่าทำไมเราจึงไม่รู้จักกับความทุกข์ของเราเสียที ไม่เข้าใจความทุกข์ของพ่อแม่ บรรพบุรุษ และพี่น้องประชาชน')
hut.append('เมื่อฉันใช้คำว่า หนุ่มสาว ฉันหมายถึงเธอทั้งหลาย ผู้มีดวงตาเป็นประกาย ผู้ซึ่งสามารถฟังและเรียนรู้ได้ลึกซึ้ง ผู้ซึ่งสวมใส่จีวรอันประณีตและเรียบง่าย ผู้ซึ่งยิ้มได้เสมอ')
hut.append('น้องมือซ้าย กับ พี่มือขวา บันทึกจากปาฐกถาธรรม "สู่ศานติสมานฉันท์ : ความรักอันไม่แบ่งแยก"')
hut.append('ความเจ็บปวดที่เกิดขึ้นแม้เพียง¬ส่วนหนึ่งของมวลมนุษยชาติแต่ก็เป็นความเจ็บปวดของมนุษยชาติทั้งหมด เผ่าพันธุ์มนุษย์โลกกับดาวเคราะห์โลกดวงนี้เป็นดั่งร่างกายเดียวกัน อะไรก็ตามที่เกิดขึ้นกับส่วนหนึ่งส่วนใดของร่างกายก็ย่อมส่งผลต่อร่างกายทั้งหมดด้วย')
price=4
win = tk.Tk()
win.title('TRR Eyeglasses Selector 1.0.1')
img = PhotoImage(file='select.gif')
win.tk.call('wm', 'iconphoto', win._w, img)
frame1 = tk.Frame(
	master = win,
	width = 640,
	height = 550,
	bg = '#8B4513'
)
frame3 = tk.Frame(master = win, width=350, height=50, bg='#ffffff')
frame4 = tk.Frame(master = win, width=150, height=50, bg='#000000')
frame1.pack(fill='both', expand='yes')

canvas = Canvas(frame1, width=640, height=450)
canvas.place(in_=frame1,x=0,y=0,width=640,height=450)
frame3.place(in_=frame1, x=5, y=460, width=427, height=75)
rsstext=tk.Text(frame3)
rsstext.insert(END,'ข่าวสาร')
rsstext.pack()

localtime = time.asctime( time.localtime(time.time()) )
frame4.place(in_=frame1, x=435, y=460, width=205, height=56)
label4001 = tk.Label(frame4, text=format(price,'01'),font="Arial 28 bold",fg='#ffffff', bg='#000000')
label4001.place(x=170,y=0)
label4002 = tk.Label(frame4, text=localtime,font="Arial 6",fg='#ffffff', bg='#000000')
label4002.place(x=5,y=40)

def plu_take_a_picture(i):
	global plu_button,image_CV,plu_tkpi,cam_num,plu_pic,nok_air
	win.after_cancel(nok_air)
	if i>=20:
		plu_pic[i-20]=True
		cam = Camera(cam_num)
		img = cam.getImage()
		img.save('tmp_picture.jpg')
		image_CV = Image.open('tmp_picture.jpg')
		resized = image_CV.resize((320,225),Image.ANTIALIAS)
		plu_tkpi[i-20] = ImageTk.PhotoImage(resized)
		plu_button[i].configure(width = 160, height = 112, image=plu_tkpi[i-20])				
	elif i>=10:
		plu_pic[i-10]=True
		cam = Camera(cam_num)
		img = cam.getImage()
		img.save('tmp_picture.jpg')
		image_CV = Image.open('tmp_picture.jpg')
		resized = image_CV.resize((320,225),Image.ANTIALIAS)
		plu_tkpi[i-10] = ImageTk.PhotoImage(resized)
		plu_button[i].configure(width = 213, height = 150, image=plu_tkpi[i-10])		
	else:
		plu_pic[i] = True
		cam = Camera(cam_num)
		img = cam.getImage()
		img.save('tmp_picture.jpg')
		image_CV = Image.open('tmp_picture.jpg')
		resized = image_CV.resize((320,225),Image.ANTIALIAS)
		plu_tkpi[i] = ImageTk.PhotoImage(resized)
		plu_button[i].configure(width = 320, height = 225, image=plu_tkpi[i])
	nok_air = win.after(1000,nok_air_task)

def clean():
	global plu_pic,plu_button,canvas
	if state==4:
		for i in range(4):
			plu_button[i].place_forget()
	elif state==9:
		for i in range(9):
			plu_button[10+i].place_forget()
	elif state==16:
		for i in range(16):
			plu_button[20+i].place_forget()

def quad():
	global state,plu_pic,plu_button,canvas,label4001,frame4
	if state!=0: clean()
	state=4
	label4001.place_forget()
	label4001 = tk.Label(frame4, text=format(state,'01'),font="Arial 28 bold",fg='#ffffff', bg='#000000')
	label4001.place(x=170,y=0)
	if plu_pic[0]:
		plu_button[0] = tk.Button(canvas, width = 320, height = 225, image=plu_tkpi[0], command = lambda:plu_take_a_picture(0))
		canvas.create_window(0,0, anchor='nw', window=plu_button[0])
	else:
		plu_button[0] = tk.Button(canvas, width = 45, height = 15, text ="(1)", command = lambda:plu_take_a_picture(0))
		canvas.create_window(0,0, anchor='nw', window=plu_button[0])
	if plu_pic[1]:
		plu_button[1] = tk.Button(canvas, width = 320, height = 225, image=plu_tkpi[1], command = lambda:plu_take_a_picture(1))
		canvas.create_window(0,225, anchor='nw', window=plu_button[1])
	else:
		plu_button[1] = tk.Button(canvas, width = 45, height = 15, text ="(2)", command = lambda:plu_take_a_picture(1))
		canvas.create_window(0,225, anchor='nw', window=plu_button[1])
	if plu_pic[2]:
		plu_button[2] = tk.Button(canvas, width = 320, height = 225, image=plu_tkpi[2], command = lambda:plu_take_a_picture(2))
		canvas.create_window(320,0, anchor='nw', window=plu_button[2])
	else:
		plu_button[2] = tk.Button(canvas, width = 45, height = 15, text ="(3)", command = lambda:plu_take_a_picture(2))
		canvas.create_window(320,0, anchor='nw', window=plu_button[2])
	if plu_pic[3]:
		plu_button[3] = tk.Button(canvas, width = 320, height = 225, image=plu_tkpi[3], command = lambda:plu_take_a_picture(3))
		canvas.create_window(320,225, anchor='nw', window=plu_button[3])
	else:
		plu_button[3] = tk.Button(canvas, width = 45, height = 15, text ="(4)", command = lambda:plu_take_a_picture(3))
		canvas.create_window(320,225, anchor='nw', window=plu_button[3])

def nine():
	global state,plu_pic,plu_button,canvas,label4001,frame4
	if state!=0: clean()
	state=9
	label4001.place_forget()
	label4001 = tk.Label(frame4, text=format(state,'01'),font="Arial 28 bold",fg='#ffffff', bg='#000000')
	label4001.place(x=170,y=0)
	if plu_pic[0]:
		plu_button[10] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[0], command = lambda:plu_take_a_picture(10))
		canvas.create_window(0,0, anchor='nw', window=plu_button[10])
	else:
		plu_button[10] = tk.Button(canvas, width = 30, height = 10, text ="(1)", command = lambda:plu_take_a_picture(10))
		canvas.create_window(0,0, anchor='nw', window=plu_button[10])
	if plu_pic[1]:
		plu_button[11] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[1], command = lambda:plu_take_a_picture(11))
		canvas.create_window(0,150, anchor='nw', window=plu_button[11])
	else:
		plu_button[11] = tk.Button(canvas, width = 30, height = 10, text ="(2)", command = lambda:plu_take_a_picture(11))
		canvas.create_window(0,150, anchor='nw', window=plu_button[11])
	if plu_pic[2]:
		plu_button[12] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[2], command = lambda:plu_take_a_picture(12))
		canvas.create_window(0,300, anchor='nw', window=plu_button[12])
	else:
		plu_button[12] = tk.Button(canvas, width = 30, height = 10, text ="(3)", command = lambda:plu_take_a_picture(12))
		canvas.create_window(0,300, anchor='nw', window=plu_button[12])
	if plu_pic[3]:
		plu_button[13] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[3], command = lambda:plu_take_a_picture(13))
		canvas.create_window(214,0, anchor='nw', window=plu_button[13])
	else:
		plu_button[13] = tk.Button(canvas, width = 30, height = 10, text ="(4)", command = lambda:plu_take_a_picture(13))
		canvas.create_window(214,0, anchor='nw', window=plu_button[13])
	if plu_pic[4]:
		plu_button[14] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[4], command = lambda:plu_take_a_picture(14))
		canvas.create_window(214,150, anchor='nw', window=plu_button[14])
	else:
		plu_button[14] = tk.Button(canvas, width = 30, height = 10, text ="(5)", command = lambda:plu_take_a_picture(14))
		canvas.create_window(214,150, anchor='nw', window=plu_button[14])
	if plu_pic[5]:
		plu_button[15] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[5], command = lambda:plu_take_a_picture(15))
		canvas.create_window(214,300, anchor='nw', window=plu_button[15])
	else:
		plu_button[15] = tk.Button(canvas, width = 30, height = 10, text ="(6)", command = lambda:plu_take_a_picture(15))
		canvas.create_window(214,300, anchor='nw', window=plu_button[15])
	if plu_pic[6]:
		plu_button[16] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[6], command = lambda:plu_take_a_picture(16))
		canvas.create_window(428,0, anchor='nw', window=plu_button[16])
	else:
		plu_button[16] = tk.Button(canvas, width = 30, height = 10, text ="(7)", command = lambda:plu_take_a_picture(16))
		canvas.create_window(428,0, anchor='nw', window=plu_button[16])
	if plu_pic[7]:
		plu_button[17] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[7], command = lambda:plu_take_a_picture(17))
		canvas.create_window(428,150, anchor='nw', window=plu_button[17])
	else:
		plu_button[17] = tk.Button(canvas, width = 30, height = 10, text ="(8)", command = lambda:plu_take_a_picture(17))
		canvas.create_window(428,150, anchor='nw', window=plu_button[17])
	if plu_pic[8]:
		plu_button[18] = tk.Button(canvas, width = 213, height = 150, image=plu_tkpi[8], command = lambda:plu_take_a_picture(18))
		canvas.create_window(428,300, anchor='nw', window=plu_button[18])
	else:
		plu_button[18] = tk.Button(canvas, width = 30, height = 10, text ="(9)", command = lambda:plu_take_a_picture(18))
		canvas.create_window(428,300, anchor='nw', window=plu_button[18])

def sixteen():
	global state,plu_pic,plu_button,canvas,label4001,frame4
	if state!=0: clean()
	state=16
	label4001.place_forget()
	label4001 = tk.Label(frame4, text=format(state,'02'),font="Arial 28 bold",fg='#ffffff', bg='#000000')
	label4001.place(x=150,y=0)
	if plu_pic[0]:
		plu_button[20] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[0], command = lambda:plu_take_a_picture(20))
		canvas.create_window(0,0, anchor='nw', window=plu_button[20])
	else:
		plu_button[20] = tk.Button(canvas, width = 22, height = 7, text ="(1)", command = lambda:plu_take_a_picture(20))
		canvas.create_window(0,0, anchor='nw', window=plu_button[20])
	if plu_pic[1]:
		plu_button[21] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[1], command = lambda:plu_take_a_picture(21))
		canvas.create_window(0,113, anchor='nw', window=plu_button[21])
	else:
		plu_button[21] = tk.Button(canvas, width = 22, height = 7, text ="(2)", command = lambda:plu_take_a_picture(21))
		canvas.create_window(0,113, anchor='nw', window=plu_button[21])
	if plu_pic[2]:
		plu_button[22] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[2], command = lambda:plu_take_a_picture(22))
		canvas.create_window(0,226, anchor='nw', window=plu_button[22])
	else:
		plu_button[22] = tk.Button(canvas, width = 22, height = 7, text ="(3)", command = lambda:plu_take_a_picture(22))
		canvas.create_window(0,226, anchor='nw', window=plu_button[22])
	if plu_pic[3]:
		plu_button[23] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[3], command = lambda:plu_take_a_picture(23))
		canvas.create_window(0,339, anchor='nw', window=plu_button[23])
	else:
		plu_button[23] = tk.Button(canvas, width = 22, height = 7, text ="(4)", command = lambda:plu_take_a_picture(23))
		canvas.create_window(0,339, anchor='nw', window=plu_button[23])
	if plu_pic[4]:
		plu_button[24] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[4], command = lambda:plu_take_a_picture(24))
		canvas.create_window(160,0, anchor='nw', window=plu_button[24])
	else:
		plu_button[24] = tk.Button(canvas, width = 22, height = 7, text ="(5)", command = lambda:plu_take_a_picture(24))
		canvas.create_window(160,0, anchor='nw', window=plu_button[24])
	if plu_pic[5]:
		plu_button[25] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[5], command = lambda:plu_take_a_picture(25))
		canvas.create_window(160,113, anchor='nw', window=plu_button[25])
	else:
		plu_button[25] = tk.Button(canvas, width = 22, height = 7, text ="(6)", command = lambda:plu_take_a_picture(25))
		canvas.create_window(160,113, anchor='nw', window=plu_button[25])
	if plu_pic[6]:
		plu_button[26] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[6], command = lambda:plu_take_a_picture(26))
		canvas.create_window(160,226, anchor='nw', window=plu_button[26])
	else:
		plu_button[26] = tk.Button(canvas, width = 22, height = 7, text ="(7)", command = lambda:plu_take_a_picture(26))
		canvas.create_window(160,226, anchor='nw', window=plu_button[26])
	if plu_pic[7]:
		plu_button[27] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[7], command = lambda:plu_take_a_picture(27))
		canvas.create_window(160,339, anchor='nw', window=plu_button[27])
	else:
		plu_button[27] = tk.Button(canvas, width = 22, height = 7, text ="(8)", command = lambda:plu_take_a_picture(27))
		canvas.create_window(160,339, anchor='nw', window=plu_button[27])
	if plu_pic[8]:
		plu_button[28] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[8], command = lambda:plu_take_a_picture(28))
		canvas.create_window(320,0, anchor='nw', window=plu_button[28])
	else:
		plu_button[28] = tk.Button(canvas, width = 22, height = 7, text ="(9)", command = lambda:plu_take_a_picture(28))
		canvas.create_window(320,0, anchor='nw', window=plu_button[28])
	if plu_pic[9]:
		plu_button[29] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[9], command = lambda:plu_take_a_picture(29))
		canvas.create_window(320,113, anchor='nw', window=plu_button[29])
	else:
		plu_button[29] = tk.Button(canvas, width = 22, height = 7, text ="(10)", command = lambda:plu_take_a_picture(29))
		canvas.create_window(320,113, anchor='nw', window=plu_button[29])
	if plu_pic[10]:
		plu_button[30] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[10], command = lambda:plu_take_a_picture(30))
		canvas.create_window(320,226, anchor='nw', window=plu_button[30])
	else:
		plu_button[30] = tk.Button(canvas, width = 22, height = 7, text ="(11)", command = lambda:plu_take_a_picture(30))
		canvas.create_window(320,226, anchor='nw', window=plu_button[30])
	if plu_pic[11]:
		plu_button[31] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[11], command = lambda:plu_take_a_picture(31))
		canvas.create_window(320,339, anchor='nw', window=plu_button[31])
	else:
		plu_button[31] = tk.Button(canvas, width = 22, height = 7, text ="(12)", command = lambda:plu_take_a_picture(31))
		canvas.create_window(320,339, anchor='nw', window=plu_button[31])
	if plu_pic[12]:
		plu_button[32] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[12], command = lambda:plu_take_a_picture(32))
		canvas.create_window(480,0, anchor='nw', window=plu_button[32])
	else:
		plu_button[32] = tk.Button(canvas, width = 22, height = 7, text ="(13)", command = lambda:plu_take_a_picture(32))
		canvas.create_window(480,0, anchor='nw', window=plu_button[32])
	if plu_pic[13]:
		plu_button[33] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[13], command = lambda:plu_take_a_picture(33))
		canvas.create_window(480,113, anchor='nw', window=plu_button[33])
	else:
		plu_button[33] = tk.Button(canvas, width = 22, height = 7, text ="(14)", command = lambda:plu_take_a_picture(33))
		canvas.create_window(480,113, anchor='nw', window=plu_button[33])
	if plu_pic[14]:
		plu_button[34] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[14], command = lambda:plu_take_a_picture(34))
		canvas.create_window(480,226, anchor='nw', window=plu_button[34])
	else:
		plu_button[34] = tk.Button(canvas, width = 22, height = 7, text ="(15)", command = lambda:plu_take_a_picture(34))
		canvas.create_window(480,226, anchor='nw', window=plu_button[34])
	if plu_pic[15]:
		plu_button[35] = tk.Button(canvas, width = 160, height = 112, image=plu_tkpi[15], command = lambda:plu_take_a_picture(35))
		canvas.create_window(480,339, anchor='nw', window=plu_button[35])
	else:
		plu_button[35] = tk.Button(canvas, width = 22, height = 7, text ="(16)", command = lambda:plu_take_a_picture(35))
		canvas.create_window(480,339, anchor='nw', window=plu_button[35])

quad()

def nok_air_task():
	global state,plu_tkpi,plu_button,plu_pic,nok_air
	plu_pic[0] = True
	cam = Camera(cam_num)
	img = cam.getImage()
	img.save('tmp_picture.jpg')
	image_CV = Image.open('tmp_picture.jpg')
	resized = image_CV.resize((320,225),Image.ANTIALIAS)
	plu_tkpi[0] = ImageTk.PhotoImage(resized)
	if state==4:
		plu_button[0].configure(width = 320, height = 225, image=plu_tkpi[0])						
	elif state==9:
		plu_button[10].configure(width = 213, height = 150, image=plu_tkpi[0])				
	elif state==16:
		plu_button[20].configure(width = 160, height = 112, image=plu_tkpi[0])				
	nok_air = win.after(500,nok_air_task)

global mindfulness,mindfull,supermindfull,small_bell,big_bell,onFull
threads = []

def small_bell():
	global onFull
	winsound.PlaySound('sbell2.wav',winsound.SND_FILENAME)
	time.sleep(5)
	# stackoverflow Q 510348 answer by Evan Fosmark 4 Feb 2009
	onFull=False
def big_bell():
	global onFull
	winsound.PlaySound('bell2.wav',winsound.SND_FILENAME)
	time.sleep(5)
	# stackoverflow Q 510348 answer by Evan Fosmark 4 Feb 2009
	onFull=False
def mindfull():
	global threads
	t = threading.Thread(target=small_bell)
	threads.append(t)
	t.start()
def supermindfull():
	global threads
	t = threading.Thread(target=big_bell)
	threads.append(t)
	t.start()

def task():
	global END,hut_num,hut,rsstext,win,steve_job,task,load_ready,onFull,label4002
	localtime = time.asctime( time.localtime(time.time()) )
	label4002.config(text=localtime)
	if (localtime[14:16]=='15' or localtime[14:16]=='30' or localtime[14:16]=='45') and (int(localtime[17:19])<=30) and not(onFull):
		onFull=True
		mindfulness = win.after(500,mindfull)
	elif (localtime[14:16]=='00')  and (int(localtime[17:19])<=30) and not(onFull):
		onFull=True
		mindfulness = win.after(500,supermindfull)
	rsstext.delete('1.0',END)
	if onFull:
		rsstext.insert(END,'ฟังสิ ฟังสิ เสียงระฆังอันประเสริฐ นำฉันกลับมาสู่บ้านที่แท้จริง\nหายใจเข้า ฉันรู้ว่า ฉันหายใจเข้า\nหายใจออก ฉันรู้ว่า ฉันหายใจออก')
	else:
		rsstext.insert(END,hut[hut_num])
		hut_num=hut_num+1
		if hut_num>=len(hut):
			hut_num=0
	steve_job = win.after(25000,task)


def on_closing():
	global win,steve_job,nok_air,mindfulness
	try: win.after_cancel(steve_job)
	except: pass
	try: win.after_cancel(nok_air)
	except: pass
	try: win.after_cancel(mindfullness)
	except: pass
	win.destroy()


button91 = tk.Button(frame1, width = 2, height = 2, text ="4", command = quad)
button91.place(x=610, y=520)
button92 = tk.Button(frame1, width = 2, height = 2, text ="9", command = nine)
button92.place(x=580, y=520)
button93 = tk.Button(frame1, width = 2, height = 2, text ="16", command = sixteen)
button93.place(x=550, y=520)

develop0 = tk.Label(frame1, text='Eyeglasses Selector', fg = '#ffffff', bg = '#8B4513')
develop0.place(x=435, y=518)
nok_air = win.after(1000,nok_air_task)
steve_job = win.after(5000,task)
onFull = True
mindfulness = win.after(500,supermindfull)
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
