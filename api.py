# api.py
from flask import Blueprint, request, jsonify
from models import db, Event

api = Blueprint('api', __name__)

@api.route('/api/events', methods=['GET'])
def get_events():
    return jsonify([e.to_dict() for e in Event.query.all()])

@api.route('/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

@api.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(
        title=data['title'],
        start_time=data['start_time'],
        end_time=data['end_time'],
        description=data.get('description')
    )
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201

@api.route('/api/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    event.title = data['title']
    event.start_time = data['start_time']
    event.end_time = data['end_time']
    event.description = data.get('description')
    db.session.commit()
    return jsonify(event.to_dict())

@api.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return '', 204
