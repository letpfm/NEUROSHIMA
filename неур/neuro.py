import os,sys, random
import pygame as pg
armyDict = {'sandrunners': {'bghq':'01', 'hq': 1,
			5: 1, 13: 2, 16: 3, 17: 5},
			'dancer': {'hq': 3,
			4: 10, 5: 8, 7: 7},
			'borgo': {4: 1, 8: 2, 9: 3, 11: 4, 13: 6},
			'ddm': {6: 1, 14: 2, 16: 4, 17: 5},
			'deathbreath': {7: 1, 11: 2, 15: 3, 16: 8},
			'hegemony': {8: 1, 11: 2, 15: 3, 16: 4, 17: 5},
			'mephisto': {6: 1, 14: 2, 17: 3, 18: 4},
			'iron_gang': {2: 1, 3: 2, 6: 3, 8: 4, 9: 5, 10: 9},#, 11: 1},
			'mississippi': {8: 1, 13: 2, 16: 3, 18: 4},
			'moloch': {16: 1, 21: 2, 22: 4, 23: 5},
			'neojungle': {8: 1, 13: 2, 16: 3, 18: 4},
			'newyork': {10: 1, 20: 2, 21: 5},
			'outpost': {9: 1,13: 2, 14: 5, 15: 6, 16: 7},
			'begemoths': {4: 1, 9: 2, 13: 3, 14: 4, 15: 5},
			'smart': {6: 1, 12: 2, 15: 3, 17: 4},
			'steelpolice': {9: 1, 15: 2, 18: 3, 19: 5},
			'uranopolis': {13: 1, 17: 2, 19: 3, 21: 4},
			'vegas': {4: 1, 11: 2, 15: 3, 16: 5},
			'Thanatos':{7: 1, 13: 2, 15: 3, 16: 4, 17: 6},
			

			#\/найм должен быть в конце
			'найм':{4: 1, 6: 0, 7: 1}
			}

game_folder = os.path.dirname(__file__)  # настройка папки ассетов
img_folder = os.path.join(game_folder, 'img')
def pgil(a, b): return pg.image.load(os.path.join(a, b)).convert_alpha()
os.environ['SDL_VIDEO_CENTERED'] = '1'#что бы по центру было
sizeDict = [(640,360), (854, 480), (960, 540), (1000, 600), (1280,720), (1366, 768)]
MyClock = pg.time.Clock()
Backgrounds = {0: '0.jpg',5: "bg5.png", 6: 'bg6.png', 7: "bg7.png"}
colorArmy = {'sandrunners': (237,76,35),
			'dancer': (241,134,0),
			'borgo': (76,172,229),
			'ddm': (91,97,95),
			'deathbreath': (163,70,4),
			'hegemony': (241,200,48),
			'mephisto': (185,15,15),
			'iron_gang': (213,215,2),
			'mississippi': (224,202,117),
			'moloch': (203,34,41),
			'neojungle': (142,146,65),
			'newyork': (166,173,216),
			'outpost': (114,179,86),
			'begemoths': (132, 198, 150),
			'smart': (213,213,213),
			'steelpolice': (145,70,150),
			'uranopolis': (101,100,101),
			'vegas': (170,99,36),
			'Thanatos': (246,113,0),
			}

hexMore = 1.05 #что бы гексы чуть заходили на друг друга на поле
size = sizeDict[0]
sumInH = 5
hexh = int(size[1]/9.9)
pg.init()
Screen = pg.display.set_mode(size)
center = Screen.get_rect().center
def draw_text(surf, text, x, y, sizet, bg = 1, rgb = (255,255,255)):
	if bg:
		draw_text(surf, '■', x, y - sizet * 0.9, int(sizet * 2.2), 0, (0,0,0))
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

def choiceArmy():
	lenArmyD = len(armyDictList)
	szChArmy = center[0] * 2 / (lenArmyD)
	while 1:
		Screen.blit(BackGround.image, BackGround.rect)
		for i in range(lenArmyD): 
			clrarmy = colorArmy[armyDictList[i]] if armyDictList[i] in colorArmy else (255,255,255)
			draw_text(Screen, armyDictList[i], center[0]*(0.5+i%2), (i-i%2)*szChArmy/2, szChArmy, 0, clrarmy)
			if not i%2: draw_text(Screen, '_'*25+'|'+'_'*25, center[0], i*szChArmy/2, szChArmy, 0)
		pg.display.update()
		for event in pg.event.get():
			if event.type == pg.QUIT:  # check for closing window
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				y = int(pg.mouse.get_pos()[1]/szChArmy)*2 + pg.mouse.get_pos()[0]//center[0]
				return y if y < lenArmyD else lenArmyD-1

