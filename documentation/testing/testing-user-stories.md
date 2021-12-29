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

    - A user can sign up from the navbar (Accounts) on any pages.

    - Once signed up the user can navigate to his/her dashbroad to enter in personal details i.e address.

    - Once sign in the user can also see any purchases history in  the profile page.

    - A user can sign up in the navbar and from any page.

    - Simple sign in process with 
        - email address
        - email address confirmation
        - username
        - password
        - password confirmation

- ## Did we achieve the result: Yes

![login-menu](/documentation/testing/files/user-stories/login-register.png)
![login-menu2](/documentation/testing/files/user-stories/signup.png)

## As a returning User, I want to log in to my dash-broad.

- ## All Pages

    - A user can sign in the navbar and from any page.

    - Navbar indicate if you as a user is signed up already by transforming the account dropdown menu to have 'My Profile' and 'Log out'.

- ## Sign In page

    - Simple sign in process with 
        - email address or username
        - password
 
    - Password has a toggle button to remember the user for next time.

- ## Did we achieve the result: Yes

![login](/documentation/testing/files/user-stories/sign-in.png)

## As a User, I want to log out and to know if I am logged out.

- ## All Pages

    - The user can log out by my account button in the navbar.

    - Navbar indicate if the user is log out by replacing the log out button with a log in button.

    - The user will be taken to a page to confirm they want to log out.

    - Flash message will appear with a message that you have logged out.

- ## Did we achieve the result: Yes

![log-out](/documentation/testing/files/user-stories/log-out.png)

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

- ## Did we achieve the result now: No 

- ### Had issue with the footer on different pages and try a few thing but ran out of time to fix it.  I just remove the footer.  No time as project need to be handed in and I have a 8 month boy who been keeping me up every night for 3 weeks plus trying to learn two other programs for the job I start in 1 week.


## As a administrator want to edit / delete products from the site.

- On the product page a admin user can edit / delete a product by clicking on the edit / delete buttons. This also can be done in the product detail page.

- On click edit item the admin will be taken to the edit page. The user will also have a flash message alerting them that they are on the edit page. Once the edit is done the admin user will be taken to the product detail page and a success message flash to them.

- Admin User can delete product by click on delete button after this the product will be deleted and a message will flash up confirming product was deleted.

- Only the Admin User can see the edit / delete option buttons and this will not be viewable by Vistors to the site.

- ## Did we achieve the result now: Yes

![product-edit](/documentation/testing/files/user-stories/product-view.png)
![product-edit2](/documentation/testing/files/user-stories/product-detail.png)
![product-edit3](/documentation/testing/files/user-stories/product-edit-item.png)

## As a administrator want to add products to the site.

- If the user is sign in and is gain admin status then they can access this feature in the account menu in the navbar, under Product Management.

- The admin user in how enter in a item using the form.
    - Category
    - Sku
    - Name * required
    - Description * required
    - Has sizes
    - Price * required
    - Rating
    - Flavour
    - Weight
    - Image url
    - Image (button to load photo)
    - Tags
    - Ingredients
    - Number of sessions
    - Price per session

- Once the user confirm adding product by the "Add Product" button.  The will be a flash message with a success message and the user will be taken to the product detail page of that new item.

- ## Did we achieve the result now: Yes

![add-product](/documentation/testing/files/user-stories/add-product.png)

# As a user I want know how many items and total price of the purchase that is in the bag in real time.

- As a user adds item to they bag the baggage icon in the navbar will update with each addition to the bag.
    - Number of items in the bag.
    - Total cost in the bag.

- The user will also get a flash message with more detail about the content of the bag with each new addition to the bag. The user in also scroll in this window to see other items.
    - Items name.
    - Size of clothing chosen.
    - quantity of the item.
    - Total price of bag content

- ## Did we achieve the result now: Yes

![bag](/documentation/testing/files/user-stories/bag-realtime.png)

# As a user I like to see a detail look into the my shopping bag.

- A user can click on to the shopping bag at the top, right of the navbar to look at the shopping bag contant.  Once click the user will be taken to the shopping bag cart. In here the is a detail profile of each item in the cart.
    - Image of the each item.
    - Item name
    - Item sku
    - Size of Item
    - Price
    - Qty
    - Subtotal
    - Bag Total
    - Delivery cost
    - Grand Total:

- ## Did we achieve the result now: Yes

![bag2](/documentation/testing/files/user-stories/bag-overview.png)

# As a user I want to be able to change what in the shopping bag cart eg Quantity, Remove item.

- On the shopping cart page the is a quantity input to allow the user to increase and decrease the quantity.  Once the user has enter the quantity number they can click update below the input reader to update the item.

- The user can just remove the item from the bag by click the remove icon below the quantity input reader.

- When the user has updated or remove the item / items the Bag Total, Delivery cost and Grand Total will update also.  As well as Sub-total to any items that have the quantity increase or decrease.

- ## Did we achieve the result now: Yes


![bag-update](/documentation/testing/files/user-stories/update-bag.png)
![bag-update2](/documentation/testing/files/user-stories/update-bag-2.png)

# As a user I want a easy to read checkout form that I can also save my detail for further use in the future.

- To help the user enter the right detail into the checkout form the form is very clear looking and reads from top the bottom.  The form has placeholders in each input section and will flash a prompt message if any information is enter incorrect.

- The is also a checkbox for the user to click if they want there delivery detail saving.  This will auto fill next time they purchase another order in the future.

- ## Did we achieve the result now: Yes

![checkout](/documentation/testing/files/user-stories/checkout.png)

# As a user I want confirmation that my order has accept.

- Once the user has click the complete order button, they will be taken to confirmation page with the detail of:
    - Order Number
    - Order Date
    - Items details
    - Delivery address
    - Billing info
        - Order Total
        - Delivery Cost
        - Grand Total

- Plus a flash message saying order was confirmation and accepted.

- The user will also be sent a email with the confirmation detail.

- The user can go and see confirmation history in they profile page, on all the different order history.

- ## Did we achieve the result now: Yes

![Thank](/documentation/testing/files/user-stories/thank-you.png)
![email](/documentation/testing/files/user-stories/confirm-payment.png)
![profile-history](/documentation/testing/files/user-stories/profile-history.png)
