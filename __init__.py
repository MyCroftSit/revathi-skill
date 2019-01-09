from mycroft import MycroftSkill, intent_file_handler


class Revathi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('revathi.intent')
    def handle_revathi(self, message):
        self.speak_dialog('revathi')


def create_skill():
    return Revathi()

