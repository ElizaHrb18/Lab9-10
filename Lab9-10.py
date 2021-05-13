class Economie:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "1) Ofertanții de monedă pot fi:\n"
    "(a)agenții economici care au prisos de disponibilități bănești \n"
    "(b)băncile\n(c)societățile de asigurări\n",
    "2) Pentru a stimula investițiile, rata dobânzii trebuie să fie:\n(a)superioară ratei medii de rentabilitate\n"
    "(b)inferioară ratei medii de rentabilitate\n(c)egală cu rata medie de rentabilitate\n",
    "3) Bursa este o piață specializată unde se vând și se cumpără:\n(a)titluri\n(b)mărfuri de toate categoriile\n"
    "(c)mărfuri omogene\n",
    "4) în cazul unei operațiuni bursiere la termen, de pe urma creșterii cursului acțiunilor nu câștigă:"
    "\n(a)firma care a emis acțiunile \n(b)cumpărătorul\n(c)vânzătorul\n",
]
questions = [
    Economie(question_prompts[0], "a"),
    Economie(question_prompts[1], "b"),
    Economie(question_prompts[2], "a"),
    Economie(question_prompts[3], "c"),
]
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions))
run_quiz(questions)
