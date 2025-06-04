from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

excuses = [
    "Kochanie, utknąłem w korku przez remonty na drodze!",
    "Szef zwołał nagłe spotkanie, nie mogłem wyjść wcześniej.",
    "Pomagałem starszej pani z zakupami, nie mogłem jej zostawić.",
    "Auto nie chciało odpalić, musiałem czekać na pomoc drogową.",
    "Zgubiłem klucze i musiałem ich szukać po całym biurze!",
    "Musiałem zostać dłużej, bo kolega miał urodziny.",
    "Zepsuł się tramwaj i musiałem iść pieszo.",
    "Telefon się rozładował, nie mogłem zadzwonić.",
    "Szef poprosił o pomoc przy ważnym projekcie.",
    "Zgubiłem portfel i musiałem go szukać.",
    "Pomagałem koledze z przeprowadzką.",
    "Byłem świadkiem wypadku i musiałem złożyć zeznania.",
    "Zatrzymała mnie policja do kontroli.",
    "Musiałem poczekać na kuriera z ważną przesyłką.",
    "Winda się zepsuła i musiałem schodzić po schodach.",
    "Zgubiłem bilet miesięczny i musiałem kupić nowy.",
    "Kolega poprosił o podwózkę do domu.",
    "Była awaria prądu w biurze.",
    "Musiałem naprawić coś w pracy przed wyjściem.",
    "Zostałem, żeby pomóc nowemu pracownikowi."
]

beer_reasons = [
    "Zasługuję na piwo, bo uratowałem projekt w pracy!",
    "Dzień był tak ciężki, że tylko piwo może mnie uratować.",
    "Obiecałem sobie, że dziś się zrelaksuję przy piwie.",
    "Dostałem pochwałę od szefa, więc należy mi się nagroda!",
    "Przetrwałem dzień bez narzekania, to zasługuje na piwo.",
    "Zrobiłem dziś coś dobrego dla innych.",
    "Nie spóźniłem się do pracy ani razu w tym tygodniu.",
    "Pomogłem koledze, więc zasługuję na chwilę relaksu.",
    "Dziś jest idealny dzień na piwo!",
    "Zaliczyłem ważny projekt przed terminem.",
    "Dzieci były dziś wyjątkowo grzeczne.",
    "Zrobiłem zakupy bez przypominania.",
    "Naprawiłem coś w domu.",
    "Zrobiłem obiad dla całej rodziny.",
    "Nie narzekałem na korki.",
    "Zrobiłem trening po pracy.",
    "Dziś jest środa – mały piątek!",
    "Dostałem premię w pracy.",
    "Zdałem ważny egzamin.",
    "Po prostu zasługuję na piwo!"
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Generator wymówek i powodów na piwo</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f7f7f7; text-align: center; margin-top: 60px; }
        #excuse-box { margin: 30px auto; padding: 30px; background: #fff; border-radius: 10px; box-shadow: 0 2px 8px #ccc; width: 60%; }
        button { padding: 15px 30px; font-size: 1.2em; border: none; border-radius: 8px; background: #007bff; color: #fff; cursor: pointer; transition: background 0.2s; }
        button:hover { background: #0056b3; }
        #result { margin-top: 30px; font-size: 1.3em; color: #333; }
    </style>
</head>
<body>
    <div id="excuse-box">
        <h1>Generator wymówek i powodów na piwo</h1>
        <button onclick="generateExcuse()">Wygeneruj wymówkę i powód na piwo</button>
        <div id="result"></div>
    </div>
    <script>
        function generateExcuse() {
            fetch('/excuse')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerText = data.excuse + ' ' + data.beer;
                });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/excuse')
def excuse():
    excuse = random.choice(excuses)
    beer = random.choice(beer_reasons)
    return jsonify({'excuse': excuse, 'beer': beer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)