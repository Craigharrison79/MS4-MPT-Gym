# Testing user Stories

## As a new user, I want an access the website on different device so I need to site to be responsive.

 - ## Navbar menu

    - The content has to be optimised for the device I am using when I visit the site.

    - Due to lack of real estate in the navbar on tablet and mobile devices, the navbar menu needs to collapse. A toggle button on the left hand side will appear and when click, a menu will display the menu option. The search, account and bag icon will still be display for accessibility.

    - If toggle the button is click once, the menu will appear and clicked again it will close and disappear.

- ## Did we achieve the result: Yes

![navbar-menu](/documentation/testing/files/user-stories/navbar-menu.png)
![navbar-menu2](/documentation/testing/files/user-stories/navbar-menu-mobile.png)
![navbar-menu3](/documentation/testing/files/user-stories/navbar-open.png)
![navbar-menu4](/documentation/testing/files/user-stories/navbar-search.png)
![navbar-menu5](/documentation/testing/files/user-stories/navbar-accounts.png)

## As a User, I want an easy and hassle free navigate through out the site for page to page.

- ## Navbar buttons

    - All buttons take you to the page or perform the exact action which is stated without errors.

    - All social media icons are linked to the correct website or application without errors.

    - All buttons are easy to read and understand.

- ## Did we achieve the result: Yes

## As a new User, I want to see the product and clubs without having to register. I want to peru's the site to see if this is a site suitable for me to use before joining.

- ## Home Page

    - Have the ability to quickly search for a particular product, type of categories that I am looking for.

- ## Product/Club Page

    - Clear looking layout that is easy for the eye to follow and also to understand what to do with the information and what to do/go next.

    - All buttons take you to the correct page without errors.

    - See some useful information about the product/club, so I can make a quick decision whether on to look at that product/club further.

    - Name of Product it's rating and price

    - Name of Club it's address and telephone number.

    - Have the ability to quickly search for a particular product, by:
        - name (A-Z) descending / ascending.
        - price descending / ascending.
        - categories (A-Z) descending / ascending.

- ## Did we achieve the result: Yes

![product-view](/documentation/testing/files/user-stories/product-view.png)
![product-view1](/documentation/testing/files/user-stories/product-sort.png)

## As a new User, I want to find out the location of the gym and information about the gym itself and personal trainer.

- ## Club Page

    - On click on the club link in the navbar the user will be taken to the club page.  On arriving to the page the user will see a list of club to choose from with some basic information.
        - Club Name
        - Club Telephone Numnber
        - Club Address

    - Once the button on the individual club card is click the user will be shown the club detail page.

    - Club detail page will present the club information, opening times and a list of personal trainer working in that gym.

    - On each personal trainer card the will be a:
        - Profile photo (if not the will be a place holder image).
        - Personal Trainer Name
        - Speciality
        - Social Media link (if no social link then the accordion will be empty)
        - Contact Number

    - All social media link work

- ## Did we achieve the result: Yes

![club-pt](/documentation/testing/files/user-stories/pt-speciality.png)
![club-pt2](/documentation/testing/files/user-stories/pt-social.png)

## As a new User, I want to understand what the difference will be between signing up and be a user or just view as a non-user.

- ## Home Page

    - On the home page there is an information panel display benefits a user has when signing up to the site.

![navbar-menu](/documentation/testing/files/user-stories/navbar-menu.png)

- ## Did we achieve the result: Yes

 ## As a new User, I want to sign up to the site to purchase products on this site.

- ## All Pages

    - Two spots that a user can sign up, navbar (Accounts) and from the home page.

    - Once signed up the user can navigate to his/her dashbroad to enter in personal details i.e address.

    - Once sign in the user can also see any purchases history.

- ## Did we achieve the result: Yes

![login-menu](/documentation/testing/files/user-stories/login-register.png)


## As a returning User, I want to log in to my dash-broad.

- ## All Pages

    - Two spots that a user can sign up, navbar and from the home page.

    - Simple sign in process with 
        - email address
        - email address confirmation
        - username
        - password
        - password confirmation

    - Navbar indicate if you as a user is signed up already by transforming the account dropdown menu to have 'My Profile' and 'Log out'.

- ## Sign In page

    - Simple sign in process with 
        - email address or username
        - password
 
    - Password has a toggle button to remember the user for next time.

- ## Did we achieve the result: Yes

## As a User, I want to log out and to know if I am logged out.

- ## All Pages

    - The user can log out by my account button in the navbar.

    - Navbar indicate if the user is log out by replacing the log out button with a log in button.

    - Flash message will appear with a message that you have logged out.

- ## Did we achieve the result: Yes

## As a User / Visitor I want to be able to find a products quickly.

-  Users and visitors have two places to quickly find a product by the narvbar bar.

- Navbar:

    - Search bar - here you can type in the item, keyword or category you wish to find.

    - Also in the nav link the is a dropdown menu with different categories that the user can pick from.
        - Once on the product page the user can sort throught the items by:
            - name (A-Z) descending / ascending.
            - price descending / ascending.
            - categories (A-Z) descending / ascending.

- ## Did we achieve the result now: Yes

![search-bar](/documentation/testing/files/user-stories/search-bar.png)

## As a User / Visitor  wants to send a message about the site, problems they are having with the site or any other problem / questions they may have.

- In the navabr the is a contact page link that will take the user to the contact us page.

- Users can fill in the user details in the form and a message about the issue. This will confirmation the email was sent by flashing a  message on the screen.

- This will also send a message to the company with details about the users and the issue / message they have sent.

- ## Did we achieve the result now: Yes

![contact](/documentation/testing/files/user-stories/contact.png)
![contact2](/documentation/testing/files/user-stories/email-contact.png)

## As a User / Visitor want to view social media from the company.

- Every page has the related social media button in the footer which when clicked will take the user to the appropriate page in a new browser.

- ## Did we achieve the result now: Yes

## As a administrator want to edit / delete products from the site.

- On the product page a admin user can edit / delete a product by clicking on the edit / delete buttons. This also can be done in the product detail page.

- On click edit item the admin will be taken to the edit page. The user will also have a flash message alerting them that they are on the edit page. Once the edit is done the admin user will be taken to the product detail page and a success message flash to them.

- Admin User can delete product by click on delete button after this the product will be deleted and a message will flash up confirming product was deleted.

- Only the Admin User can see the edit / delete option buttons and this will not be viewable by Vistors to the site.

- ## Did we achieve the result now: Yes

![product-edit](/documentation/testing/files/user-stories/product-view.png)
![product-edit2](/documentation/testing/files/user-stories/product-detail.png)
![product-edit3](/documentation/testing/files/user-stories/product-edit-item.png)

