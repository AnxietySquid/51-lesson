import logging
import os
from datetime import datetime

class AppLogger:
    """Класс для логирования работы приложения"""
    
    def __init__(self):
        
        # Создаем директорию для логов если её нет
        self.logs_dir = "logs"
        if not os.path.exists(self.logs_dir):
            os.makedirs(self.logs_dir)
            
        # Имя файла лога с текущей датой
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_file = os.path.join(self.logs_dir, f"chat_app_{current_date}.log")
        
        # Настраиваем форматирование
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Файловый обработчик
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        
        # Консольный обработчик
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # Настраиваем логгер
        self.logger = logging.getLogger('ChatApp')
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message: str):
        """Логирование информационного сообщения"""
        self.logger.info(message)
    
    def error(self, message: str, exc_info=None):
        """Логирование ошибки"""
        self.logger.error(message, exc_info=exc_info)
    
    def debug(self, message: str):
        """Логирование отладочной информации"""
        self.logger.debug(message)
    
    def warning(self, message: str):
        """Логирование предупреждения"""
        self.logger.warning(message)