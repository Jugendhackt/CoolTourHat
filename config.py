import json
with open("p.json") as pfile:
	p = json.load(pfile)
	p_r = {}
	for i,x in enumerate(p):
		p_r[x] = i


import inquirer
questions = [
  inquirer.Checkbox('interests',
                    message="What are you interested in?",
                    choices=p,
                    ),
  inquirer.Checkbox('are',
                    message="What are you?",
                    choices=p,
                    ),
]
answers = inquirer.prompt(questions)
a_i = [p_r[x] for x in answers["interests"]]
a_a = [p_r[x] for x in answers["are"]]
c = {"i":a_i, "a":a_a}

with open("config.json","w") as cfile:
	json.dump(c, cfile)

print("config written")