from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener las notas y la asistencia del formulario 
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        
        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3
        
        # Determinar si está aprobado o reprobado
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        
        return render_template('ejercicio1.html', 
                              promedio=round(promedio, 1), 
                              estado=estado, 
                              mostrar_resultado=True)
    return render_template('ejercicio1.html', mostrar_resultado=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)
        
        return render_template('ejercicio2.html', 
                              nombre_largo=nombre_mas_largo, 
                              longitud=longitud, 
                              mostrar_resultado=True)
    return render_template('ejercicio2.html', mostrar_resultado=False)

if __name__ == '__main__':
    app.run(debug=True)