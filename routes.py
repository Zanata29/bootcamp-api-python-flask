from main import app
from dbmanager import DBManager
from flask import request, jsonify
import re

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

@app.route("/cursos/cadastrar", methods=["POST"])
def insert_curso():
    id,nome,turno,carga_horaria = request.get_json().values()
    if id < 0 or id > 99999:
        return jsonify({'error': 'ID do curso é inválido.'})
    if not nome:
        return jsonify({'error': 'Nome do curso é inválido.'})
    if turno not in ['matutino','vespertino','noturno']:
        return jsonify({'error': 'Turno do curso é inválido.'})
    if carga_horaria < 0 or carga_horaria > 1000:
        return jsonify({'error': 'Carga-horária do curso é inválida.'})
    
    return DATABASE.insert_all("Curso",[str(id),"'"+nome+"'","'"+turno+"'",str(carga_horaria)]) 

@app.route("/alunos/cadastrar", methods=["POST"])
def insert_aluno():
    cpf,nome,matricula,data_nascimento,telefone,email,status = request.get_json().values()
    if re.match(r'^\d{11}$', str(cpf)) is None:
        return jsonify({'error': 'CPF inválido.'})
    if not nome:
        return jsonify({'error': 'Nome do aluno é inválido.'})
    if re.match(r'^\d{13}$', matricula) is None:
        return jsonify({'error': 'Número de matrícula é inválido.'})
    if re.match(r'^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4})$', data_nascimento) is None:
        return jsonify({'error': 'Data de nascimento inválida.'})
    if re.match(r'^\d{11}$', telefone) is None:
        return jsonify({'error': 'Número de telefone inválido.'})
    if len(email) > 35 or re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is None:
        return jsonify({'error': 'Endereço de e-mail inválido.'})
    if status < 0 or status > 1:
        return jsonify({'error': 'Status do aluno é inválido.'})
    
    return DATABASE.insert_all("Aluno",[str(cpf),"'"+matricula+"'","'"+nome+"'","'"+data_nascimento+"'","'"+telefone+"'","'"+email+"'", str(status)]) 

@app.route("/alunos/matricular", methods=["POST"])
def insert_aluno_on_curso():
    aluno_cpf,curso_id = request.get_json().values()
    if not DATABASE.get_by_id("Aluno", str(aluno_cpf), "cpf").get_json():
        return jsonify({'error': 'Código de aluno informado não foi encontrado.'})
    if not DATABASE.get_by_id("Curso", str(curso_id)).get_json():
        return jsonify({'error': 'Código do curso informado não foi encontrado.'})
    
    return DATABASE.insert("AlunoCurso",["aluno_cpf","curso_id"],[str(aluno_cpf),str(curso_id)])

