from flask import Flask, render_template
app = Flask(__name__)

currentSong = """  Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.

Em    B7         G          D          Em B7 G D Em
Возвращаемся с работы мы, ребята, от сохи.
     B7         G           D          Em  B7 G D G
А кругом читают Дао, что творится, мужики!
        B7           Em          D            Em B7 G D Em
А мы вдыхаем вольный ветер, наши мысли так легки.
    B7            G            D          Em B7 G D
А пока мы не в Шанхае, нам все это не с руки.

Em    B7         G          D          Em B7 G D Em
А мне все пофиг - я с покоса - уберите кирпичи.
     B7         G           D          Em  B7 G D G
А на хрена уральский парень занимается Тай-Чи?
        B7           Em          D            Em B7 G D Em
А мы вдыхаем вольный ветер, наши руки так крепки.
    B7            G            D          Em B7 G D
А ломать без толку доски - удавиться от тоски.

Em    B7         G          D          Em B7 G D Em
Освежись аэрозолью, это чудо - финский пар.
     B7         G           D          Em  B7 G D G
А дома кафельная ванна и искусственный загар.
        B7           Em          D      Em B7 G D Em
А мы вдыхаем вольный ветер у вонючей у реки.
    B7            G            D     Em B7 G D
Натуральные березы, ой, да в бане веники.

   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.

Em    B7         G          D          Em B7 G D Em
Все мы грешны, и не надо перед образом стоять.
     B7         G           D          Em  B7 G D G
С нас потом никто не спросит, да и что с нас можно взять?
        B7           Em          D         Em B7 G D Em
А мы вдыхаем вольный ветер, наши души так легки.
    B7            G            D          Em B7 G D
Отпускай же, мать-природа, наши смертные грехи.

      G      B7           Em  D G
     А мы вдыхаем вольный ветер.
             B7           Em  D G
     А мы вдыхаем вольный ветер.
             B7           Em  D G
     А мы вдыхаем вольный ветер.
             B7           Em  D
     А мы вдыхаем вольный ветер.

   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
   Em       B7        G        D
   Ум да ли дури дали ум да ли дури да ли.
"""

@app.route('/')
def index():
    return render_template('guest.html', currentSong=currentSong)

@app.route('/list')
def admin_full_list():
    return render_template('full_list.html')

@app.route('/list/<author>')
def admin_author_list():
    return render_template('author_list.html')

@app.route('/list/<author>/<song>')
def admin_song():
    return render_template('song.html')
