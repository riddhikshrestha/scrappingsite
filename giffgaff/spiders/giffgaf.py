# -*- coding: utf-8 -*-
import scrapy
import csv

nickname = 'Ravetoom'
password = 'mathew76'

class GiffgafSpider(scrapy.Spider):
    name = 'giffgaf'
    allowed_domains = ['www.giffgaff.com']
    start_urls = ['https://www.giffgaff.com/auth/login']
    output = "output.csv"

    def __init__(self):
        open(self.output,"w").close()

    def parse(self, response):
        # nickname = 'Ravetoom'
        # password = 'mathew76'
        token = response.xpath('.//*[@name="login_security_token"]/@value').extract_first()
        # print(token)
        # print('hello world')
        yield scrapy.FormRequest('https://www.giffgaff.com/auth/login',formdata={'login_security_token':token,'nickname': nickname,'password':password},callback=self.startscraping)

    def startscraping(self,response):
        yield scrapy.Request('https://www.giffgaff.com/dashboard',callback=self.verifylogin)

    def verifylogin(self,response):
        # print(response.text)
        
        # print(response.css("title::text")[0].extract())
        # print(response.css("title::text").extract_first())   # For not error  
        # print(response.css("h2.profile-phone-number::text").extract_first())
        # print('Username is :'+nickname +' Password is: '+password)

        with open(self.output,"a",newline="") as f:
            writer = csv.writer(f)
            phonenumber = response.css("h2.profile-phone-number::text").extract_first()
            writer.writerow([nickname,password,phonenumber])
            yield {'uname':nickname,'password':password,'phone':phonenumber}

        

        
        
        

