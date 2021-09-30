from mycroft import MycroftSkill, intent_file_handler


class Piot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('piot.intent')
    def handle_piot(self, message):
        self.speak_dialog('piot')


def create_skill():
    return Piot()

