from flask import Flask, render_template, request, send_file
import urllib
import wikipedia
import htmlfunc
import searchecosia
import change_string

####################
####################
# Creating Website #

app = Flask(__name__)

# End of creating website #
###########################
###########################

#####################
#####################
# Website Templates #

class study_template:
    # This is the home page.
    @app.route('/')
    def home():
        return htmlfunc.read("home.html")

    # This is the site with all the articles in them.
    @app.route('/wiki')
    def wiki():
        args = request.args
        lang = args.get('lang')
        eng = args.get('search-eng')
        rawResult = args.get('result')
        result = change_string.change_string(rawResult, "<", '&#60;')
        if result is None:
            result = ''
        web_result_html = f'<h1>{result}</h1>'
        wikipedia.set_lang(lang)
        try:
            try:
                Content = wikipedia.page(result, auto_suggest=False).content.split('\n')
                for i in Content:
                    if i[0:1] == '=' and i[-2:]:
                        web_result_html += f'<h2 style="font-family: didot; font-weight: 500;">{i.split()[1]}</h2>'
                    else:
                        web_result_html += f'<p style="font-family: Arial;">{change_string.change_string(i, "<", "&#60;")}</p>'
            except wikipedia.DisambiguationError as e:
                for i in e.options:
                    web_result_html += f"<fieldset><h3 class='links'><a href='/wiki?{urllib.parse.urlencode({'result': i})}&lang={lang}&search-eng={eng}'>{change_string.change_string(i, '<', '$#60;')}</a></h3></fieldset>\n"
        except:
            web_result_html += '<h1>No Article Found</h1>'
        return htmlfunc.study_html_formater(web_result_html, result, lang=lang, eng=eng, photo_q=urllib.parse.urlencode({'q': rawResult}))

    # This is the search engine.
    @app.route('/search', methods=['GET'])
    def search():
        web_search_html = ''
        args = request.args
        lang = args.get('lang')
        eng = args.get('search-eng')
        rawSearch = args.get('search')
        Search = change_string.change_string(rawSearch, "'", '&#39;')
        if eng == 'wikipedia':
            wikipedia.set_lang(lang)
            try:
                page_list = wikipedia.search(rawSearch)
                if page_list:
                    for i in page_list:
                        i = change_string.change_string(i, "'", '&#39;')
                        web_search_html += f"<fieldset><h3 class='links'><a href='/wiki?{urllib.parse.urlencode({'result': i})}&lang={lang}&search-eng={eng}'>{change_string.change_string(i, '<', '$#60;')}</a></h3></fieldset>\n"
                else:
                    web_search_html += '<h1>No Values Found</h1>'
            except:
                web_search_html += '<h1>No Values Found</h1>'
        elif eng == 'britannica':
            if Search is None:
                web_search_html = 'https://www.britannica.com/'
            else:
                web_search_html = f"<iframe src={'https://www.britannica.com/search?' + urllib.parse.urlencode({'query': Search})} width='100%' height='850px' style='border:none;'></iframe>"
        elif eng == 'ecosia':
            results = searchecosia.search_ecosia(Search)
            web_search_html += """<script>function evaluateMathExpression(expr) { const apiUrl = `https://api.mathjs.org/v4/?expr=${encodeURIComponent(expr)}`; return fetch(apiUrl) .then(response => { if (response.status >= 400) { return false; } return response.text(); }) .then(data => { return data; }) .catch(error => { return false; }); } evaluateMathExpression(document.getElementById("search").value) .then(result => { if (result) { console.log('Result:', result); let fieldset = document.createElement("fieldset"); let heading = document.createElement("h4"); heading.innerHTML = "Math.js Calculator Api"; heading.setAttribute("class", "links"); heading.setAttribute("style", "margin: 2px; margin-top: 4px;"); let iconDiv = document.createElement("div"); iconDiv.setAttribute("style", "display: flex; color: #687485; margin: 4px;"); let icon = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); icon.setAttribute("xmlns", "http://www.w3.org/2000/svg"); icon.setAttribute("width", "24"); icon.setAttribute("height", "24"); icon.setAttribute("fill", "currentColor"); icon.setAttribute("class", "bi bi-calculator"); icon.setAttributeNS(null, "viewBox", "0 0 16 16"); let iconPath = document.createElement("path"); iconPath.setAttribute("d", "M12 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h8zM4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4z"); let iconPath2 = document.createElement("path"); iconPath2.setAttribute("d", "M4 2.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5v-2zm0 4a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm3-6a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1zm0 3a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-4z"); let equation = document.createElement("p"); equation.innerHTML = document.getElementById("search").value + " = "; equation.setAttribute("class", "links"); equation.setAttribute("style", "display: flex; color: #687485; margin-left: 8px;"); let answer = document.createElement("h3"); answer.innerHTML = result; answer.setAttribute("class", "links"); answer.setAttribute("style", "margin-left: 16px;"); fieldset.appendChild(iconDiv); icon.appendChild(iconPath); icon.innerHTML += "\\n"; icon.appendChild(iconPath2); icon.innerHTML += "\\n"; iconDiv.appendChild(icon); iconDiv.appendChild(heading); fieldset.appendChild(equation); fieldset.appendChild(answer); let parentElement = document.getElementById("content"); parentElement.insertBefore(fieldset, parentElement.children[1]); }});</script>"""
            try:
                wikipedia.set_lang(lang)
                wikipedia_data = wikipedia.page(rawSearch, auto_suggest=False)
                wikipedia_summary = wikipedia_data.content.split('\n')[0]
                wikipedia_source = wikipedia_data.url
                web_search_html += f"<fieldset style='margin-bottom: 16px;'><div style='display: flex; color: #687485; margin: 4px;'><svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' fill='none' viewBox='0 0 24 24'><path fill='currentColor' fill-rule='evenodd' d='M21.167 13H14.5a.834.834 0 0 1 0-1.667h6.667a.834.834 0 0 1 0 1.667Zm0-4.167H14.5a.834.834 0 0 1 0-1.666h6.667a.834.834 0 0 1 0 1.666Zm0-4.166H14.5A.834.834 0 0 1 14.5 3h6.667a.834.834 0 0 1 0 1.667Zm-10 8.333H2.833A.834.834 0 0 1 2 12.167V3.833c0-.46.373-.833.833-.833h8.334c.46 0 .833.373.833.833v8.334c0 .46-.373.833-.833.833Zm-.834-8.333H3.667v6.666h6.666V4.667ZM2.833 15.5h18.334a.834.834 0 0 1 0 1.667H2.833a.834.834 0 0 1 0-1.667Zm0 4.167h13.334a.834.834 0 0 1 0 1.666H2.833a.834.834 0 0 1 0-1.666Z' clip-rule='evenodd'></path></svg><h4 class='links' style='margin: 2px;'>Summary</h4></div><p class='links'>{wikipedia_summary}</p><a href='/wiki?{urllib.parse.urlencode({'result': rawSearch})}&lang={lang}&search-eng={eng}'><h3 class='links' style='margin-bottom: 2px; color: #1a0dab;'>{change_string.change_string(wikipedia_data.title, '<', '&#60;')}</h3><h5 class='links' style='margin-top:0px; color: green;'>https://www.theaustenwiki.org/wiki?{urllib.parse.urlencode({'result': rawSearch})}&lang={lang}&search-eng=wikipedia</h5></fieldset>"
            except:
                pass
            if results != []:
                for result in results:
                    web_search_html += f"<fieldset><a target='_blank' href='{result['url']}'><h3 class='links' style='margin-bottom: 2px; color: #1a0dab;'>{change_string.change_string(result['title'], '<', '&#60;')}</h3><h5 class='links' style='margin-top:0px; color: green;'>{result['url']}</h5><em><p class='links' style='color: #202124;'>{change_string.change_string(result['description'], '<', '&#60;')}</p></em></a></fieldset>"
            else:
                web_search_html += '<h1>No Values Found</h1>'
        return htmlfunc.study_html_formater(web_search_html, Search, lang=lang, eng=eng, photo_q=urllib.parse.urlencode({'q': rawSearch}))

    # This would be our about page.
    @app.route('/about')
    def about():
        return htmlfunc.study_html_formater(htmlfunc.read('about.html'), 'About')
    
    # Baldwin Huang's auto-biografy
    @app.route('/about/baldwinhuang')
    def baldwinhuang():
        return htmlfunc.study_html_formater(htmlfunc.read('aboutBaldwinHuang.html'), 'Baldwin Huang')

    # This is Mael's biografy
    @app.route('/about/maelcamilolefevre')
    def maelcamilo():
        return htmlfunc.study_html_formater(htmlfunc.read('aboutMaelCamiloLefevre.html'), 'Mael-Camilo Lefevre')

    # Here we have a paraphrasing iframe.
    @app.route('/paraphraser')
    def paraphraser():
        return htmlfunc.study_html_formater(htmlfunc.read('paraphraser.html'), 'Paraphraser')

    # This is a Translator.
    @app.route('/translator')
    def translator():
        return htmlfunc.study_html_formater(htmlfunc.read('translator.html'), 'Translator')

    # This is a photo library.
    @app.route('/photos')
    def photos():
        args = request.args
        rawPhoto = args.get('q')
        photo = rawPhoto
        if photo is None:
            photo = 'https://www.bing.com/images/feed'
        else:
            photo = "https://www.bing.com/images/search?" + urllib.parse.urlencode({'q': photo})
        return htmlfunc.study_html_formater(f'''<div style='width:100%; float: left;'>
    <iframe src="{photo}" width="100%" height="850px" style="border:none;"></iframe>
</div>
<script>document.getElementById('search').value = '{rawPhoto}'</script>
''', 'Photo Library')

    # This is a background remover.
    @app.route('/bgremover')
    def bgremover():
        print(htmlfunc.study_html_formater(htmlfunc.read('bgremover.html'), 'Background Remover'))
        return htmlfunc.study_html_formater(htmlfunc.read('bgremover.html'), 'Background Remover')

    # This is a citation machine.
    @app.route('/citations')
    def citations():
        return htmlfunc.study_html_formater(htmlfunc.read('citations.html'), 'Citations')
    
    # This is a RickRoll
    @app.route('/rickroll')
    def rickroll():
        return htmlfunc.study_html_formater(htmlfunc.read('rickroll.html'), 'Haha, get Rickrolled')

    # This is the ten-minute mail iframe.
    @app.route('/tenminutemail')
    def tenminutemail():
        return htmlfunc.study_html_formater(htmlfunc.read('tenminutemail.html'), 'Ten Minute Mail')

    # Our own Austen News Link
    @app.route('/news')
    def news():
        return render_template('austennews.html')
    
    # This is a math white board.
    @app.route('/maths')
    def maths():
        return htmlfunc.study_html_formater(htmlfunc.read('maths.html'), 'Math')

    # Llama 2 AI
    @app.route('/llama2ai')
    def llama2ai():
        return htmlfunc.study_html_formater(htmlfunc.read('llama2ai.html'), 'Llama 2 AI')

