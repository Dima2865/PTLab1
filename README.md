# Лабораторная 1 по дисциплине "Технологии программирования"

Вариант 4

Индивидуальное задание
1. Выберите для Вашего проекта тип лицензии и добавьте файл с лицензией в проект.
2. Добавьте в проект файл .gitignore и сформируйте его содержимое.
3. Добавьте в проект еще один класс – наследник класса DataReader, который должен
обрабатывать входной файл определенного формата (согласно индивидуальному варианту, см. 
таблицу). Составьте модульные тесты для методов этого класса, постарайтесь покрыть тестами 
максимально возможный объем кода. Для работы с этим заданием создайте новую ветку кода на основе 
главной и фиксируйте в нее весь программный код в процессе разработки. Добейтесь выполнения всех 
тестов проекта, после чего объедините текущую ветку кода с главной.
4. Добавьте в проект класс, реализующий расчет определенных характеристик студентов 
(согласно индивидуальному варианту, см. таблицу). Составьте модульные тесты для методов этого 
класса, постарайтесь покрыть тестами максимально возможный объем кода. Для работы с этим 
заданием создайте новую ветку кода на основе главной и фиксируйте в нее весь программный код в 
процессе разработки. Добейтесь выполнения всех тестов проекта, после чего объедините текущую 
ветку кода с главной.
5. Составьте UML-диаграмму классов итогового проекта.
6. Проанализируйте полученные результаты и сделайте выводы.

![image](https://github.com/user-attachments/assets/25414669-721e-49e9-8ac5-fb7c138aacac)
![image](https://github.com/user-attachments/assets/92ebec37-ab98-4f69-9b9f-d1b83afbdb7e)

C:\Users\d222a\University\Technologii programmirovania\TP_lab_1_git

pycodestyle.exe src test

$env:PYTHONPATH = "./;./src"

pytest.exe test

python.exe src\main.py -p data\data.txt
