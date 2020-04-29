[![Build Status](https://travis-ci.org/elkrojo/croiglas-shop.svg?branch=master)](https://travis-ci.org/elkrojo/croiglas-shop)

# CroíGlas - Online Clothing Store

Project 4 - Full Stack Frameworks with Django (Code Institute 2020)        

**CroíGlas** is a clothing store presenting the best of what Irish fashion brands have to offer. Whether you are looking at preparing your wardrobe for the coming season or surprising a loved one with a thoughtful gift, here at **CroíGlas** you will surely find something to fit your need.

<br>

---

## Table of Contents

1. [Demo](#demo)
2. [UX](#ux)
3. [Features](#features)
4. [Information Architecture](#information-architecture)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

<br>

---

## Demo
Clicking on the image below will bring you to a live demo. Right click and select "Open link in new tab" to open the demo in a new browser tab.      

[![Main](https://raw.githubusercontent.com/elkrojo/croiglas-shop/master/static/img/presentation/demo-link.jpg)](https://croiglas-shop.herokuapp.com/)

<br>

[Back to Top](#table-of-contents)

---

## UX

**As a customer, I am looking for a shopping expereince that combines the following:**      

1. Presents products to me in a manner which is easy to digest, at first.
2. Provides critical information about the product at a glance.
3. Provides further detailed information about the product on inspection.
4. Provides a familiar and easy payment method.
5. Allows me to search for products which match my requirements.        


**As the business owner, I am looking for an e-commerce package which combines the following:**     

1. Instills a sense of confidence in the user initially, which keeps them browsing in the shop.
2. Presents the user with options which are easy to follow.
3. Presents the user with an easy checkout experience, with reassuring feedback messaging.      

<br>

### Strategy
The design is intuitive and easy to grasp. The options are clearly laid out, and products are presented following a familiar layout.

### Structure 
The shop is divided into two main sections. One section caters to Men, while the other section caters to Women. 
Upon selecting one of these options, only products in the selected category will be displayed to the user.

### Skeleton
[Desktop Wireframe](https://raw.githubusercontent.com/elkrojo/conjure/master/static/images/docu/conjure-desktop.jpeg)      
[Mobile Wireframe](https://raw.githubusercontent.com/elkrojo/conjure/master/static/images/docu/conjure-mobile.jpeg)

### Surface
The home page makes use of a cycling clickable image display with embedded buttons. 
Products are displayed in evenly spaced tiles, below which are clearly displayed information related to each tile.

<br>

[Back to Top](#table-of-contents)

---

## Features
 
### Existing Features

**Header** - presents users with the main account actions, alongside a search box.          

**Product Tiles** - shows users the products which fall into the main category selected.         

**Product Showcase** - presents users with a closer look at the selected product.             

**Account Registration Page** - can only be accessed by a user who is not currently logged in. User account is created on completion of registration form.           

**Account Login Page** - can only be accessed by a user who is not currently logged in. Login only possible on exact username|password or email|password combinations. Feedback messaging provided.     

**Account Profile Page** - allows users to enter their contact information. This information can be updated from the same page.     

**Account Logout Page** - will redirect the user back to the home page, while displaying a message indicatiing they have logged out.        

**Cart Page** - displays a table of contents showing what items are currently stored in the cart before checkout. Quantities can be updated before checkout.        

**Checkout Page** - shows customers a table of checkout items. Below is a checkout form and credit card payment form. Feedback provided alerting the customer on successful and unsuccessful payments.       

   
### Features Left to Implement

**Product Category Filtering** - would allow users greater control,displaying only products in one clothing category. *Jackets, Sweatshirts, Jeans, etc.*       

**Product Colour Filtering** - would allow users greater control, displaying only products in one colour. *Black, Green, Yellow, etc.* 

**Product Size Filtering** - would allow users greater control, displaying only products in one size category. *S, M, L, etc.* 

**Special Offers** - would allow users to see only products which are reduced in price.     

**New Arrivals** - would show customers products most recently added to the shop.       

**Contact Form** - would allow the user to contact a shop employee, whatever the purpose.      

<br>

[Back to Top](#table-of-contents)

---

## Information Architecture
### Database
[PostgreSQL](https://www.postgresql.org/) - The database chosen for this project is **PostgreSQL**, an open source relational database.       

### Data Structure

**Accounts App:**

**Customer**
| Id | Data Type | Validation
--- | --- | ---
id | int | auto-increment
user | onetoone(User) |
full_name | models.CharField | max_length=42
street_address_1 | varchar | max_length=32
street_address_2 | varchar | max_length=32
city | varchar | max_length=24
postcode | varchar | max_length=12
county | varchar | max_length=24
country | varchar |max_length=32
phone_number | varchar | max_length=16
<br>


**Products App:**

**GenderFilter**
| Id | Data Type | Validation
--- | --- | ---
id | int | auto-increment
category| varchar | max_length=1
<br>

**Product**
| Id | Data Type | Validation |
--- | --- | ---
id | int | auto-increment
person_category | foreignkey(GenderFilter) | blank=True, null=True, on_delete=models.SET_NULL
brand | varchar(6) | max_length=6, choices=BRAND_CHOICES, default='LABONE'
product_category | varchar(6) | max_length=6, choices=PRODUCT_CATEGORY_CHOICES, default='JACPAR'
title | varchar(100) | max_length=100, default='', blank=False
description | text | blank=False
size | varchar(3) | max_length=3, choices=SIZE_CHOICES, default='NA'
price | float8 | max_digits=6, decimal_places=2, blank=False
image | image |
quantity | int | default=1
<br>


**Checkout App:**

**Order**
| Id | Data Type | Validation
--- | --- | ---
id | int | auto-increment
full_name | varchar | max_length=50, blank=False
street_address_1 | varchar | max_length=40, blank=False)
street_address_2 | varchar | max_length=40, blank=False)
city | varchar | max_length=40, blank=False)
postcode | varchar | max_length=20, blank=True)
county | varchar | max_length=40, blank=False)
country | varchar | max_length=40, blank=False)
phone_number | varchar | max_length=20, blank=False)
date | date | 
<br>

**OrderLineItem**
| Id | Type |
--- | ---
id | int | auto-increment
order | foreignkey(Order) | null=False
product | foreignkey(Product) | null=False
quantity | int | blank=False


<br>

[Back to Top](#table-of-contents)

---

## Technologies Used
[Python3](https://www.python.org/) - The project uses **Python3** to build the backend data processing features.       

[Django 1.11](https://django-documentation.readthedocs.io/en/latest/index.html) - The project uses **Django1.11** as the web application framework.     

[JavaScript](https://en.wikipedia.org/wiki/JavaScript) - The project uses **JavaScript** to add dynamic stripe authentication at the checkout.      

[HTML5](https://en.wikipedia.org/wiki/HTML5) - The project uses **HTML5** to structure the page contents.     

[CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - The project uses **CSS3** to style the HTML elements.         

[Bootstrap3](https://getbootstrap.com/docs/3.3/) - The project uses **Bootstrap3** for consistent styling and responsive alignment of HTML elements.        

[JQuery](https://jquery.com) - The project uses **JQuery** to simplify DOM manipulation.       

[GitHub](https://github.com) - The project uses **GitHub** as a version control repository.

[AWS S3](https://aws.amazon.com/s3/) - The project uses **AWS S3** to host static files and media.      

[Stripe](https://stripe.com/) - The project uses **Stripe** to process credit card payments.        

[Travis CI](https://travis-ci.org) - The project uses **Travis CI** to run build tests throughout development.      

[Heroku](https://www.heroku.com) - The project uses  **Heroku** to host and serve the web application with database.        

<br>

[Back to Top](#table-of-contents)

---