BackGround = Background(0)
pg.display.set_caption("Егор молодец")
running = True
r = 2
l = ['случайная армия']*6
armyDictList = [i for i in armyDict]
size = sizeDict[4]
map27 = 'не '
while running:
	Screen.blit(BackGround.image, BackGround.rect)
	t = ['разрешение экрана: '+str(size), \
	'поле '+map27+'на 27 ячеек'\
	,'Кол-во игроков на новую игру: '+str(r)] + ['игрок №'+str(i+1)+': '+l[i] for i in range(r)]\
	+ ['' for i in range(6-r)] + ['Начать игру NEUROSHIMA']
	for i in range(len(t)):
		if i in (2,8):
			draw_text(Screen, '_'*23, center[0], i*hexh, hexh, 0, (50, 200, 50))
		if 2 < i < 9 and t[i] != '' and l[i-3] != 'случайная армия':
			draw_text(Screen, 'Выбрать\nслучайную\nармию', hexh, (i+0.1)*hexh, hexh/4, 1, (200,100,100))
			clrarmy = colorArmy[l[i-3]] if l[i-3] in colorArmy else (255,255,255)
			draw_text(Screen, t[i], center[0], i*hexh, hexh, 0, clrarmy)
		else:
			draw_text(Screen, t[i], center[0], i*hexh, hexh, 0)
	pg.display.update()
	MyClock.tick(60)

	for event in pg.event.get():
		if event.type == pg.QUIT:  # check for closing window
			pg.quit()
			sys.exit()
		if event.type == pg.MOUSEBUTTONDOWN:
			mPos = pg.mouse.get_pos()[1]
			if mPos < hexh:
				n = sizeDict.index(size) + 1
				if n == len(sizeDict):
					n = 0
				size = sizeDict[n]
			elif mPos < hexh*2:
				map27 = '' if map27 == 'не ' else 'не '
			elif mPos < hexh*3:
				r += 1
				if r > 6:
					r = 2
					for i in range(-4, 0):
						if l[i] != 'случайная армия':
							armyDictList += [l[i]]
							l[i] = 'случайная армия'
			elif mPos < hexh*(3+r):
				i = int(mPos/hexh-3)
				if l[i] != 'случайная армия':
					armyDictList += [l[i]]
					if pg.mouse.get_pos()[0] <= hexh*2:
						l[i] = 'случайная армия'
					else:
						l[i] = armyDictList.pop(choiceArmy())
				else:
					l[i] = armyDictList.pop(choiceArmy())

			elif hexh*9 < mPos:
				running = False

if r == 6: l[5],l[2],l[4] = l[2],l[4],l[5]
elif r > 3: l[2], l[3] = l[3], l[2]
ArmyList = l[:r]
for i in range(len(ArmyList)):
	if not ArmyList[i] in armyDict:
		ArmyList[i] = armyDictList.pop(random.randrange(len(armyDictList)-1))
if map27 == '':
	sumInH = 6
else:
	sumInH = 7 if r > 4 else 5
hexh = int(size[1]/(sumInH*0.99)) #нужная высота
Screen = pg.display.set_mode(size)
center = Screen.get_rect().center
HEXhINw = 946/821 #ширина оригинала/высота  оригинала
hexw = int(hexh*HEXhINw) #нужная ширина
countNoTake = []
hexx = hexh/HEXhINw #hexh/hexx = HEXhINw высота гекса выступает шириной вписанного в него 6угольника высота которого подходит для расстояния меж ячейками по ширене поля

class hex:
	hp = 1
	rot = 0
	notake = 1
	z = 0
	click = False
	radius = hexh//2
	take = 0
	def __init__(self, ORIG_IMAGE, bg, startImage = 0, nameArmy = 0, numberUnit = 1):
		self.nameArmy = nameArmy
		self.numberUnit = numberUnit
		pg.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов Sprite
		self.image_orig = pg.Surface((100, 100))
		self.image_bg = bg
		self.image_orig = ORIG_IMAGE
		if startImage:
			self.image = startImage
		else:
			self.image = pg.transform.scale(self.image_orig, (int(hexw*hexMore),int(hexh*hexMore)))
		self.rect = self.image.get_rect() # прямоугольник вокруг image
		# pg.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
	def zoom(self):
		if self.z:
			self.rect.center = self.old_center
			self.rotate(0)
			self.z = 0
		else:
			s = size[1]*1.2
			self.old_center = self.rect.center
			self.rect.center = center
			self.rotate(0, int(s * HEXhINw), int(s))
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
			y = surface.get_rect().center[1]
			r = ((x1-x)**2+(y1-y)**2)**0.5
			if r < y:
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

		if self.hp - 1 and not self.z:
			sizet = hexh//4
			x = self.rect.center[0]
			y = self.rect.center[1]-sizet//1.5
			t = str(self.hp) if self.hp else '#'
			draw_text(surface, t, x, y, sizet)
			# draw_text(surface, str(self.hp), int(x + (y**2 - (y1 - y)**2)**0.5), y1 - hexh//4)

	def imagebg(self):
		i = self
		i.image_orig, i.image_bg = i.image_bg, i.image_orig
		i.rotate(0)

	def rotate(self, r=60, w = int(hexw*hexMore), h = int(hexh*hexMore)):
		self.rot = (self.rot + r) % 360
		old_center = self.rect.center
		self.image = pg.transform.rotate(self.image_orig, self.rot)

		if self.rot in (0, 180):
			sz = (w, h)
		else:
			s160 = h/160
			sz = (int(230*s160), int(239*s160))
		self.image = pg.transform.scale(self.image, sz)
		self.rect = self.image.get_rect()
		self.rect.center = old_center

