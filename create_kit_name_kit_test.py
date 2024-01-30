import data
import sender_stand_request


# Запрос тела (имя созданного набора)
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


#   Позитивные проверки
def positive_assert(name):
    kit_body_positive = get_kit_body(name)
    kit_response_positive = sender_stand_request.post_new_kit(kit_body_positive)
    assert kit_response_positive.json()["name"] == name
    assert kit_response_positive.status_code == 201


#   Негативные проверки (с именем)
def negative_assert(name):
    kit_body_negative = get_kit_body(name)
    kit_response_negative = sender_stand_request.post_new_kit(kit_body_negative)
    assert kit_response_negative.status_code == 400


#   Негативные проверки (без имени)
def negative_assert_no_name(kit_body):
    kit_response_negative_no_name = sender_stand_request.post_new_kit(kit_body)
    assert kit_response_negative_no_name.status_code == 400
    assert kit_response_negative_no_name.json()["code"] == 400
    assert kit_response_negative_no_name.json()["message"] == "Не все необходимые параметры были переданы"


# 1 Допустимое количество символов (1)
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")


# 2 Допустимое количество символов (511)
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# 3 Количество символов меньше допустимого (0)
def test_create_kit_0_symbol_in_name_get_error_response():
    negative_assert("")


# 4 Количество символов больше допустимого (512)
def test_create_kit_512_symbols_in_name_get_error_response():
    negative_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd" \
            "abcdabcdabcdabcD")


# 5 Разрешены английские буквы (QWErty)
def test_create_kit_english_symbols_in_name_get_success_response():
    positive_assert("QWErty")


# 6 Разрешены русские буквы (Мария)
def test_create_kit_russian_symbols_in_name_get_success_response():
    positive_assert("Мария")


# 7 Разрешены спецсимволы (№%@)
def test_create_kit_special_symbols_in_name_get_success_response():
    positive_assert("№%@")


# 8 Разрешены пробелы ( Человек и КО )
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# 9 Разрешены цифры (123)
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# 10 Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    current_kit_body_negative_no_name = data.kit_body.copy()
    current_kit_body_negative_no_name.pop("name")
    negative_assert_no_name(current_kit_body_negative_no_name)


# 11 Передан другой тип параметра (число)
def test_create_kit_numeric_type_in_name_get_error_response():
    negative_assert(123)
    