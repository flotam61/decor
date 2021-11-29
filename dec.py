import datetime
import json


def decor_path(path):
    def decor(old_function):
        logi = {}
        def new_function(*args, **kwargs):
            argument = f'{args}{kwargs}'
            namefunction = old_function.__name__
            dt = datetime.datetime.today()
            result = old_function(*args, **kwargs)
            logi["Название функции"] = namefunction
            logi["Дата и время:"] = dt
            logi["Аргументы функции"] = argument
            logi["Возвращаемое значение"] = result
            with open(path, 'w', encoding="UTF-8") as file:
                json.dump(logi, file, indent=3, sort_keys=True, default=str, ensure_ascii=False)
            return logi
        return new_function
    return decor
