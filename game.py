###########################################################################################################################
########################################################В О П Р О С Ы #####################################################
vopr_1 = 'Как заканчивается присказка: «Мы и сами с…»?'

var_ans_1 = ['с волосами', 'с усами', 'с часами', 'с долгами']

true_var_ans_1 = var_ans_1[1]

vopr_2 = 'Как в обиходе называют растение, которое часто дарят женщинам к празднику 8 марта?'

var_ans_2 = ['оливье', 'винегрет', 'мимоза', 'селёдка под шубой']

true_var_ans_2 = var_ans_2[2]

vopr_3 = 'С помощью чего пасссажиры часто попадают в самолет?'

var_ans_3 = ['рукава', 'воротника', 'лацкана', 'манжеты']

true_var_ans_3 = var_ans_3[0]

vopr_4 = 'Как называлась песня, которую исполнял Лев Лещенко?'

var_ans_4 = ['Воробьиная стая', 'Соловьиная роща', 'Ласточкино гнездо', 'Воронья слободка']

true_var_ans_4 = var_ans_4[1]

vopr_5 = 'Какой клетки нет на шахматной доске?'

var_ans_5 = ['h8', 'b7', 'k6', 'g5']

true_var_ans_5 = var_ans_5[2]

vopr_6 = 'Что не собирают?'

var_ans_6 = ['коллекцию', 'коррупцию', 'конструкцию', 'информацию']

true_var_ans_6 = var_ans_6[1]

vopr_7 = 'Какая бывает лопата?'

var_ans_7 = ['совковая', 'граблевая', 'тяпковая', 'мотыжная']

true_var_ans_7 = var_ans_7[0]

vopr_8 = 'Как называется фильм, снятый по мотивам «Повести временных лет»?'

var_ans_8 = ['Варяг', 'Кореец', 'Викинг', 'Чухонец']

true_var_ans_8 = var_ans_8[2]

vopr_9 = 'На что надевают брекеты?'

var_ans_9 = ['на пальцы', 'на уши', 'на волосы', 'на зубы']

true_var_ans_9 = var_ans_9[3]

vopr_10 = 'Кто такой ара?'

var_ans_10 = ['дельфин', 'медведь', 'попугай', 'крокодил']

true_var_ans_10 = var_ans_10[2]

vopr_11 = 'На каком курсе школы Хогвартс учился Гарри Поттер, когда раскрыл секрет Тайной комнаты?'

var_ans_11 = ['на первом', 'на втором', 'на третьем', 'на четвёртом']

true_var_ans_11 = var_ans_11[1]

vopr_12 = 'Какой обряд перед свадьбой назывался рукобитьем?'

var_ans_12 = ['выяснение, кто сильнее', 'праздник друзей жениха', 'одевание невесты', 'скрепление договора']

true_var_ans_12 = var_ans_12[3]

vopr_13 = 'Какой город группа «Кар-Мэн» называла «полным риска»?'

var_ans_13 = ['Нью-Йорк', 'Сан-Франциско', 'Лос-Анджелес', 'Детройт']

true_var_ans_13 = var_ans_13[1]

vopr_14 = 'Из чего плели лапти, которые называли «волосяники»?'

var_ans_14 = ['из травы', 'из полос кожи', 'из конского волоса', 'из льна']

true_var_ans_14 = var_ans_14[2]

vopr_15 = 'Кто автор строк «Ленин — жил, Ленин — жив, Ленин — будет жить»?'

var_ans_15 = ['Есенин', 'Маяковский', 'Сталин', 'Ленин']

true_var_ans_15 = var_ans_15[1]

vopr_16 = 'Какой вид физических упражений получил название по имени изобретателя?'

var_ans_16 = ['стретчинг', 'кроссфит', 'тай-бо', 'пилатес']

true_var_ans_16 = var_ans_16[3]

vopr_17 = 'Какой московский магазин некогда носил название Верхние торговые ряды?'

var_ans_17 = ['ЦУМ', 'Петровский пассаж', 'Гостинный Двор', 'ГУМ']

true_var_ans_17 = var_ans_17[3]

vopr_18 = 'Куда подевалась горошина, лежавшая под тюфяками и пуховиками принцессы, в сказке Андерсена?'

var_ans_18 = ['сварили в супе', 'скормили канарейке', 'отдали в кунсткамеру', 'вставили в корону']

true_var_ans_18 = var_ans_18[2]

