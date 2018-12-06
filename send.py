from models.rabbit_wrapper import RabbitWrapper


rabbit_wrapper = RabbitWrapper()

message = {'first_name': 'Nik', 'last_name': 'S.'}

rabbit_wrapper.send_message(message)
