import os


def chat_exists(username1, username2):
    chats_folder = f'whatsapp/chats/{username1}_{username2}'
    return os.path.exists(chats_folder)