################
# Game Section #

# Here we have the home page for games.
@app.route('/games')
def games():
    return htmlfunc.games_html_formater(htmlfunc.read('games.html'), 'Austen Games')

class game_section:
        @app.route('/games/dino')
        def dino():
            return htmlfunc.games_html_formater(htmlfunc.read('dino.html'), 'Google Dino')

        @app.route('/games/tetris')
        def tetris():
            return htmlfunc.games_html_formater(htmlfunc.read('tetris.html'), 'Tetris')

        @app.route('/games/chess')
        def chess():
            return htmlfunc.games_html_formater(htmlfunc.read('chess.html'), 'Chess')

        @app.route('/games/solitaire')
        def solitaire():
            return htmlfunc.games_html_formater(htmlfunc.read('solitaire.html'), 'Solitaire')

        @app.route('/games/fruitninja')
        def fruitninja():
            return htmlfunc.games_html_formater(htmlfunc.read('fruitninja.html'), 'Fruit Ninja')

        @app.route('/games/pingpong')
        def pingpong():
            return htmlfunc.games_html_formater(htmlfunc.read('pingpong.html'), 'Ping Pong')

        @app.route('/games/topspeed3d')
        def topspeed3d():
            return htmlfunc.games_html_formater(htmlfunc.read('topspeed3d.html'), 'Top Speed 3D')

        @app.route('/games/baseball')
        def baseball():
            return htmlfunc.games_html_formater(htmlfunc.read('baseball.html'), 'Baseball')

        @app.route('/games/zombies')
        def zombies():
            return htmlfunc.games_html_formater(htmlfunc.read('zombies.html'), 'Plant vs. Zombies')
        
        @app.route('/games/pacman')
        def pacman():
            return htmlfunc.games_html_formater(htmlfunc.read('pacman.html'), 'PACman')

        @app.route('/games/firstpersonshooter')
        def firstpersonshooter():
            return htmlfunc.games_html_formater(htmlfunc.read('1v1lol.html'), '1v1 Lol')

        @app.route('/games/othergames')
        def othergames():
            return htmlfunc.games_html_formater(htmlfunc.read('othergames.html'), 'Other Github Games')

# End Game Section #
####################

# Here I store some dev sites.
@app.route('/dev')
def dev():
    return render_template('dev.html')

class dev_section():
    pass

# End of site templates #
#########################
#########################

# Down here we just publish the website
# "host='0.0.0.0'" just means to publish it on all available hosts.
# When published "debug" should be set to false or not even be there.

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

#########################################
# Don't write any code below this line. #
#########################################
