from whatsapp.app import app
from whatsapp import utils
from flask import jsonify, request, make_response
import os
import datetime


@app.route('/')
def home():
    return "Home view"


@app.route('/start-chat', methods=['POST'])
def start_chat():
    request_body = request.get_json()
    # check inputs: format should be correct and user should not already exist
    if 'username1' and 'username2' not in request_body:
        return make_response(jsonify(error="The body must contain 'username1' and 'username 2' for sign up."), 400)
    username1 = request_body['username1']
    username2 = request_body['username2']

    if utils.chat_exists(username1, username2):
        return make_response(jsonify(error=f"Conversation between {username1} and {username2} already exists."), 400)

    # create a directory and text file for the chat
    chats_folder = f'whatsapp/chats/{username1}_{username2}'
    try:
        os.makedirs(chats_folder)
        with open(os.path.join(chats_folder, f'{username1}_{username2}_chat.txt'), 'w'):
            pass
        return make_response(jsonify(message='ok'), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/send-message', methods=['POST'])
def send_message():
    request_body = request.get_json()
    username1 = request_body['username1']
    username2 = request_body['username2']
    message = request_body['message']
    sender = request_body['sender']
    # inputs: username1, username2, message
    # check if user is present
    chats_folder = f'whatsapp/chats/{username1}_{username2}'
    if not utils.chat_exists(username1, username2):
        return make_response(jsonify(error=f"Chat between {username1} and {username2} does not exist."), 400)
    # check input format

    if 'username1' not in request_body or 'username2' not in request_body or 'sender' not in request_body or 'message' not in request_body:
        return make_response(jsonify(error="The body must contain 'usernames' and 'message' for create message."), 400)

    # if chat is present add text message to it
    now = datetime.datetime.now()
    with open(f'{chats_folder}/{username1}_{username2}_chat.txt', 'a') as message_file:
        # message_file.write('\n')
        message_file.write(f'{sender}: {message} \t@ {now.strftime("%Y-%m-%d %H:%M:%S")}\n')
    return make_response(jsonify(message='ok'), 200)


@app.route('/get-messages', methods=['GET'])
def get_messages():
    request_body = request.get_json()
    username1 = request_body['username1']
    username2 = request_body['username2']
    chats_folder = f'whatsapp/chats/{username1}_{username2}'
    try:
        chat_file = open(f'{chats_folder}/{username1}_{username2}_chat.txt', 'r')
        messages_content = chat_file.read()
        chat_file.close()
        return make_response(jsonify(text=messages_content), 200)
    except Exception as e:
        print('error')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/edit-message', methods=['PATCH'])
def edit_message():
    request_body = request.get_json()
    now = datetime.datetime.now()
    username1 = request_body['username1']
    username2 = request_body['username2']
    message = request_body['message']
    sender = request_body['sender']
    chats_folder = f'whatsapp/chats/{username1}_{username2}'
    try:
        with open(f'{chats_folder}/{username1}_{username2}_chat.txt', 'r') as chat_file:
            messages_lines = chat_file.readlines()
        with open(f'{chats_folder}/{username1}_{username2}_chat.txt', 'w') as chat_file:
            messages_lines[-1] = f'{sender}: {message} \t@ {now.strftime("%Y-%m-%d %H:%M:%S")}\n'
            chat_file.writelines(messages_lines)
        return make_response(jsonify(message='ok'), 200)
    except Exception as e:
        print('error')
        return make_response(jsonify(error=str(e)), 500)
