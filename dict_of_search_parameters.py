from tkinter import BooleanVar


def create_dict_of_search_parameters ( ) -> dict[str, BooleanVar]:
	return {
            "200%": BooleanVar ( ),
            "знаков": BooleanVar ( ),
            "Иномир": BooleanVar ( ),
            "Жатвы": BooleanVar ( ),
            "Чаюле": BooleanVar ( ),
            "Делириум": BooleanVar ( ),
            "Священн": BooleanVar ( ),
            "зверей": BooleanVar ( ),
            "животных": BooleanVar ( ),
            "500%": BooleanVar ( ),
            "Альву": BooleanVar ( ),
            "уникальных монстров": BooleanVar ( ),
            "золоченый": BooleanVar ( ),
            "Джун": BooleanVar ( ),
            "8 свойств": BooleanVar ( ),
            "таинственный": BooleanVar ( ),
            "Алтари": BooleanVar ( ),
            "Легион": BooleanVar ( ),
            "преследуемых": BooleanVar ( ),
            "преслелуемых": BooleanVar ( ),
            "Ларцы": BooleanVar ( ),
            "Тайник": BooleanVar ( ),
            "Бездн": BooleanVar ( ),
            "Сущн": BooleanVar ( ),
            "телохра": BooleanVar ( ),
            "строительства": BooleanVar ( ),
            "Эйнар": BooleanVar ( ),
            "скверн": BooleanVar ( ),
            "редких": BooleanVar ( ),
            "волшебн": BooleanVar ( ),
            "гладк": BooleanVar ( ),
            "ваал": BooleanVar ( ),
            "неопознанных": BooleanVar ( ),
            "Нико": BooleanVar ( ),
            "встречаться": BooleanVar ( ),
            "катализаторы": BooleanVar ( ),
            "кражи": BooleanVar ( ),
            "Синдик": BooleanVar ( )
           }

# Если создать переменную со словарём, то вылезает ошибка,
# потому что BooleanVar должен чему-то принадлежать
# (окошку, например)
