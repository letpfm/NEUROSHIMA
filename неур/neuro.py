#надо будет сделать нормальный подсчет кол-ва оставшихся фишек, что бы был пересчет фишек по месту, а не по армии. Места для колод поместить в ячейки седки что бы можно было возвращать карту (если взял случайно) и перезапускать игру что бы все опять перемешивалось - хотя бы так.

import pickle, os, sys, random, datetime
import pygame as pg


armyDict = {'dancer': {'color': (241,134,0), 'hq': 3, 4: 10, 5: 8, 7: 7},
			'borgo': {'color': (76,172,229), 4: 1, 8: 2, 9: 3, 11: 4, 13: 6},
			'ddm': {'color': (91,97,95), 6: 1, 14: 2, 16: 4, 17: 5},
			'hegemony': {'color': (241,200,48), 8: 1, 11: 2, 15: 3, 16: 4, 17: 5},
			'mississippi': {'color': (224,202,117), 8: 1, 13: 2, 16: 3, 18: 4, 19: 1},
			'moloch': {'color': (203,34,41), 16: 1, 21: 2, 22: 4, 23: 5},
			'neojungle': {'color': (142,146,65), 8: 1, 13: 2, 16: 3, 18: 4, 19: 6},
			'newyork': {'color': (166,173,216), 10: 1, 20: 2, 21: 5},
			'outpost': {'color': (114,179,86), 9: 1,13: 2, 14: 5, 15: 6, 16: 7},
			'smart': {'color': (213,213,213), 6: 1, 12: 2, 15: 3, 17: 4},
			'steelpolice': {'color': (145,70,150), 9: 1, 15: 2, 18: 3, 19: 5},
			'uranopolis': {'color': (101,100,101), 13: 1, 17: 2, 19: 3, 21: 4},
			'vegas': {'color': (170,99,36), 4: 1, 11: 2, 15: 3, 16: 5},

			'sandrunners': {'color': (237,76,35), '01':'01', 'hq': 1, 5: 1, 13: 2, 16: 3, 17: 5},
			'deathbreath': {'color': (163,70,4), 7: 1, 11: 2, 15: 3, 16: 8},
			'mephisto': {'color': (185,15,15), 6: 1, 14: 2, 17: 3, 18: 4, 24: 1},
			'iron_gang': {'color': (213,215,2), 2: 1, 3: 2, 6: 3, 8: 4, 9: 5, 10: 9},
			'begemoths': {'color': (132, 198, 150),4: 1, 9: 2, 13: 3, 14: 4, 15: 5},
			'Thanatos':{'color': (246,113,0), 7: 1, 13: 2, 15: 3, 16: 4, 17: 6},
			'Clan Mercurius':{'color': (211, 124, 124), '01':'01', 15: 1, 17: 2, 18: 3, 20: 4, 21: 5, 22: 2, 23: 4},
			'The MIT':{'color': (222, 108, 52), 11: 1, 19: 2, 20: 3, 21: 5, 22: 9, 23: 5, 24: 2},

			'найм': {'hq': 0, 1: [[[-2.606896551724138, -0.4827586206896552], 0, 1, 0, True]],
			2: [[[-2.606896551724138, 0.5172413793103449], 0, 1, 0, True]],
			3: [[[2.6, -0.4827586206896552], 0, 1, 0, True]],
			4: [[[2.6, 0.5172413793103449], 0, 1, 0, True]],
			5: [[[0.8620689655172413, -0.4827586206896552], 0, 1, 0, True]],
			6: [[[-1.7379310344827585, 2.013793103448276], 0, 1, 0, True]],
			7: [[[1.7310344827586206, 2.013793103448276], 0, 1, 0, True]],
			8: [[[0.0, 0.013793103448275862], 0, 1, 0, True]],
			9: [[[-0.8689655172413793, -0.4827586206896552], 0, 1, 0, True]]},

			'Frontier Nexus': {'color':(220, 48, 165), 7: 1, 17: 2, 19: 4, 21: 2, 22: 9},
			'New Detroit': {'color': (145, 160, 180), 16: 1, 21: 2, 24: 3},
			'HI-TECH': {'color': (59, 138, 220), 7: 1, 11: 2, 13: 3, 14: 4, 16: 5, 17: 2, 18: 11},
			'Sand Runners': {'color': (117, 154, 68), 11: 1, 14: 2, 15: 3, 18: 5},
			'Silicon Valley': {'color': (114, 56, 168), 6: 1, 15: 2, 17: 3, 18: 5, 19: 4},
			'Bayou Boyz': {1: 1, 6: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 2, 27: 1},
			'firemen': {'color': (161, 245, 255), 5: 1, 13: 2, 14: 4, 16: 5}
			}