def main(Surface, AllUnits):
	game_event_loop(AllUnits) #цикл игровых событий
	Surface.blit(BackGround.image, BackGround.rect)
	[i.update(Surface) for i in AllUnits[::-1] if not i.notake or i in AllUnits[-len([i for i in countNoTake if i]):]]
	sz = hexh//4
	for i in range(len(countNoTake)):
		if countNoTake[i] > 1:
			if 4 > i > 1: y = size[1]-hexh//2
			elif i > 3: y = center[1] - hexh//3
			else: y = -hexh//8
			draw_text(Surface, str(countNoTake[i]), abs(size[0]*(i%2) - sz), y, hexh//2)

def game_event_loop(a):
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
			tops_of_stacks = []
			if countNoTake:
				for i in range(len(A)):
					tops_of_stacks += [A[i][-countNoTake[i]]]
			for i in a[:len(a)-sum(countNoTake)]+tops_of_stacks:
				iPos = i.rect.center
				mPos = pg.mouse.get_pos()
				if ((mPos[0] - iPos[0])**2+(mPos[1] - iPos[1])**2)**0.5 < i.radius:
					#произошло ли событие мыши над гексом
					aInd = a.index(i)
					if aInd: a.insert(0, a.pop(aInd))
					if i.notake:
						i.imagebg()
						i.notake = 0
					if EventHp:
						i.hp += (ek == ku) - (ek == kd)
						break
					else:
						if event.button == 1:
							i.posmouse = [iPos[n] - mPos[n] for n in (0,1)]
							i.click = True
						elif event.button == 2: i.zoom()
						elif event.button == 3: i.imagebg()
						elif event.button == 4: i.rotate(-60)
						else: i.rotate()
						break
		elif event.type == pg.MOUSEBUTTONUP:
			for i in a:
				i.click = False
				if i.z: i.zoom()
		elif event.type == pg.QUIT:
			# for n in A: #на тот случай если займусь сохранениями
				# print(n[0].nameArmy)
				# print('notake:')
				# units_no_take = sorted([i.numberUnit for i in n if i.notake])
				# print(units_no_take)
				# d = {}
				# for q in units_no_take:
				# 	if not q in d:
				# 		d[q] = units_no_take.count(q)
				# print(d,'\ntake:')
				# units_take = sorted([i.numberUnit for i in n if not i.notake])
				# print(units_take)
				# d = {}
				# for q in units_take:
				# 	if not q in d:
				# 		d[q] = units_take.count(q)
				# print(d)
				# d = {}
				# lastQ = 0
				# how_long_Q = 0
				# for q in range(max(armyDict[n[0].nameArmy]["how"]),0,-1):
				# 	if not q in d:
				# 		how_long_Q += 1
				# 		Uc = units_no_take.count(q)
				# 		if lastQ != Uc or not q+how_long_Q in d: 
				# 			d[q] = Uc
				# 			lastQ = Uc
				# 			how_long_Q = 0
				# print(d)
			pg.quit()
			sys.exit()

def addarmies(t, n = 0):
	d = armyDict[t] #достал инструкцию
	bghq = d['bghq'] if 'bghq' in d else 0 #задник базы
	hq = d['hq'] if 'hq' in d else 1 #количество баз
	f = os.path.join(img_folder, t) #папка армии
	A = [] #лист для армии
	bg = pgil(f, "0.png") #задник армии
	bgTransform = pg.transform.scale(bg, (int(hexw*hexMore),int(hexh*hexMore)))
	for i in range(hq + 1, max([i for i in d if type(i)==int])+1):
		img = pgil(f, f"{i}.png")
		for x in [i for i in d if type(i)==int]:
			if i <= x:
				a = d[x]
				break
		A += [hex(bg, img, bgTransform, t, i) for n in range(a)]#Добавляю бойцов
	if t != 'найм':
		random.shuffle(A) # перемешал
	if bghq:
		bg = pgil(f, f"{bghq}.png") #достал картинку задника базы
		bgTransform = 0
	for i in range(1, hq+1): #пройтись по базам
		A += [hex(bg,pgil(f, f"{i}.png"), bgTransform, t)] #инициализация объекта
		if t != 'найм':
			A[-1].hp = {1: 20, 3: 10}[hq]#выдать здоровье по кол-ву баз

	if t == 'найм':
		x = center[0]
		y = center[1]
	else:
		x = hexw//3
		y = hexh//2
		if n:
			if n % 2:
				x = size[0] - x
			if 4 > n > 1:
				y = size[1] - y
			elif n > 3:
				y = center[1]

	for i in A:
		i.rect.center = (x, y)#Определяю место

	return A[::-1]

BackGround = Background(sumInH)
A = [addarmies(ArmyList[i], i) for i in range(len(ArmyList))]
armies = []
n = []
for i in A:
	armies += i[:-1]
	n += [i[-1]]
armies += n
while 1:
	countNoTake = [sum([i.notake for i in n]) for n in A]
	main(Screen, armies)
	pg.display.update()
	MyClock.tick(60)