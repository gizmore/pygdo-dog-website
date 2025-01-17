from gdo.base.GDO_Module import GDO_Module


class module_dog_website(GDO_Module):
    """
    The Dog Chatbot Website
    """
    def gdo_is_site_module(self) -> bool:
        return True

    def gdo_dependencies(self) -> list:
        return [
            'blackjack',
            'bootstrap5',
            'chatgpt4o',
            'contact',
            'discord',
            'irc',
            'login',
            'math',
            'perf',
            'register',
            'slapwarz',
            'telegram',
        ]
