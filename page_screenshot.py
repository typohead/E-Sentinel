from selenium import webdriver
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image
chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def screenshot_fullpage(url):


    driver=webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    page_height= driver.execute_script("return Math.max(document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight);")
    page_width= 1920
    # print(page_width)
    # driver.execute_script(script_for_normal_page)
    driver.set_window_size(page_width,page_height)
    # body=driver.find_element(By.TAG_NAME,"body")
    # body.screenshot("test.png")
    screenshot = driver.get_screenshot_as_png()
    driver.quit()


    # Save the image in memory to a BytesIO buffer
    image = Image.open(BytesIO(screenshot))
    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    # image.show()
    # Seek to the beginning of the buffer
    image_buffer.seek(0)
    return image


# screenshot_fullpage("https://www.flipkart.com/home-kitchen/home-appliances/fans/~cs-4xk309rwd0/pr?sid=j9e%2Cabm%2Clbz&p%5B%5D=facets.bee_energy_rating%255B%255D%3D5%2BStar&p%5B%5D=facets.bee_energy_rating%255B%255D%3D3%2BStar&otracker=clp_banner_2_14.bannerX3.BANNER_tvs-and-appliances-new-clp-store_8L5IFQEWUHMO&fm=neo%2Fmerchandising&iid=M_ef82ea20-2dec-4b36-8152-ea3250a8f27e_14.8L5IFQEWUHMO&ppt=hp&ppn=homepage&ssid=smu4tk7t000000001706135535307")
