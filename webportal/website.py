import pygal
import json
from urllib2 import urlopen  # python 2 syntax
# from urllib.request import urlopen # python 3 syntax
 
from flask import Flask, render_template
from pygal.style import DarkSolarizedStyle
 
app = Flask(__name__)
 
#----------------------------------------------------------------------
@app.route('/')
def get_weather_data(date='20140415', state='IA', city='Ames'):
    """
    Date must be in YYYYMMDD
    """
    api_key = '510acf25c9603630'
    url = 'http://api.wunderground.com/api/{key}/history_{date}/q/{state}/{city}.json'
    new_url = url.format(key=api_key,
                         date=date,
                         state=state,
                         city=city)
    result = urlopen(new_url)
    js_string = result.read()
    parsed = json.loads(js_string)
    history = parsed['history']['observations']
 
    imp_temps = [float(i['tempi']) for i in history]
    times = ['%s:%s' % (i['utcdate']['hour'], i['utcdate']['min']) for i in history]
 
    # create a bar chart
    title = 'Temps for %s, %s on %s' % (city, state, date)
    bar_chart = pygal.Bar(margin=20, width=1200, height=600,
                          explicit_size=False, title=title,
                          style=DarkSolarizedStyle,
                          disable_xml_declaration=True)
    bar_chart.x_labels = times
    bar_chart.add('Temps in F', imp_temps)
 
    return render_template('index.html', 
                           title=title,
                           bar_chart=bar_chart)
 
 
#----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0')

