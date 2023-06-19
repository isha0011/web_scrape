from selenium.webdriver.common.by import By
import pandas as pd



class Scrapper:
    def __init__(self, driver):
        self.driver_class = driver
        pd.set_option('display.max_columns', None)

    def scrape_section(self, section_number):
        list_of_topic = []
        list_of_title = []
        list_of_price = []
        j = 1

        a = self.driver_class.find_element(f"/html/body/main/section[{section_number}]/div/div/div[1]/h2")

        while j <= 8:
            title = self.driver_class.find_element(
                f"/html/body/main/section[{section_number}]/div/div/slider-component/ul/li[{j}]/div/div/div[2]/div[1]/h3")
            price = self.driver_class.find_element(
                f"/html/body/main/section[{section_number}]/div/div/slider-component/ul/li[{j}]/div/div/div[2]/div[1]/div/div/div/div[2]/span[4]")
            list_of_title.append(title.text)
            list_of_price.append(price.text)
            list_of_topic.append(a.text)
            j = j + 1

        section_list = pd.DataFrame(
            {'Category': list_of_topic,
             'Book_name': list_of_title,
             'Price': list_of_price
             })

        return section_list

    def display_all(self):
        a = self.scrape_section(2)
        b = self.scrape_section(3)
        c = self.scrape_section(4)
        merge_list = [a, b, c]
        # print(merge_list)
        merge = pd.concat(merge_list)
        # print(merge)
        # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #     print(merge)
        return merge

    def scroll(self, xpath):
        sc = self.driver_class.find_element(xpath, By.XPATH)
        return self.driver_class.execute_script("arguments[0].scrollIntoView();", sc)
