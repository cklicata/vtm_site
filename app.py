from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle= "About")

@app.route('/estimate')
def estimate():
    return return_template('estimate.html', pageTitle= "Estimating VTM")

def calculate():
    radius=request.form['radius']
    height=request.form['height']
    radius=float(radius)
    height=float(height)
    pi=3.14


    tanktop_area=(radius*radius)*pi
    tanksides_area=(2*(pi*(radius*height)))
    total_area=tanksides_area+tanktop_area
    area_sqft=total_area/144
    material_cost=area_sqft*25
    labor_cost=area_sqft*15
    total_cost=material_cost+labor_cost
    print("Total Cost Estimate: $")
    
    return render_template('estimate.html',
        total_cost=total_cost)
    












if __name__ == '__main__':
    app.run(debug=True)