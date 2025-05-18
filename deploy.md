### Краткая инструкция по развертыванию Flask-приложения на удаленном сервере:

1. **Создать папку `venv` на сервере**:  
   ```bash
   mkdir venv
   ```

2. **Скопировать файлы проекта на сервер**:  
   ```bash
   scp -P ssh_port -r C:\my_path my_user@host_ip:~/venv/
   ```

3. **Перейти в папку проекта и создать виртуальное окружение**:  
   ```bash
   cd ~/venv/swarm_app
   python3 -m venv venv
   ```

4. **Активировать виртуальное окружение**:  
   ```bash
   source venv/bin/activate
   ```

5. **Установить Flask**:  
   ```bash
   pip install flask
   ```

6. **Запустить приложение**:  
   ```bash
   python swarm_app.py
   ```

7. **Доступ к приложению**:  
   Откройте в браузере:  
   ```http
   http://host_ip:5011
   ```

Готово! Flask-приложение запущено на сервере. 🚀
