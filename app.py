from flask import Flask, jsonify, request

from database import engine, SessionLocal
from models import Base, Ticket

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

@app.route("/")
def home():

    return jsonify({
        "status": "Flask działa!"
    })

@app.route("/tickets", methods=["POST"])
def create_ticket():

    data = request.json

    db = SessionLocal()

    try:

        new_ticket = Ticket(
            priority=data["priority"],
            category=data["category"],
            sentiment=data["sentiment"],
            confidence=data["confidence"],
            ai_summary=data["ai_summary"]
        )

        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        return jsonify({
            "message": "Ticket created",
            "id": new_ticket.id,
            "status_code": 200
        }), 200

    except Exception as e:

        db.rollback()

        return jsonify({
            "error": str(e)
        }), 500

    finally:

        db.close()

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)