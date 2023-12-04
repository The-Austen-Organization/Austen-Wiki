import change_string
Script = '''
let state = false;
function showBar() {
    if (state) {
        document.getElementsByClassName('setting')[0].setAttribute("onclick", "");
        let height = document.getElementsByClassName('toplogo')[0].clientHeight + 8;
        let place = document.getElementsByClassName('topbar')[0].clientHeight + 32;
        height = height + height * 0.15;
        let animation = setInterval(frame, 1);
        function frame() {
            if (place <= height) {
                clearInterval(animation)
                document.getElementById("content").style.top = height + "px";
                let toplink = document.getElementsByClassName('toplink');
                for (let i = 0; i < toplink.length; i++) {
                    toplink[i].style.visibility = "hidden";
                }
                document.getElementsByClassName('setting')[0].setAttribute("onclick", "showBar()");
                state = false;
            }
            else {
                place -= 5
                document.getElementById("content").style.top = place + "px";
            }
        }
        }
    else {
        document.getElementsByClassName('setting')[0].setAttribute("onclick", "");
        let toplink = document.getElementsByClassName('toplink');
        for (let i = 0; i < toplink.length; i++) {
            toplink[i].style.visibility = "visible"
        }
        let height = document.getElementsByClassName('topbar')[0].clientHeight + 32;
        let place = document.getElementsByClassName('toplogo')[0].clientHeight;
        place = place + place * 0.15;
        let animation = setInterval(frame, 1);
        function frame() {
            if (place >= height) {
                clearInterval(animation)
                document.getElementById("content").style.top = height + "px";
                document.getElementsByClassName('setting')[0].setAttribute("onclick", "showBar()");
            }
            else {
                place += 5
                document.getElementById("content").style.top = place + "px";
            }
        }
        state = true;
    }
}'''
Style = '''
.sidelink , .toplink{
    font-family: Serif;
    font-weight: normal;
    font-size: large;
}
.button {
    width: 40px;
}
.content {
    width: 89%;
    float: right;
    margin-left: 5px;
    background-color: white;
}

a {
    color: #000;
    text-decoration: none;
}
fieldset {
    border-radius: 8px;
}
.sidebar {
    float: left; 
    max-width: 150px;
    min-width: 10px;
}
.logo {
    width: 100%;
}
.links {
    font-family: didot; 
    font-weight: 300;
}
@media only screen and (min-width: 776px)  {
    .toplogo, .toplink, .setting, .topbar{
        display: None;
    }
    .sidebar {
        position: fixed;
    }
@media only screen and (max-width: 1430px) {
    fieldset { 
        -webkit-border-radius: 8px;
        -moz-border-radius: 8px;
        border-radius: 8px;
    }
    .sidebar {
        width: 40px;
        
    }
    .sidelink {
        font-size: small;
    }
    .logo {
        width: 100px;
    }
    .content {
        width: 89%;
        margin-left: 5px;
    }
    .links {
        font-family: didot; 
        font-weight: 300;
        font-size: medium;
    }
}
@media only screen and (max-width: 1230px) {
    fieldset { 
        -webkit-border-radius: 8px;
        -moz-border-radius: 8px;
        border-radius: 8px;
    }
    .sidebar {
        width: 40px;
        
    }
    .sidelink {
        font-size: smaller;
    }
    .logo {
        width: 80px;
    }
    .content {
        width: 89%;
        margin-left: 5px;
    }
    .links {
        font-family: didot; 
        font-weight: 300;
        font-size: medium;
    }
}
@media only screen and (max-width: 1050px) {
    fieldset { 
        border-radius: 8px;
    }
    .sidebar {
        width: 40px;
        
    }
    .sidelink {
        font-size: x-small;
    }
    .logo {
        width: 70px;
    }
    .content {
        width: 89%;
        margin-left: 5px;
    }
    .links {
        font-family: didot; 
        font-weight: 300;
        font-size: small;
    }
}
@media only screen and (max-width: 1025px) {
    fieldset { 
        border-radius: 8px;
    }
    .sidebar {
        width: 40px;
        
    }
    .sidelink {
        font-size: xx-small;
    }
    .logo {
        width: 60px;
    }
    .content {
        width: 89%;
        margin-left: 5px;
    }
    .links {
        font-family: didot; 
        font-weight: 300;
        font-size: smaller;
    }
}
@media only screen and (max-width: 850px) {
    fieldset { 
        border-radius: 8px;
    }
    .sidebar {
        width: 40px;
        
    }
    .sidelink {
        font-size: xx-small;
    }
    .logo {
        width: 50px;
    }
    .content {
        width: 89%;
        margin-left: 5px;
    }
    .links {
        font-family: didot; 
        font-weight: 300;
        font-size: x-small;
    }
}
}
@media only screen and (max-width: 775px) {
.setting {
    width: 10%;
    margin-left: 45%;
    margin-top: 3%;
    margin-bottom: 3%;
    display: initial;
}
.toplink {
    font-size: small;
    margin-left: 16px;
    visibility: hidden;
}
.topbar {
    width: 100%;
}
.toplogo{
    width: 40%;
    margin-bottom: 2%;
}
fieldset { 
    border-radius: 8px;
}
.sidebar {
    display: None;
}
.sidelink {
    font-size: 0px;
}
.logo {
    width: 0px;
}
.content {
    width: 100%;
    position: absolute;
    height: 650px;
}
.links {
    font-family: didot; 
    font-weight: 300;
    font-size: small;
}
'''
def study_html_formater(input, title, lang='en', eng='ecosia', photo_q=''):
    if lang == 'es':
        lang_default = '''<option value="es">Español</option>
                          <option value="en">English</option>
                          <option value="fr">Français</option>'''
    elif lang == 'fr':
        lang_default = '''<option value="fr">Français</option>
                          <option value="es">Español</option>
                          <option value="en">English</option>
                          '''
    else:
        lang_default = '''<option value="en">English</option>
                          <option value="es">Español</option>
                          <option value="fr">Français</option>'''
    if eng == 'ecosia':
        eng_code = '''<option value="ecosia">Ecosia</option>
                      <option value="wikipedia">Wikipedia</option>
                      <option value="britannica">Britannica</option>
                 '''
    elif eng == 'britannica':
        eng_code = '''<option value="britannica">Britannica</option>
                      <option value="ecosia">Ecosia</option>
                      <option value="wikipedia">Wikipedia</option>
                      '''
    else:
        eng_code = '''<option value="wikipedia">Wikipedia</option>
                      <option value="britannica">Britannica</option>
                      <option value="ecosia">Ecosia</option>
                 '''
    return f'''
    <!DOCTYPE html>
    <html lang="{lang}">
        <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link rel="icon" type="image/x-icon" href="https://static.wixstatic.com/media/c1b42d_05c2082d93994ffdab3369a0b7daa687~mv2.png/v1/fill/w_614,h_614,al_c,lg_1,q_90,enc_auto/c1b42d_05c2082d93994ffdab3369a0b7daa687~mv2.png">
            <title>{change_string.change_string(title, '<', '&#60')}</title>
            ''' + """
            
            """ + f'''<script>
                {Script}
            </script>
            <style>
                {Style}
            </style>
        </head>
        <body>
            <div class="topbar">
                <a href='/'><img class="toplogo" alt="Logo" src="https://static.wixstatic.com/media/c1b42d_98f394b365c94b2cb0ab1e777a5a6b09~mv2.png/v1/fill/w_1384,h_462,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/c1b42d_98f394b365c94b2cb0ab1e777a5a6b09~mv2.png" width="100%"></a>
                <img class="setting" onclick="showBar()" src="https://static.wixstatic.com/media/c1b42d_67ed5b7e27164b0fabb4b2798077edff~mv2.png/v1/fill/w_600,h_600,al_c,lg_1,q_85,enc_auto/c1b42d_67ed5b7e27164b0fabb4b2798077edff~mv2.png">
                <h3 class="toplink"><a href='/'>Home</a></h3>
                <h3 class="toplink"><a href='/about'>About</a></h3>
                <h3 class="toplink"><a href="/games">Games</a></h3>
                <h3 class="toplink"><a href="/paraphraser">Paraphraser</a></h3>
                <h3 class="toplink"><a href="https://app.copyleaks.com/">Plagiarism</a></h3>
                <h3 class="toplink"><a href="/translator">Translator</a></h3>
                <h3 class="toplink"><a href="/photos?{photo_q}">Photos</a></h3>
                <h3 class="toplink"><a href="/bgremover">Back Ground Remover</a></h3>
                <h3 class="toplink"><a href="/citations">Citation Machine</a></h3>
                <h3 class="toplink"><a href="/tenminutemail">Ten Minute Mail</a></h3>
                <h3 class="toplink"><a href="/maths">Maths</a></h3>
                <h3 class="toplink"><a href="/llama2ai">Llama 2 AI</a></h3>
            </div>
            <div class="sidebar">
                <fieldset>
                    <a href='/'><img class="logo" alt="Logo" src="https://static.wixstatic.com/media/c1b42d_98f394b365c94b2cb0ab1e777a5a6b09~mv2.png/v1/fill/w_1384,h_462,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/c1b42d_98f394b365c94b2cb0ab1e777a5a6b09~mv2.png" width="100%"></a>
                    <h3 class="sidelink"><a href='/'>Home</a></h3>
                    <h3 class="sidelink"><a href='/about'>About</a></h3>
                    <h3 class="sidelink"><a href="/games">Games</a></h3>
                    <h3 class="sidelink"><a href="/paraphraser">Paraphraser</a></h3>
                    <h3 class="sidelink"><a href="https://app.copyleaks.com/">Plagiarism</a></h3>
                    <h3 class="sidelink"><a href="/translator">Translator</a></h3>
                    <h3 class="sidelink"><a href="/photos?{photo_q}">Photos</a></h3>
                    <h3 class="sidelink"><a href="/bgremover">Back Ground Remover</a></h3>
                    <h3 class="sidelink"><a href="/citations">Citation Machine</a></h3>
                    <h3 class="sidelink"><a href="/tenminutemail">Ten Minute Mail</a></h3>
                    <h3 class="sidelink"><a href="/maths">Maths</a></h3>
                    <h3 class="sidelink"><a href="/llama2ai">Llama 2 AI</a></h3>
                </fieldset>
            </div>
            <div class="content" id="content">
                <form name="inputs" action="search" method="get">
                    <Label for="search">Search: </Label><input value='{change_string.change_string(title, "'", '&#39')}' onfocus="this.select()" id="search" name="search" type="text" autofocus="autofocus" accesskey="F" dir="auto" autocomplete="off" style="border-radius: 8px; margin: 4px; width: 50%;"><input style="background-color:rgb(64, 101, 197); color:white; border: 0px; border-radius: 8px; " type="submit" value="Search">
                    <label for="lang"></label>
                    <select name="lang" id="lang" style="border-radius: 8px;">
                        {lang_default}
                    </select>
                    <select name="search-eng" id="search-eng" style="border-radius: 8px;">
                        {eng_code}
                    </select>
                </form>''' + '\n' + input + '\n' +'''</div>
            </div>
            <script>
                window.onload = function(){
                    let height = document.getElementsByClassName('toplogo')[0].clientHeight + 8;
                    height = height + height * 0.15;
                    document.getElementById("content").style.top = height + 'px';
                    document.getElementsByTagName('iframe')[0].style.height = window.innerHeight - 45.5 + 'px';
                }
            </script>
        </body>
    </html>'''
