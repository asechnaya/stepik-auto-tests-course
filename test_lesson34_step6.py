import pytest


@pytest.fixture(scope="class") # выполнится-то она один раз для всего класса, но если мы внутри теста
# хотим как-то использовать значение которое фикстура возвращает, надо передавать в каждую функцию в классе
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)  # autouse=True, который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        print("\n")
        pass

    def test_second_smiling_faces(self, prepare_faces):
        print("\n")
        pass