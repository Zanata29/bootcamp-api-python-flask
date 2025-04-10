from main import app
from dbmanager import DBManager

DATABASE = DBManager("db/BD_Bootcamp.db")

@app.route("/")
def index():
    return 'Bem Vindo ao Bootcamp API'

@app.route("/ping")
def ping():
    return 'pong'

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return DATABASE.get_all("Aluno")

@app.route("/cursos", methods=["GET"])
def get_cursos(): 
    return DATABASE.get_all("Curso")

@app.route("/alunos/<int:id>", methods=["GET"])
def get_alunos_by_id(id):
    return DATABASE.get_by_id("Aluno", str(id), "cpf")

@app.route("/cursos/<int:id>", methods=["GET"])
def get_cursos_by_id(id):
    return DATABASE.get_by_id("Curso", str(id))

@app.route("/alunos/curso/<int:curso_id>", methods=["GET"])
def get_alunos_by_curso(curso_id):
    return DATABASE.raw_sql(
    """
    SELECT a.* FROM Aluno AS a
	JOIN AlunoCurso AS ac ON a.cpf = ac.aluno_cpf
	WHERE ac.curso_id = {id}
	ORDER BY a.nome
    """.format(id=curso_id)
    )

@app.route("/cursos/aluno/<int:aluno_cpf>", methods=["GET"])
def get_cursos_by_aluno(aluno_cpf):
        return DATABASE.raw_sql(
    """
    SELECT c.* FROM Curso AS c
	JOIN AlunoCurso AS ac ON c.id = ac.curso_id
	WHERE ac.aluno_cpf = {id}
	ORDER BY c.nome
    """.format(id=aluno_cpf)
    )