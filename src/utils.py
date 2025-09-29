import heapq
import itertools
from .models import R2I, SUBSTITUTIONS

def greedy_suggest(available, top_k=5):
    available_set = set(x.strip().lower() for x in available)
    heap = []
    for recipe, ings in R2I.items():
        ings_lower = set(i.lower() for i in ings)
        have = len(ings_lower & available_set)
        total = len(ings_lower)
        missing = total - have
        coverage = have / total
        score = coverage - 0.1 * missing
        heapq.heappush(heap, (-score, missing, -coverage, recipe))
    results = []
    for _ in range(min(top_k, len(heap))):
        score, missing, negcov, recipe = heapq.heappop(heap)
        score = -score
        coverage = -negcov
        results.append({
            "recipe": recipe,
            "score": round(score, 3),
            "coverage": round(coverage, 3),
            "missing": missing,
            "missing_ingredients": sorted([ing for ing in R2I[recipe] if ing.lower() not in available_set])
        })
    return results


def backtracking_best_combo(available, max_recipes=3, allow_missing=3):
    available_set = set(x.strip().lower() for x in available)
    recipes = list(R2I.keys())
    best = []
    def evaluate(combo):
        combo_ings = set()
        for r in combo:
            combo_ings.update(R2I[r])
        combo_ings_lower = set(i.lower() for i in combo_ings)
        covered = len(combo_ings_lower & available_set)
        missing = len(combo_ings_lower - available_set)
        return covered, missing, combo_ings
    for r in range(1, max_recipes + 1):
        for combo in itertools.combinations(recipes, r):
            covered, missing, combo_ings = evaluate(combo)
            if missing <= allow_missing:
                best.append({
                    "recipes": combo,
                    "covered": covered,
                    "missing": missing,
                    "missing_ingredients": sorted([ing for ing in combo_ings if ing.lower() not in available_set])
                })
    best.sort(key=lambda x: (-x["covered"], x["missing"], len(x["recipes"])))
    return best[:10]


def analyze_gaps(recipe, available):
    available_set = set(x.strip().lower() for x in available)
    ings = R2I[recipe]
    missing = [ing for ing in ings if ing.lower() not in available_set]
    suggestions = {}
    for ing in missing:
        key = ing.lower()
        suggestions[ing] = SUBSTITUTIONS.get(key, [])
    return missing, suggestions
