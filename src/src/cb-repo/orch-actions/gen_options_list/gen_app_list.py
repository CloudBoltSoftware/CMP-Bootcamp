def get_options_list(field, control_value=None, control_value_dict=None, **kwargs):
    options = []

    if not control_value and not control_value_dict:
        return options

    if control_value == "Database":
        options = ["PostgreSQL", "MySQL"]
    elif control_value == "Messaging Server":
        options = ["RabbitMQ", "Kafka"]
    elif control_value == "Web Server":
        options = ["Apache", "Nginx"]

    return {
        "options": options,
        "override": True,
        "sort": True
    }
