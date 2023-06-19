from base_class import Driver
from scrape import Scrapper
from database import *
from configs import config


def main():
    driver_class = Driver()
    driver_class.url_get(config.url)
    scrape_class = Scrapper(driver_class)
    db_class = Database()
    driver_class.scroll("/html/body/main/section[2]/div/div/div[1]/h2")
    df = scrape_class.display_all()
    db_class.create_table()
    # db_class.insert_table(df)
    db_class.insert(df)


if __name__ == "__main__":
    main()