###########################################################################################################################

print('''
Добро пожаловать в консольную игру "Кто хочет стать миллионером!"
Игра для двоих игроков!
Для начала нужно указать имена игроков.
''')

igrok_1 = str(input('Как зовут игрока под номером 1?: ')) # Первый игрок
igrok_2 = str(input('Как зовут игрока под номером 2?: ')) # Второй игрок
score_igrok_1 = 0 # Стартовые очки
score_igrok_2 = 0 # Стартовые очки

print('Итак начнём!')

print(vopr_1)
print('Варианты ответа: ')
print(var_ans_1)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))

###### Вопрос 1

if o_v1_i1 == true_var_ans_1:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_1:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_1:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_1:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))
		
#################################
###### Вопрос 2	
	
print(vopr_2)
print('Варианты ответа: ')
print(var_ans_2)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_2:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_2:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_2:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_2:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))	
#################################
###### Вопрос 3

print(vopr_3)
print('Варианты ответа: ')
print(var_ans_3)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_3:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_3:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_3:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_3:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))	
		
#################################
###### Вопрос 4

print(vopr_4)
print('Варианты ответа: ')
print(var_ans_4)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_4:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_4:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_4:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_4:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 5

print(vopr_5)
print('Варианты ответа: ')
print(var_ans_5)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_5:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_5:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_5:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_5:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		
		
#################################
###### Вопрос 6

print(vopr_6)
print('Варианты ответа: ')
print(var_ans_6)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_6:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_6:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_6:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_6:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 7

print(vopr_7)
print('Варианты ответа: ')
print(var_ans_7)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_7:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_7:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_7:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_7:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		
		
#################################
###### Вопрос 8

print(vopr_8)
print('Варианты ответа: ')
print(var_ans_8)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_8:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_8:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_8:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_8:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 9

print(vopr_9)
print('Варианты ответа: ')
print(var_ans_9)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_9:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_9:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_9:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_9:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		
		
#################################
###### Вопрос 10

print(vopr_10)
print('Варианты ответа: ')
print(var_ans_10)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_10:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_10:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_10:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_10:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 11

print(vopr_11)
print('Варианты ответа: ')
print(var_ans_11)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_11:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_11:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_11:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_11:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))	

#################################
###### Вопрос 12

print(vopr_12)
print('Варианты ответа: ')
print(var_ans_12)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_12:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_12:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_12:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_12:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))	

#################################
###### Вопрос 13

print(vopr_13)
print('Варианты ответа: ')
print(var_ans_13)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_13:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_13:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_13:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_13:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))	
		
#################################
###### Вопрос 14

print(vopr_14)
print('Варианты ответа: ')
print(var_ans_14)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_14:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_14:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_14:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_14:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))			
				
#################################
###### Вопрос 15

print(vopr_15)
print('Варианты ответа: ')
print(var_ans_15)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_15:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_15:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_15:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_15:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 16

print(vopr_16)
print('Варианты ответа: ')
print(var_ans_16)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_16:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_16:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_16:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_16:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		
		

#################################
###### Вопрос 17

print(vopr_17)
print('Варианты ответа: ')
print(var_ans_17)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_17:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_17:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_17:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_17:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

#################################
###### Вопрос 18

print(vopr_18)
print('Варианты ответа: ')
print(var_ans_18)
o_v1_i1 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_1))
o_v1_i2 = input('Игрок {} напишите Ваш ответ (буквами)'.format(igrok_2))
if o_v1_i1 == true_var_ans_18:
    score_igrok_1 += 1
    print('Ответ игрока {} засчитан'.format(igrok_1))
    if o_v1_i1 != true_var_ans_18:
        score_igrok_1 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_1))
if o_v1_i2 == true_var_ans_18:
    score_igrok_2 += 1
    print('Ответ игрока {} засчитан'.format(igrok_2))
    if o_v1_i2 != true_var_ans_18:
        score_igrok_2 -= 1
        print('Ответ игрока {} засчитан'.format(igrok_2))		

##Итоги

print('Игра закончена между {0} и {1}'.format(igrok_1, igrok_2))
if score_igrok_1 > score_igrok_2:
    print('{0} победил!'.format(igrok_1))
elif score_igrok_1 < score_igrok_2:
	print('{1} победил!'.format(igrok_2))
else:
	print('Увы ничья между игроками {0} и {1}'.format(igrok_1, igrok_2))
