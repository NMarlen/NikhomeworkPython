import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """
    Фикстура для инициализации WebDriver.

    Создаёт экземпляр браузера Chrome в headless-режиме,
    настраивает неявное ожидание и корректно завершает работу
    после выполнения теста.

    Returns:
        Generator[WebDriver, None, None]: генератор, который даёт WebDriver
        и выполняет финализацию после теста.
    """
    options = Options()
    options.add_argument("--headless")

    service = Service()
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.implicitly_wait(10)

    yield driver_instance

    driver_instance.quit()
