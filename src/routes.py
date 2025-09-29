from flask import Blueprint, request, render_template, jsonify
from .models import RECIPES, SUBSTITUTIONS, R2I
from .utils import greedy_suggest, backtracking_best_combo, analyze_gaps

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', recipes=RECIPES)

@main_bp.route('/suggest', methods=['POST'])
def suggest():
    available_raw = request.form.get('available', '')
    available = [x.strip() for x in available_raw.split(',') if x.strip()]
    top_k = int(request.form.get('top_k', 5))
    max_combo = int(request.form.get('max_combo', 2))
    allow_missing = int(request.form.get('allow_missing', 2))

    greedy = greedy_suggest(available, top_k=top_k)
    combos = backtracking_best_combo(available, max_recipes=max_combo, allow_missing=allow_missing)

    subs = {}
    for s in greedy:
        for m in s['missing_ingredients']:
            subs[m] = SUBSTITUTIONS.get(m.lower(), [])
    for c in combos:
        for m in c['missing_ingredients']:
            subs[m] = SUBSTITUTIONS.get(m.lower(), [])

    return render_template('suggest.html', greedy=greedy, combos=combos, subs=subs, available_raw=available_raw)

@main_bp.route('/shopping', methods=['POST'])
def shopping():
    available_raw = request.form.get('available', '')
    available = [x.strip().lower() for x in available_raw.split(',') if x.strip()]
    picks = request.form.getlist('pick')
    shopping_set = set()
    for p in picks:
        ings = R2I.get(p, [])
        for ing in ings:
            if ing.lower() not in available:
                shopping_set.add(ing)
    return render_template('shopping.html', list_items=sorted(shopping_set))

# ------------------ API ------------------

@main_bp.route('/api/suggest', methods=['POST'])
def api_suggest():
    data = request.get_json() or {}
    available = data.get('available', [])
    top_k = data.get('top_k', 5)
    max_combo = data.get('max_combo', 2)
    allow_missing = data.get('allow_missing', 2)
    greedy = greedy_suggest(available, top_k=top_k)
    combos = backtracking_best_combo(available, max_recipes=max_combo, allow_missing=allow_missing)
    return jsonify({"greedy": greedy, "combos": combos})

@main_bp.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.get_json() or {}
    recipe = data.get('recipe')
    available = data.get('available', [])
    if recipe not in RECIPES:
        return jsonify({"error": "unknown recipe"}), 400
    missing, suggestions = analyze_gaps(recipe, available)
    return jsonify({"missing": missing, "substitutions": suggestions})
