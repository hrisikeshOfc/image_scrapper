import os
import time
from logger import logging
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import IMAGES_FOLDER

class ImageScraper:
    def __init__(self, search_input:str):
        self.search_input = search_input.strip().lower()
        self.base_dir = os.path.join(os.getcwd(),
                                     IMAGES_FOLDER, 
                                     self.search_input
                                      )
        
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
  
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 50)

    def _create_directory(self):
        os.makedirs(self.base_dir, exist_ok=True)
        logging.info(f"Created directory: {self.base_dir}")

    def _save_image(self, image_url, file_name):
        try:
            image_path = os.path.join(self.base_dir, file_name)
            response = request.urlopen(image_url)
            with open(image_path, 'wb') as f:
                f.write(response.read())
            logging.info(f"Saved image: {file_name}")
        except Exception as e:
            logging.error(f"Error saving image: {str(e)}")

    def scrape_images(self, num_images):
        self._create_directory()

        try:
            self.driver.get(f'https://www.google.com/search?q={self.search_input}&tbm=isch')
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'rg_i')))

            images = self.driver.find_elements(By.CLASS_NAME, 'rg_i')
            logging.info(f"Found {len(images)} images for {self.search_input}")

            while len(images) < num_images:
                # Scroll to load more images
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                images = self.driver.find_elements(By.CLASS_NAME, 'rg_i')
                logging.info(f"Loaded {len(images)} images")

            for index in range(num_images):
                image = images[index]
                image_url = image.get_attribute('src')
                file_name = f"{self.search_input}_{index}.png"
                self._save_image(image_url, file_name)

        except Exception as e:
            logging.error(f"Error scraping images: {str(e)}")

        finally:
            self.driver.quit()

