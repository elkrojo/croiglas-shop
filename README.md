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
[Desktop Wireframe](https://raw.githubusercontent.com/elkrojo/croiglas-shop/master/static/img/presentation/croiglas-shop-desktop.jpg)      
[Mobile Wireframe](https://raw.githubusercontent.com/elkrojo/croiglas-shop/master/static/img/presentation/croiglas-shop-mobile.jpg)

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

**Shipping** - would present the shipping cost to a user depending on their location.

**Shipping Address Toggle** - would allow the user to import their billing address in the event that it is the same as the shipping address for the current order.

**Previous Shipping Address** - would allow the user to select a shipping address from a previous order.

**Purchase Confirmation Email** - would sent a copy of the checkout receipt to the customer following a successful payment.

<br>

[Back to Top](#table-of-contents)

---

## Information Architecture
### Database
[PostgreSQL](https://www.postgresql.org/) - The database chosen for this project is **PostgreSQL**, an open source relational database.       

### Data Structure

**Accounts App:**

**BillingAddress**
| Id | Data Type | Modifiers
--- | --- | ---
id | int pk | auto-increment
user | onetoone(User) |
full_name | models.CharField | max_length=42
street_address_1 | varchar | max_length=32
street_address_2 | varchar | max_length=32
city | varchar | max_length=24
postcode | varchar | max_length=12
county | varchar | max_length=24
country | varchar |max_length=32
phone_number | varchar | max_length=16

>*Note: Billing address is not always the same as the shipping address for an order, and as such requires its own database table.*

<br>

**Products App:**

**GenderFilter**
| Id | Data Type | Modifiers
--- | --- | ---
id | int pk | auto-increment
category| varchar | max_length=1
<br>

**Product**
| Id | Data Type | Modifiers
--- | --- | ---
id | int pk | auto-increment
person_category | foreignkey(GenderFilter) | blank=True, null=True, on_delete=models.SET_NULL
brand | varchar | max_length=6, choices=BRAND_CHOICES, default='LABONE'
product_category | varchar | max_length=6, choices=PRODUCT_CATEGORY_CHOICES, default='JACPAR'
title | varchar | max_length=100, default='', blank=False
description | text | blank=False
size | varchar | max_length=3, choices=SIZE_CHOICES, default='NA'
price | float8 | max_digits=6, decimal_places=2, blank=False
image | image |
quantity | int | default=1
<br>


**Checkout App:**

**Order**
| Id | Data Type | Modifiers
--- | --- | ---
id | int pk | auto-increment
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
| Id | Data Type | Modifiers
--- | --- | ---
id | int pk | auto-increment
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

## Testing

| Objective | Observation | Outcome
| --- | --- | ---
| Click header logo, return to home page. | Redirects to home page. | Successful
| Click register button, load register form page. | Registration form page loads. | Successful
| Enter invalid registration form field data, try to create account, receive browser prompt. | Browser highlights invalid form field data. | Successful
| Enter valid registration form field data, try to create account, receive success message and log user in. | Message displayed, user logged in. | Successful
| Click profile button, load profile info form page. | Profile form page loads. | Successful
| Enter incomplete profile form field information, update profile, receive browser prompt. | Unfilled fields are highlighted by the browser. | Successful
| Enter complete profile form field information, update profile, receive confirmation message. | Profile information is updated and stored, confirmation message received. | Successful
| Change any profile form field information, update profile, receive confirmation message. | Profile information is updated and stored, confirmation message received. | Successful
| Click log out button, receive confirmation message, return to home page | Browser returns to home page, confirmation message received | Successful
| While logged out - Click log in button, click forgot passwrod button, enter email address, receive password reset instructions email. | Email sent from shop address with password reset instructions. | Successful
| Click shop men on home page, filter and display products accordingly | Only products for men are displayed | Successful
| Click shop women on home page, filter and display products accordingly | Only products for women are displayed | Successful
| Add any number of products to the cart, observe header cart icon updating | Cart icon shows number of cart items | Successful
| Click cart button, load cart page, display cart contents table | Cart page loads, cart contents table displayed | Successful
| Update quantity of cart item, click refresh button, cart header icon quantity updates, cart total is updated accordingly | Header icon updates, Cart toatl is updated accorgingly | Successful
| Click continue shopping button, return to home page | Browser returns to home page | Successful
| While logged out - Click checkout button, redirect to page requiring user to log in | Login page is loaded | Successful
| While logged in - Click checkout button, load checkout page | Checkout page loads | Successful
| Enter incomplete payment details form field information, submit payment, receive browser prompt. | Unfilled fields are highlighted by the browser. | Successful
| Enter invalid credit card expiration date, reject payment, receive browser alert message | Payment rejected, message displayed accordingly | Successful
| Enter valid credit card expiration date, accept payment, return to homa page, receive success message in browser | Home page loads, success message is displayed | Successful
| Click search button in header, header expands with search box | Header expands vertically, search box appears | Successful
| Search for product not featured in shop, remain on current page, receive error message in browser | Browser redirects to home page, no error message displayed | Unsuccessful
| Search for product featured in shop, filter products containing the search term, display those products | Products page loads, products matching search term are displayed | Successful

<br>

### Browser Compatibility       

The site was tested on multiple browsers (Chrome, Firefox, Brave, Safari) and on a few portable devices (iPhone 5s: Safari, iPad: Safari) to assess compatibility and responsiveness.      

<br>

[Back to Top](#table-of-contents)

---

## Deployment

The live demo site is hosted on Heroku and deployed using the latest master branch version of this Git repository.       

**The order of events for deployment:**     

1. Click "Create new app" on Heroku dashboard. Choose a name, select a region, create app.      
2. Click "Resources" tab. Under Addd-ons, search for "postgres" and select "Heroku Postgres". Select "Hobby Dev - Free" and click Provision buton.      
3. Click "Settings" tab. Reveal config vars and copy DATABASE_URL value.     
4. Store database value as variable in env.py. Use the DATABASE_URL variable in settings.py when connecting your project to Heroku PostgreSQL database using dj_database_url.       
5. Once connected, configure the PostgreSQL database to match your projects models. `python3 manage.py makemigrations`, `python3 manage.py migrate`.        
6. Copy all project variables from env.py and copy to heroku app config vars (except for DATABASE_URL, which is already present).       
![Config Vars](https://raw.githubusercontent.com/elkrojo/croiglas-shop/master/static/img/presentation/config-vars.jpg)
7. Install gunicorn in Django project to facilitate a heroku deployment. Use gunicorn command within Procfile declaration.      
8. In Heroku config vars, set DISABLE_COLLECTSTATIC = 1. This will prevent Heroku from serving static files.        
9. Once you have pushed a good working version of the project to GitHib, click "Deploy" tab and select "Deploy Branch".     
10. Once the app is deployed, copy the url and add it to Django project "ALLOWED_HOSTS" in settings.py.     
11. Now push the latest version of the app to GitHub, and deploy again to secure access.        
12. In settings.py, add a conditional statement which sets debug mode relative to the presence of env.py file.      
    ```python
    if os.path.exists('env.py'):
        import env
        DEBUG = True
    else:
        DEBUG = False
    ```

To run the code in this project locally, you can clone the full contents of the repository. In your terminal, 
navigate to the directory you want the repository located and enter the following command:
 
    git clone https://github.com/elkrojo/croiglas-shop.git

Once cloned, you can remove all connection to the source repository using the command:

    git remote rm origin

before you can run the project locally, you will first need to install the packages for the environment to access.

1. `pip3 install requirements.txt`

This app has been developed using private keys to access the PostgeSQL Database, AWS S3 Bucket and Stripe Backend.      

<br>

[Back to Top](#table-of-contents)

---

## Credits

### General Appearance
The site is inspired in part by [Carhartt WIP](https://www.carhartt-wip.com/en)

### Images
All images are free from copyright and sourced from [Pexels](https://www.pexels.com)

All content is intended **for educational use only**.

<br>

[Back to Top](#table-of-contents)

---
