# =--------------------------------EMAIL collector----------------------------------------#
import re

str = '''Skip to main content
Global links iconYou are in Nestlé IndiaGlobal links dropdown
Contact us
Home
Search
Search
Home
About us
Our Stories
Our Businesses
Nestlé in society
Nutrition Health and Wellness
Careers
Investors
Media
Contact Us
Share this page

Corporate Office
Nestlé India Ltd.
Nestlé House, Jacaranda Marg M Block
DLF City Phase II, National Highway 8
Gurgaon 122 002, India

Important Emails
1.	Consumer Services	wecare@in.nestle.com

2.	Investor Relations	investor@in.nestle.com

3.	General Enquiries	communication@in.nestle.com

4.	Journalist Enquiries	ambereen.shah@in.nestle.com
shashank.nair@in.nestle.com
(with a CC to media.india@in.nestle.com)

5.	Exports	exports.enquiry@in.nestle.com

Important Phone Numbers
1.	Consumer Services	Toll Free Number:1800 103 1947
 	 	WhatsApp: 9717771947
2.	Nestlé Head Office	Tel: +91 124 238 93 00
 	 	Fax: +91 124 238 93 99
3.	Journalist Enquiries	Tel: +91 124 3321824 / 1275
MINI FOOTER
Nestlé News
Search our archive of news and press releases

Discover all the news
Compliance Concerns
Speak Up about your concerns

Speak Up
map
Contact us
Across the globe, Nestlé are here to help answer your queries

Contact us
Nestlé
We unlock the power of food to enhance quality of life for everyone, today and for generations to come

Nestlé
ABOUT US
All About Nestlé
Presence Across India
Research and Development
Our Websites and Social Media Presence
Trending Now
Report your concerns
GST for Business Partners
OUR STORIES
Our stories
NESTLÉ IN SOCIETY
Creating Shared Value
Individuals and Families
Communities
Planet
CSV Impact
Case Studies
BRANDS
Beverages
Breakfast Cereals
Chocolates and Confectionery
Dairy
Nutrition
Foods
Vending and Food Services
Imports
Exports
Nestlé Ad Campaigns
NUTRITION HEALTH AND WELLNESS
Healthy Living
Nutrition Basics
Understanding Food Labels
Family, fun and food
Myths and Tips
Nutrition, Health And Wellness @ Nestlé
INVESTORS
Directors and Officers
Key Figures
Analysts' Meet
Investor Services
Policies/Code of Conduct
Investor Information
MEDIA
Media Library
Events
Press Releases
Special Announcements
Statements
Media Contacts
Images
Videos
SHARE PRICE
CHF 112.38 (-1.46%)
follow us on
SUB FOOTER MENU'''

pattern = re.compile(r"[\w.$#!%^&*]+@[\w.]+")

matches = pattern.findall(str)

for match in matches:
    print(match)

with open('emailContacts.txt', 'w') as f:
    for match in matches:
        f.write(f"{match}\n")
