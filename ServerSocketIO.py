from asyncio.windows_events import NULL
from socket import socket
from flask import Flask, render_template, redirect, request, session
from flask.globals import request
from flask_socketio import SocketIO, emit, rooms,send
from flask_socketio import join_room, leave_room
from Paddle_ocr import ocr as ocr
from Paddle_ocr.b64 import base64_pil 
from flask import g
import cv2
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.FATAL)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('client:OCR_request')
def OCR_request(data):
    id = request.sid
    print('here')
    image1 = base64_pil(data['image_base64'])
    response = ocr.get_words(image1)
    print(response)   
    socketio.emit('OCR Server: Response', response , room = id ) 
    
if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',debug=True, port=5000)
    # id = request.sid
    # print('here')
    # image1 = cv2.imread("C:\\CV-project\\Paddle_ocr\\imgs_en\\ascsac.jpg",cv2.IMREAD_COLOR)
    # response = ocr.get_words(image1)
    # print(response)   
    # socketio.emit('OCR Server: Response', response , room = id ) 






