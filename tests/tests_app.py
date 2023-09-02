# Mengimpor modul yang diperlukan
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

# Inisialisasi virtual display untuk menjalankan browser tanpa GUI (headless)
display = Display(visible=0, size=(800, 800))
display.start()

# Menggunakan chromedriver_autoinstaller untuk menginstal ChromeDriver
chromedriver_autoinstaller.install()

# Konfigurasi opsi Chrome
chrome_options = webdriver.ChromeOptions()

# Daftar opsi yang ingin ditambahkan
options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
]

# Menambahkan opsi-opsi ke dalam chrome_options
for option in options:
    chrome_options.add_argument(option)

class TestLibraryapptesting():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_libraryapptesting(self):
    self.driver.get("http://localhost:5000/")
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Peminjaman Buku\')]").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'nama_peminjam\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'nama_peminjam\']").send_keys("rahil")
    self.driver.find_element(By.XPATH, "//input[@name=\'judul_buku\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'judul_buku\']").send_keys("python 101")
    self.driver.find_element(By.XPATH, "//input[@name=\'tanggal_peminjaman\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'tanggal_peminjaman\']").click()
    self.driver.find_element(By.XPATH, "//input[@name=\'tanggal_peminjaman\']").send_keys("2023-09-06")
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Pinjam Buku\')]").click()
    self.driver.find_element(By.XPATH, "//a[contains(@href, \'/\')]").click()
    self.driver.find_element(By.XPATH, "//a[contains(text(),\'Peminjaman Buku\')]").click()