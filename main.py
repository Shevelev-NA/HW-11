from flask import Flask, render_template
from utils import Utils

app = Flask(__name__)



@app.route('/')
@app.route('/candidate/')
def get_all_candidates():
    """ Вывод списка всех кандидатов """

    req = Utils()

    FILENAME = "candidates.json"
    req.load_candidates(FILENAME)

    candidates = req.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def get_candidate(x):
    """ Поиск кандидатов по id """

    req = Utils()

    FILENAME = "candidates.json"
    req.load_candidates(FILENAME)
    req.load_candidates_from_json()

    candidate = req.get_candidate(x)
    if candidate:
        return render_template('single.html', item=candidate)
    return "NOT FOUND" # отображение в случае отсутствия совпадений


@app.route('/search/<candidate_name>')
def get_candidate_name(candidate_name):
    """ Поиск кандидатов по имени """

    req = Utils()

    FILENAME = "candidates.json"
    req.load_candidates(FILENAME)
    req.load_candidates_from_json()

    candidates = req.get_candidates_by_name(candidate_name)
    count_candidate = len(candidates) # Подсчет колличества найденых совпадений
    if candidates:
        return render_template('search.html', candidates=candidates, lens=count_candidate)
    return "NOT FOUND"  # отображение в случае отсутствия совпадений


@app.route('/skill/<skill_name>')
def get_candidate_skill(skill_name):
    """ Поиск кандидатов по навыкам """
    req = Utils()

    FILENAME = "candidates.json"
    req.load_candidates(FILENAME)
    req.load_candidates_from_json()

    candidates = req.get_candidates_by_skill(skill_name)
    count_candidate = len(candidates) # Подсчет колличества найденых совпадений
    if candidates:
        return render_template('skill.html', candidates=candidates, lens=count_candidate)
    return "NOT FOUND" # отображение в случае отсутствия совпадений


if __name__ == '__main__':
    app.run(port=5000, debug=False)