colorArmy = {}
for i in armyDict:
	if 'color' in armyDict[i]:
		colorArmy[i] = armyDict[i]['color']
lenArmyDict = len(armyDict)

game_folder = os.path.dirname(__file__)  # настройка папки ассетов
files = [nameFile for nameFile in os.listdir(game_folder) if nameFile[-4:] == '.txt']
img_folder = os.path.join(game_folder, 'img')
def pgil(a, b): return pg.image.load(os.path.join(a, b)).convert_alpha()
os.environ['SDL_VIDEO_CENTERED'] = '1'#что бы по центру было
sizeDict = [(640,360), (854, 480), (960, 540), (1000, 600), (1280,720), (1366, 768)]
MyClock = pg.time.Clock()
Backgrounds = {0: '0.jpg',5: "bg5.png", 6: 'bg6.png', 7: "bg7.png"}

size = sizeDict[0]
sumInH = 6
hexh = int(size[1]/(sumInH - 0.1))
pg.init()
Screen = pg.display.set_mode(size)
center = Screen.get_rect().center
def draw_text(surf, text, x, y, sizet, bg = 1, rgb = (255,255,255)):
	if bg:
		draw_text(surf, text, x-sizet//20, y-sizet//20, sizet, 0, [255 - i for i in rgb])
	if '\n' in text:
		indexN = text.index('\n')
		draw_text(surf, text[indexN+1:], x, y+sizet, sizet, bg, rgb)
		text = text[:indexN]
	font = pg.font.Font(pg.font.match_font('arial'), int(sizet))
	text_surface = font.render(text, True, rgb)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (int(x), int(y))
	surf.blit(text_surface, text_rect)

class Background(pg.sprite.Sprite):
	def __init__(self, number_bg):
		pg.sprite.Sprite.__init__(self)  #call Sprite initializer
		self.image = pg.Surface((50, 50))
		bgname = Backgrounds[number_bg]
		self.image = pgil(img_folder, bgname)
		self.image = pg.transform.scale(self.image, (int(size[1]*1.778), size[1]))
		self.rect = self.image.get_rect()
		self.rect.center = center

def choiceArmy(l, start = 0):
	i0 = 0
	tempColor = {}
	while 1:
		Screen.blit(BackGround.image, BackGround.rect)
		ll = len(l)	
		if ll > sumInH:
			yScroll = int(i0/(ll - sumInH)*(center[1]*2-hexh))
			draw_text(Screen, '[', center[0]*2, yScroll, hexh, 1, \
			random.choice([colorArmy[i] for i in colorArmy]))
		for i in range(i0, min(ll, i0 + sumInH)):
			if not l[i] in colorArmy and not l[i] in tempColor:
				tempColor[l[i]] = [random.randrange(256) for i in range(3)]
			clrarmy = colorArmy[l[i]] if l[i] in colorArmy else tempColor[l[i]]
			draw_text(Screen, l[i], center[0], (i - i0)*hexh, hexh, 1, clrarmy)

		pg.display.update()

		for event in pg.event.get():
			for i in range(i0, min(ll, i0 + sumInH)):
				if l[i] in tempColor:
					tempColor[l[i]] = [random.randrange(256) for i in range(3)]
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			elif event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 4:
					if i0: i0 -= 1
				elif event.button == 5:
					if i0 < ll - sumInH: i0 += 1
				else:
					o = i0 + pg.mouse.get_pos()[1]//hexh
					if o >= start:
						return o

pg.display.set_caption("Егор молодец")
BackGround = Background(0) #нашёл фон


size = sizeDict[5]
running = True #что бы цикл бегал
r = 2 #стартовое кол-во игроков
l = ['случайная армия']*6 #названия которые надо отобразить
armyDictList = [l[0]] + [i for i in armyDict if not i in ('sumInH', 'найм')] #возможные армии
map27 = 'не ' #будет ли поле особым
mercenaries = 'не '
nameFile = 0
while running:
	Screen.blit(BackGround.image, BackGround.rect)
	lenf = int(len(files) != 0)
	t = ['экран: '+str(size)] + ["ЗАГРУЗИТЬ"] * lenf +\
	['поле '+map27+'на 27 ячеек', 'игроков: '+str(r)]\
	+ [mercenaries + 'брать наёмников','НАЧАТЬ НОВУЮ ИГРУ']
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	y =	choiceArmy(t)

	if y == 0:
		n = sizeDict.index(size) + 1
		if n == len(sizeDict):
			n = 0
		size = sizeDict[n]

	elif y == 1 and lenf:
		i = 0
		nameFile = 0
		while not nameFile:
			fi = files[i][:-4].split(', ')
			fi += ['' for fi0 in range(sumInH - len(fi) - 3)]
			t = fi + [f'следующая {str(i+1)}/{str(len(files))}']*int(len(files)>1)+\
			['>Да, эта партия< ','-вернуться-','[УДАЛИТЬ]']
			chA = -1
			while chA < 0:
				chA = choiceArmy(t, len(fi)) - len(fi) + int(len(files)==1)
			if chA == 0:
				i += 1
				if i >= len(files):
					i = 0
			elif chA == 1:
				nameFile = files[i]
				with open(nameFile, 'rb') as f:
					armyDict = pickle.load(f)
				running = 0
			elif chA == 2:
				nameFile = 1
			elif chA == 3:
				if choiceArmy(['' for fi0 in range(sumInH//2-2)]+['НЕТ!!!','_'*sumInH*3, 'Да, X×УДАЛИТЬ×X']) < sumInH//2:
					pass
				else:
					os.remove(os.path.join(os.path.abspath(game_folder), files.pop(i)))
					break
	lenf = int(not lenf)
	if y == 2 - lenf:
		map27 = '' if len(map27) else 'не '
	elif y == 3 - lenf:
		while 1:
			chA = choiceArmy(['игроков: '+str(r)]+[l[i] for i in range(r)]+['[готово]'])
			if chA == 0: 
				r += 1
				if r > 6:
					r = 2
					for i in range(-4, 0):
						if l[i] != 'случайная армия':
							armyDictList += [l[i]]
							l[i] = 'случайная армия'
			elif chA == r+1:
				break
			else:
				i = chA - 1
				if l[i] != 'случайная армия':
					armyDictList += [l[i]]
				l[i] = armyDictList[choiceArmy(armyDictList)]
				if l[i] != 'случайная армия':
					armyDictList.remove(l[i])
	elif y == 4 - lenf:
		mercenaries = '' if len(mercenaries) else 'не '
	elif y == 5 - lenf:
		nameFile = datetime.datetime.today().strftime("%H'%M'%S %d'%m'%Y") + ', '
		running = False


if lenArmyDict == len(armyDict):
	armyDictList.remove('случайная армия')
	if r == 6:
		l[5], l[2], l[4] = l[2], l[4], l[5]
	elif r > 3:
		l[2], l[3] = l[3], l[2]

	ArmyList = l[:r]
	for i in range(len(ArmyList)):
		if not ArmyList[i] in armyDict:
			ArmyList[i] = armyDictList.pop(random.randrange(len(armyDictList)))

	if mercenaries == '':
		ArmyList += ['найм']

	if map27 == '':
		sumInH = 6
	else:
		sumInH = 7 if r > 4 else 5

else:
	sumInH = armyDict['sumInH']
	ArmyList = [i for i in armyDict if i != 'sumInH']

hexh = int(size[1]/(sumInH*0.99)) #нужная высота
Screen = pg.display.set_mode(size)
center = Screen.get_rect().center
hexw = int(hexh*2/3**0.5) #нужная ширина
countNoTake = []
hexx = int(hexw * 0.75)
sizePiece = hexh//3
class piece:
	hp = 1
	z = 0
	rot = 0
	notake = 0
	click = False
	radius = sizePiece/2
	side = 0
	def __init__(self, typehex, img, nameArmy, numberUnit):
		self.type = typehex
		self.nameArmy = nameArmy
		self.numberUnit = numberUnit
		pg.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов Sprite
		self.image = pg.Surface((100, 100))
		self.image = img
		self.rect = self.image.get_rect()
	def update(self, surface):
		if self.click:
			self.rect.center = [pg.mouse.get_pos()[i] + self.posmouse[i] for i in (0, 1)]
		surface.blit(self.image, self.rect)
	def remember(self, l):
		i = self
		i.rect.center = [int(l[0][n] * hexh + center[n]) for n in (0, 1)]

class hex(piece):
	notake = 1
	radius = hexh//2
	take = 0
	def __init__(self, typehex, ORIG_IMAGE, bg, startImage, nameArmy, numberUnit):
		self.type = typehex
		self.nameArmy = nameArmy
		self.numberUnit = numberUnit
		pg.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов Sprite
		self.image_orig = pg.Surface((100, 100))
		self.image_bg = bg
		self.image_orig = ORIG_IMAGE
		if startImage:
			self.image = startImage
		else:
			self.image = pg.transform.scale(self.image_orig, (int(hexw),int(hexh)))
		self.rect = self.image.get_rect() # прямоугольник вокруг image
		# pg.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
	def zoom(self):
		if self.z:
			self.rect.center = self.old_center
			self.rotate(0)
			self.z = 0
		else:
			s = size[1]
			self.old_center = self.rect.center
			self.rect.center = center
			self.rotate(0, int(s * 2/3**0.5), int(s))
			self.z = 1
			
	def update(self, surface):
		if self.click:
			self.rect.center = [pg.mouse.get_pos()[i] + self.posmouse[i] for i in (0, 1)]
			self.take = 1
		elif self.take:
			self.take = 0
			x1 = self.rect.center[0]
			y1 = self.rect.center[1]
			x = surface.get_rect().center[0]
			if not sumInH % 2:
				x += hexx / 2
			n = (x1 - x) / hexx #ячейка №
			if abs(n) % 1 >= 0.5: #если остаток перевешивает
				n += 0.5 - 1 * int(n < 0)
			n = int(n)
			o = y1
			if not n % 2: # четная ячейка от центра
				o -= hexh/2
			o %= hexh #расстояние до ближайшей ячейки

			if o >= hexh / 2: #если остаток перевешивает
				o -= hexh
			self.rect.center = (int(x + n * hexx), int(y1 - o))

		surface.blit(self.image, self.rect)
		if self.hp - 1 and not self.z and self.side:
			sizet = hexh//2
			x = self.rect.center[0]
			y = self.rect.center[1]-sizet//1.5
			t = str(self.hp) if self.hp else '#'
			draw_text(surface, t, x, y, sizet)

	def imagebg(self):
		i = self
		i.image_orig, i.image_bg = i.image_bg, i.image_orig
		i.rotate(0)
		i.side = not i.side

	def rotate(self, r=60, x = int(hexw), y = int(hexh)):
		self.rot = (self.rot + r) % 360
		old_center = self.rect.center
		self.image = pg.transform.rotate(self.image_orig, self.rot)
		if self.rot % 180:
			x = int(1183/946*x)
			y = int(1229/820*y)
		self.image = pg.transform.scale(self.image, (x, y))
		self.rect = self.image.get_rect()
		self.rect.center = old_center

	def remember(self, l):
		i = self
		if i.side != l[4]: i.imagebg()
		i.rect.center, i.notake, i.hp, i.rot = \
		[int(l[0][n]*hexh + center[n]) for n in (0, 1)], l[1], l[2], l[3]
		i.rotate(0)

def main(Surface, AllUnits):
	game_event_loop(AllUnits) #цикл игровых событий
	Surface.blit(BackGround.image, BackGround.rect)
	for i in AllUnits:
		if i.z:
			return i.update(Surface)

	updateList = []
	centerList = []
	for i in AllUnits:
		if not i.rect.center in centerList:
			centerList += i.rect.center
			updateList += [i]

	[i.update(Surface) for i in updateList[::-1]]

	sz = hexh//4

	for i in range(len(countNoTake)):
		if countNoTake[i] > 1:
			if 4 > i > 1: y = size[1]-hexh//2
			elif i > 3: y = center[1] - hexh//3
			else: y = -hexh//8
			draw_text(Surface, str(countNoTake[i]), abs(size[0]*(i%2) - sz), y, hexh//2)

def game_event_loop(a, nameFile = nameFile):
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			ek = event.key
			if ek == pg.K_f:
				if Screen.get_flags() == 0: pg.display.set_mode(size, flags=pg.FULLSCREEN)
				else: pg.display.set_mode(size)
			ku, kd =  pg.K_UP, pg.K_DOWN
			EventHp = ek in (ku, kd)
		else: EventHp = 0 

		if event.type == pg.MOUSEBUTTONDOWN or EventHp:
			for i in a:
				iPos = i.rect.center
				mPos = pg.mouse.get_pos()
				if ((mPos[0] - iPos[0])**2+(mPos[1] - iPos[1])**2)**0.5 < i.radius:
					#произошло ли событие мыши над гексом
					aInd = a.index(i)
					if i.type != 'маркер':
						if aInd != sumPiece:
							a.insert(sumPiece, a.pop(aInd))
					elif aInd:
						a.insert(0, a.pop(aInd))
					if i.notake:
						i.imagebg()
						i.notake = 0
					if EventHp:
						i.hp += (ek == ku) - (ek == kd)
					else:
						if event.button == 1:
							i.posmouse = [iPos[n] - mPos[n] for n in (0,1)]
							i.click = True
						if i.type != 'маркер':
							if event.button == 2: i.zoom()
							elif event.button == 3: i.imagebg()
							elif event.button == 4: i.rotate(-60)
							elif event.button == 5: i.rotate()
					break
		elif event.type == pg.MOUSEBUTTONUP:
			for i in a:
				i.click = False
				if i.z: i.zoom()
		elif event.type == pg.QUIT:
			D = {'sumInH': sumInH}
			if nameFile == 0:
				nameFile = ''
			for n in A: #прохожусь по всем армиям
				a = n[0].nameArmy
				if not '.txt' in nameFile:
					nameFile += a + ', '
				d = armyDict[a] #беру инструкцию создания этой армии

				for i in n: #пройтись по элементам в армии
					#сколько высот гексов от центра
					xy = [(i.rect.center[q] - center[q])/hexh for q in (0, 1)]
					if i.type != 'маркер':
						sInf = [xy, i.notake, i.hp, i.rot, i.side]
					else:
						sInf = [xy] #для маркера нужно только положение

					k = i.numberUnit

					if not k in d or isinstance(d[k],int): #если я ещё не трогал ключ
						d[k] = []

					d[k] += [sInf]

				D[a] = d
			if not '.txt' in nameFile:
				nameFile = nameFile[:-2]+'.txt'
			with open(nameFile, 'wb') as f:
				pickle.dump(D, f)

			pg.quit()
			sys.exit()

def addarmies(t, n = 0):
	n %= 6
	d = armyDict[t] #достал инструкцию
	bghq = d['01'] if '01' in d else 0 #задник базы
	hq = d['hq'] if 'hq' in d else 1 #количество баз
	f = os.path.join(img_folder, t) #папка армии
	A = [] #лист для армии
	bg = pgil(f, "0.png") #задник армии
	bgTransform = pg.transform.scale(bg, (int(hexw),int(hexh))) #=меняю размер для отображения=
	keyInt = sorted([i for i in d if type(i)==int]) #все ключи типа число
	
	instruction = {} #на тот случай если в библиотеке не числа
	if not isinstance(d[keyInt[-1]],int):
		for k in keyInt:
			instruction[k] = len(d[k])
	else:
		instruction = d
	a = 100 #проверка наличия маркеров

	for i in range(hq + 1, max(keyInt)+1): 

		if len(A)<34:

			img = pgil(f, f"{i}.png") #записал путь к картинке
			
			for x in range(len(keyInt)):
				
				if i <= keyInt[x]:
					A += [hex('не база и не маркер',bg, img, bgTransform, t, i) for q in range(instruction[keyInt[x]])]#Добавляю бойцов
					break
		else:
			a = i
			break

	if t != 'найм':
		random.shuffle(A) # перемешал

	if a != 100:

		for i in range(a, max(keyInt)+1):
			img = pg.transform.scale(pgil(f, f"{i}.png"), (sizePiece, sizePiece))

			for x in range(len(keyInt)):

				if i <= keyInt[x]:
					A += [piece('маркер', img, t, i) for n in range(instruction[keyInt[x]])]#Добавляю маркеры
					break

	if bghq:
		bg = pgil(f, f"{bghq}.png") #путь картинки задника базы
		bgTransform = pg.transform.scale(bg, (int(hexw),int(hexh))) #=меняю размер для отображения=

	for i in range(1, hq+1): #пройтись по базам
		A.insert(0,hex('база', bg, pgil(f, f"{i}.png"), bgTransform, t, i)) #инициализация объекта
		A[0].hp = {1: 20, 3: 10}[hq]#выдать здоровье по кол-ву баз

	if isinstance(d[keyInt[-1]],int):
		
		if t == 'найм':
			x = center[0]
			y = center[1]
			for i in A:
				i.rect.center = (x, y)#Определяю место
		else:
			x = hexw//3
			y = hexh//2
			x1 = sizePiece
			y1 = 0
			if n:
				if n % 2:
					x = size[0] - x
					x1 *= -1
				if 4 > n > 1:
					y = size[1] - y
					y1 = 0
				elif n > 3:
					y = center[1]
					x1 = 0
					y1 = -sizePiece
			for i in range(35):
				A[i].rect.center = (x, y)#Определяю место
			if not y1:
				y = sizePiece//2 + (size[1] - sizePiece) * int(y > center[1])
				x += x1
			if not x1:
				x = + sizePiece//2 + (size[0] - sizePiece) * int(x > center[0])
				y += y1
			for i in range(35,len(A)):
				n = A[i].numberUnit - a
				A[i].rect.center = (x+x1*n, y+y1*n)#Определяю место
	else:
		for i in range(len(A)):
			A[i].remember(d[A[i].numberUnit].pop(0))
	return A

BackGround = Background(sumInH)
A = [addarmies(ArmyList[i], i) for i in range(len(ArmyList))]
armies = []
sumPiece = 0
for i in A:
	armies += i
	if len(i)>35:
		sumPiece += len(i[35:])
		armies = i[35:] + armies
while 1:
	countNoTake = [sum([i.notake for i in n]) for n in A]
	main(Screen, armies)
	pg.display.update()
	MyClock.tick(60)