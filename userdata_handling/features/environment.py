from behave.log_capture import capture


def before_all(context):
    """Perform setup before the first event."""
    print("Context: ", context)
    print("Userdata: ", context.config.userdata)
    print("x=", context.config.userdata["x"])
    print("y=", context.config.userdata["y"])