def games_html_formater(input, title):
    return f'''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="icon" type="image/x-icon" href="https://static.wixstatic.com/media/c1b42d_05c2082d93994ffdab3369a0b7daa687~mv2.png/v1/fill/w_614,h_614,al_c,lg_1,q_90,enc_auto/c1b42d_05c2082d93994ffdab3369a0b7daa687~mv2.png">    
        <title>{change_string.change_string(title, '<', '&#60')}</title>
        ''' + """

        """ + f'''<link href="images" rel="icon" type="image/png">
        <style>{Style}</style>
        <script>{Script}</script>
    </head>
    <body>
        <div class="topbar">
            <a href='/games'><img class="toplogo" alt="Logo" src="https://static.wixstatic.com/media/c1b42d_f9912844c30845c59005e2577a87b7fa~mv2.png/v1/fill/w_1480,h_494,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/c1b42d_f9912844c30845c59005e2577a87b7fa~mv2.png" width="90%"></a>
            <img class="setting" onclick="showBar()" src="https://static.wixstatic.com/media/c1b42d_67ed5b7e27164b0fabb4b2798077edff~mv2.png/v1/fill/w_600,h_600,al_c,lg_1,q_85,enc_auto/c1b42d_67ed5b7e27164b0fabb4b2798077edff~mv2.png">
            <h3 class="toplink"><a href='/'>Home</a></h3>
            <h3 class="toplink"><a href='/about'>About</a></h3>
            <h3 class="toplink"><a href="/games">Games</a></h3>
        </div>
        <div class="sidebar">
            <fieldset>
                <a href='/games'><img class="logo" alt="Logo" src="https://static.wixstatic.com/media/c1b42d_f9912844c30845c59005e2577a87b7fa~mv2.png/v1/fill/w_1480,h_494,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/c1b42d_f9912844c30845c59005e2577a87b7fa~mv2.png" width="90%"></a>
                <h3 class="sidelink"><a href='/'>Home</a></h3>
                <h3 class="sidelink"><a href='/about'>About</a></h3>
                <h3 class="sidelink"><a href="/games">Games</a></h3>
            </fieldset>
        </div>
        <div class="content" id="content">
            ''' + input + '''
        </div>
        <script>
            window.onload = function(){
                let height = document.getElementsByClassName('toplogo')[0].clientHeight + 8;
                height = height + height * 0.15;
                document.getElementById("content").style.top = height + 'px';
                document.getElementsByTagName('iframe')[0].height = window.innerHeight - 16 + 'px';
            }
        </script>
    </body>
</html>'''
def read(file_name, noTabs=0):
    with open('templates/' + file_name, 'r') as file:
        return file.read()
