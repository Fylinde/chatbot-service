import pika
import json
import logging
from sqlalchemy.exc import IntegrityError
from app.database import SessionLocal
from app.models.chatbot_user import ChatbotUserModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def user_callback(ch, method, properties, body):
    user_data = json.loads(body)

    # Log the received message
    logger.info(f"Received user_created event from RabbitMQ for user_id: {user_data['id']}")

    # Save user to the local database
    db = SessionLocal()
    try:
        # Check if the user already exists
        existing_user = db.query(ChatbotUserModel).filter(ChatbotUserModel.id == user_data["id"]).first()
        if existing_user:
            logger.info(f"User with id {user_data['id']} already exists in chatbot_users. Skipping insertion.")
        else:
            user_obj = ChatbotUserModel(
                id=user_data["id"],
                username=user_data["username"],
                email=user_data["email"],
                hashed_password=user_data["hashed_password"],
                profile_picture=user_data.get("profile_picture"),
                preferences=user_data.get("preferences"),
            )
            db.add(user_obj)
            db.commit()
            # Log user addition inside the session
            logger.info(f"User added in chatbot-service: {user_obj.username} (ID: {user_obj.id})")
    except IntegrityError as e:
        logger.error(f"Integrity error occurred while adding user: {str(e)}")
        db.rollback()
    except Exception as e:
        logger.error(f"Failed to add user: {str(e)}")
        db.rollback()
    finally:
        db.close()

def start_user_consuming():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    # Declare the fanout exchange
    channel.exchange_declare(exchange='user_events', exchange_type='fanout')

    # Declare a queue for chatbot-service and bind it to the exchange
    queue_name = channel.queue_declare(queue='', exclusive=True).method.queue
    channel.queue_bind(exchange='user_events', queue=queue_name)

    channel.basic_consume(
        queue=queue_name, on_message_callback=user_callback, auto_ack=True
    )

    logger.info('Waiting for user messages. To exit press CTRL+C')
    channel.start_consuming()
