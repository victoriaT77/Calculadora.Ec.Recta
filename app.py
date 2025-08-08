from flask import Flask, render_template, request
from plane_solver import compute_plane_equation

app = Flask(__name__)

def parse_vector(text):
    """Convierte una cadena como '(1.0, 2.0, 3.0)' en una lista de floats."""
    try:
        # Elimina paréntesis y espacios, luego separa por coma
        cleaned = text.strip().replace("(", "").replace(")", "")
        parts = list(map(float, cleaned.split(",")))
        if len(parts) != 3:
            raise ValueError("El vector no tiene 3 componentes.")
        return parts
    except:
        raise ValueError("Formato inválido. Usa (x, y, z)")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            v1 = parse_vector(request.form["vector1"])
            v2 = parse_vector(request.form["vector2"])
            v3 = parse_vector(request.form["vector3"])

            plane_eq, normal = compute_plane_equation(v1, v2, v3)

            return render_template("result.html",
                                   A=v1, B=v2, C=v3,
                                   normal=normal.tolist(),
                                   plane_eq=plane_eq,
                                   points_json=[v1, v2, v3],
                                   normal_json=normal.tolist())
        except Exception as e:
            return render_template("index.html", error=f"❌ Entrada inválida: {str(e)}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)