import os
import traceback
from flask import Flask, jsonify, app, Blueprint, request, render_template
from sqlalchemy.orm.exc import NoResultFound
from database.database_session import Session, get_session, engine
from mappings.characters_mapping import Character
from http import HTTPStatus

path = os.path.dirname(os.path.abspath(__file__))


character_blueprint = Blueprint('admin', __name__, static_folder='./ static', template_folder='templates')


@character_blueprint.route('/',methods= ['GET'])
def index():

    response = request.args.get(f'http://127.0.0.1:8080/')
    print(response)
    message = getAllTheDataFronTheDatabase()
    return render_template('index.html', message=message)

def getAllTheDataFronTheDatabase():
    session = get_session()
    print(session.query(Character).count())
    info = session.query(Character).filter().all()
    # for result in info:
    #     # print(str(results))
    #     print(result.name + result.description)
    # print(info[0])
    return info


@character_blueprint.route('/characters', methods= ['GET'])
def displayAll():
    message = getAllTheDataFronTheDatabase()
    return render_template('displayall.html', message=message)

@character_blueprint.route('/characters', methods= ['POST'])   #getOne method
def returndescription():
    #data = request.args.get('name')
    data =request.form['char_name']
    print(data)
    # if not data:
    #      raise NoResultFound('Please add the name of the character')
    try:
        session = get_session()
        info = session.query(Character).filter(Character.name == data).one()
    except NoResultFound:
        return data + 'was not found'

    #return str(info)
    return render_template('returndescription.html', message = info)

@character_blueprint.route('/post', methods= ['POST'])
def insert_characters():
    #data = request.get_json()
    Name =request.form['Name']
    Description = request.form['character_info']
    Power = request.form['character_power']

    if not Name:
        return "All fields are required "
    if not Description:
        return "All fields are required "
    if not Power:
        return "All fields are required "
    session = get_session()
    character = Character(name=Name,
                          description=Description,
                          power=Power)
    try:
        session.add(character)
        session.commit()

    except NoResultFound:
        session.rollback()
        return("failed to add")
    finally:
        session.close()
    message = "added successfully"

    return "successfully added"

@character_blueprint.route('/delete', methods= ['POST'])
def deletetheentry():
    #data = request.get_json()
    data = request.form['character_delete']
    if not data:
        return "Please add name of the character"
    print(data)
    #Name = data['name']
    session = get_session()
    cnt  = session.query(Character).count()
    query = session.query(Character).filter_by(name=data).one()

    try:
        if(cnt > 5 ):
            print("Inside the delete")
            session.delete(query)
            # session.Flush()
            session.commit()
        else:
            return ("Cannot delete")

    except NoResultFound:
        traceback.print_exc()
        session.rollback()
        return ("failed to delete")
    finally:
        session.close()

    message = "deleted"
    return message

@character_blueprint.route('/put', methods= ['POST'])
def updateTheEntry():
    # data =  request.get_json()
    # character_name = request.form('Character')
    # print(character_name)
    character_name = request.form['Character']
    description = request.form['character_info']
    if not description:
        return "Please add discription"
    print(character_name)

    session = get_session()
    info = session.query(Character).filter(Character.name == character_name).one()
    power = info.power

    Id = info.id
    power = info.power
    power_level = info.power_level
    session.delete(info)

    character = Character(id =Id ,  name=character_name,
                          description=description,
                          power=power, power_level=power_level)
    print(character)
    try:
        session.add(character)
        session.commit()

    except NoResultFound:
        session.rollback()
        return ("failed to update")
    finally:
        session.close()

    return "successfully Updated"




