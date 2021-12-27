# [MPT GYM]()

MPT Gym is a website and Ecommerce site for a personal training company.  It was created for a milestone project 4 as part of Code Insitute’s full stack development course.

This fully interactive and responsive website was build and developed using HTML, CSS, Python on a Django framework with a little JavaScript thrown in.

View this project live here

[]()
View the site: [MPT GYM](https://ms4-mpt-gym.herokuapp.com/)

## Table of Content

- [UX Design](#ux-design)
    - [Strategy](#strategy)
    - [Goals](#goals)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Typography](#Typography)
    - [Color Scheme](#color-scheme)
    - [Image](#image)
- [Features](#features)
    - [Layout](#layout)
    - [Features to implement in the future](#features-to-implement-in-the-future)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Acknowlegements](#acknowlegements)
    - [Inspiration from website](#Inspiration-for-website)
    - [Code](#code)

# UX

## Strategy

As a personal trainer I wanted to build a fictional personal training website and build also add an Ecommerce store to allow extra company to sell personal trainer package and well as giving the company’s client base the opportunity to purchase products that the company promote.

## Goals

#### Owner goal

- To increase a online presence
- To drive and connect to there members
- To convert new customer
- To add a new way of build revenue in the company
- 

#### User goals

- To access the company’s site across different devices.
- To find a gym or personal trainer in their citys or towns.
- To buy products/services from the company without having to the premises.
- To contact the gym with questions.

## **User stories:**

- **Website experience**

    - Would like a easily site to navigate and easily to understand what the user is looking at or for.
    - Would like a responsive website that can be access on different devices.

-  **Club / Personal Trainer experience**

    - Would like to read about the clubs information and personal trainer work a specific club.
    - Would like to read about the personal trainer specialty and contact information.
    
- **Shopping experience**

    - Would like to have a overview on the product on offer.
    - Would like to sort product out by specific list.
    - Would like to view product by category and specific request to find things I'm looking for.
    - Would to view basic information about the product about click on a item.
    - World like to get further information about the product once I click on the item.
    - Would like to select quantity of the item I would like to order.

- **Checkout and shopping bag experience**

    - Would like to reveiw my bag items to change or adjust as needed.
    - Would like to see the overall grand total of my shopping bag.
    - Would like a safe and secure way to enter payment information with it easy to follow and understand.
    - Would like a way to safe my payment detail to make my next purchase quick and easy.
    - Would like to receive a confirmation on my purchase order.

- **Contact**

    - Would like a way to contact the owner of the site to make queries or inquiry from orders to question about personal trainer / clubs.

- **Registratinon and Profile**

    - Would like to register for an account to save my payment details safely and securly.
    - Would like my to edit my profile page to keep my contact information up to date.
    - Would like to login and out of my profile safley.
    - Would like a way to reset my password if I forgot my password.
    - Would like to review my order history.
    
- **Site Management**

    - Would like to add item to the site collection.
    - Would like to edit individual item to keep the website up to date.
    - Would like to delete specialty item that will no longer be available on the site.
    
## Scope

- Responsive interface.
- Simple menu.
- Simple search function.
- Display search results.
- Login and sign up page.
- A user dashbroad.
- Display club / personal trainer / product
- Display shopping cart
- Update / remove quantites for item in cart
- Add / edit delivery information 
- Add / edit / delete function of products
- A way to contact owner.
- Log out

#### **Functional requirement for the platform.**

- Sign up form with email address and password.
- Be able to login
- Be able to view profile page / dashboard.
- Able to run search events by using keywords.
- Display product.
- Be able to add / edit / delete a products.
- To be able to create/view/edit/delete shopping bag.
- To be able to process order and payments.
- To be able to store images of products added to collection.
- Able to contact owner.
- Page 404 Not Found.
- Page 500 Internal Server Error page.

#### **Functional requirement for the platform.**

- To message personal trainer through your profile page.
- To keep track of your personal trainer / massage session clips.
- To be able to have your personal trainer load your workout program to your profile.
- Admin management to update workout class schedule.

## Building Constraints

- The owner is building the site for the first time and is still learning Python, Django. The lack of knowledge could hinder me from fulfilling the owners overall look and features on this platform.
- Lack of time: to implement features due to learning new technical skills. Full time work and two kids (one being 8 months).
 
## Structure

- Header: Search function, logo and account icon and bag icon.
- Navbar: navigational links with collapsible menu.
- Homepage: Hero image, information about the company, sign up button and find a trainer.
- Club page: Display clubs details and personal trainer working at each club.
- Product page: Display item on the site.
- Shopping bag: Display item that are/added to the bag.
- Checkout page: Display item, the form to buy items.
- Footer: Links to social media and Copyright.

### Database structure

Project using SQLite for deveploment and then Postgres when Hosted by Heroku.  This is first draft for the project.

[structure-first-look]()

# Design

### Wireframes

I used mockup [mockflow.com](https://www.mockflow.com/) 

![Homepage](documentation/design/wireframes/home-page.jpg)
![Clubpage](documentation/design/wireframes/club-page.jpg)
![Clubpage](documentation/design/wireframes/club-detail-page.jpg)
![Productpage](documentation/design/wireframes/product-page.jpg)
![Productpage2](documentation/design/wireframes/product-detail-page.jpg)


- [Wireframes Download PDF](documentation/design/wireframes/home-page.pdf)
- [Wireframes Download PDF](documentation/design/wireframes/club-page.pdf)
- [Wireframes Download PDF](documentation/design/wireframes/club-detail-page.pdf)
- [Wireframes Download PDF](documentation/design/wireframes/product-page.pdf)
- [Wireframes Download PDF](documentation/design/wireframes/product-detail-page.pdf)
- [Wireframes Download PDF]()

### Database Structure

A pdf version of the feature trade-off can been see [here](documentation/design/database-structure/db-database-excel.pdf)

A pptx version of the feature trade-off can been see [here](documentation/design/database-structure/db-database.pptx)

![Database-design-1](documentation/design/database-structure/db-database-1.png)
![Database-design-2](documentation/design/database-structure/db-database-2.png)
![Database-design-3](documentation/design/database-structure/db-database-3.png)


### Typography

[Google Fonts](https://fonts.google.com/)

### Color Scheme

![Colour Scheme](documentation/design/design-structure/colours.png)

### Image

Image details and information about the image can be found here in [this document](documentation/feature-images/image.md).



# Features

- #### Landing Page or menu

- #### Login / Sign Up page

- #### Log Out

- #### Profile page

- #### CRAD Features

- #### Footer

- ### Future Features

# Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) 
    - used to structure the page.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) 
    - used to add style and look of the page.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript) 
    - used to build interactive elements of the website/page.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python is an interpreted high-level general-purpose programming language.

# Database

- [db.sqlite3](https://www.sqlite.org/index.html)
    - A SQLITE3 file is a database file stored in the SQLite 3 format. It contains structured data records, which contain data types and values. SQLITE3 files are often used for storing embedded SQL-based databases for iPhone apps and other mobile applications.
- [Postgres](https://www.postgresql.org/)
    - PostgreSQL also known as Postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance.

# Technologies, Libraries and Frameworks Used

- [Bootstrap 5:]()
    - to help build the layout of the page with the use of the library.
- [Font Awesome:](https://fontawesome.com/) 
    - a library full of icons.
- [Google Fonts:](https://fonts.google.com/)
    - a library full of fonts.
- [Jquery:](https://en.wikipedia.org/wiki/JQuery) jQuery is a fast, small, and feature-rich JavaScript library.
- [Git:](https://git-scm.com/) 
    - Version control from gitpod, save, commits, and push code to Github.
- [GitHub:](https://github.com/)
    - Live site to save code.
- [GitPod:](https://www.gitpod.io) 
    - Local repository to read the develop code.
- [Heroku](https://www.heroku.com/home)
    - Heroku is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007
- [Django](https://www.djangoproject.com/)
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- [Amazon Web Services (AWS)](https://aws.amazon.com)
    - AWS (Amazon Web Services) is a comprehensive, evolving cloud computing platform provided by Amazon.
- [Amazon Web Services S3](https://aws.amazon.com)
    - Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
- [Amazon Web Services IAM](https://aws.amazon.com)
    - Identity and access management (IAM) is a framework of business processes, policies and technologies that facilitates the management of electronic or digital identities.
- [Stripe](https://stripe.com/en-gb-se)
    - Stripe is an online payment processing and credit card processing platform for businesses. When a customer buys a product online, the funds need to be delivered to the seller; Insert Stripe. Stripe allows safe and efficient processing of funds via credit card or bank and transfers those funds to the sellers account.
- [mockflow.com](https://www.mockflow.com/) 
    - Used to design my wireframes.
- [DB Diagram](https://dbdiagram.io/home)
    - Database diagrams graphically show the structure of the database and relations between database objects. You can generate a diagram for a data source, a schema, or a table. To create relations between database objects, consider using primary and foreign keys
- [W3C CSS Validator](https://validator.w3.org) 
    - Used to check of errors in HTML code.
- [W3C HTML Checker](https://validator.w3.org)
    - Used to check of errors in CSS code.
- [Am I responsive](http://ami.responsivedesign.is) 
    - is a high fidelity responsive design tool for previewing your site across a variety of popular devices.
- [W3C Spell Checker](https://www.w3.org/2002/01/spellchecker) 
    - This tool allows you to check the spelling of a web page.
- [Chrome Development Tools](https://developer.chrome.com/docs/devtools/)
    - Web developer tools built directly into the Google Chrome browser. To help developers diagnose problems as they work on projects.
- [Responsive viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) 
    - To test your website responsiveness across different devices.
- [Wave Accessibility](https://wave.webaim.org) 
    - helps you make their web content more accessible to different people with disabilities.
- [Google lighthouse](https://developers.google.com/web/tools/lighthouse) 
    - Check your site Performance, Accessibility, Best Practices, and SEO and give it a rating out of a 100.

### Media

- [figma](https://www.figma.com) 

# Testing User Stories

- ## User Stories Testing can be read [here]().

# Testing

- ## Testing process can be read [here](documentation/testing/testing.md).

# Deployment

Repository is hosted on Github and deployed on Heroku. I developed the website using the Code Institute template on Gitpod, and push to GitHub by the uses of the Gitpod terminal.

### Other platforms used

- An account with Heroku.

## Cloning the Project

When you finish logging into Github, navigate to the repository page, and select MS3-recipes. Above the file list, click on the Code button next to the Gitpod button (green button). Copy the URL. Open your terminal. Change the working directory to the location where you want the cloned directory. Paste the URL after you have type git clone. eg $ git clone https://github.com/Username/repository-name Press enter and this will create a local clone.

Or 

## Download zip files

Create a repository in GitHub. Unzip the folder Upload the files into your workspace You can read more about this in the link below.

More information on cloning repository:
[Github Information](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

![github1](documentation/deployment/GitHub-2.png)

## Forking the Project

When you finish logging into Github, navigate to the repository page, and select MS3-MPT-Recipes. At top right of the page click on the fork button.

More information on fork repository:
[Github Information](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

![github2](documentation/deployment/GitHub-1.png)

## Set up the local environment

## Procfile and Requirements.txt

- We need to make a list of all the Python dependencies for the project which can be done in the command line by creating a file "requirements.txt.

``$ pip freeze > requirements.txt`` 

- When we deploy to Heroku we need a specific file that lets Heroku know how to run the project and this is done in the command line also by creating a Profile.


``$ echo web: python app.py > Procfile`` (use capital P when writing Procfile).

- Also make sure you remove any added lines to the Procfile code as this can cause problems in Heroku running the project.

- How push to GitHub.

## Deployment on Heroku

Log onto Heroku and to create an app by clicking on the new app button.

![heroku1]()

- You need to a unique name for your application.
 
- Now select the region that is closest to you.

- Set your deployment method to 'GitHub'.

![heroku2]()

- Find the repository that you are going to deploy.

- Enable automatic deploy.

![heroku3]()

- To Set environment in Heroku App

    - Go to settings, In the config vars click show config vars.
    - Enter your key value pairs as per your env.py file.

# Credits

[CodeInstitue]() : contact us form

[CodeInstitue]() : template of the site, and code!

## Inspiration for Website
https://www.zestwellnessnutrition.com/purchase-new/60-min-virtual-11-coaching-session

## Acknowledgments

- My Wife: for her support and looking after the kids.
- My Daughter and Son: For the understand that daddy has to study.
- New Mentor: Felipe Souza Alarcon for his feedback and help.
- Code Institue: for the knowledge you gave me.
- W3School: For helpful reminders.
- [Stackoverflow](https://stackoverflow.com)
- Product image and information sourced from [MyProtein.com](https://www.myprotein.se/)

## Code

- Code Institute [Boutique-ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/933797d5e14d6c3f072df31adf0ca6f938d02218)