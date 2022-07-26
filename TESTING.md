# **GAMES EXCLUSIVES - TESTING**

Testing.md document records all reports from validators and gives a summary of manual testing which got carried out on several devices.

All of the listed tests were performed on desktop PC, Dell laptop, iPhone 8, iPhone 12, and iPad Pro and worked as planned. The app was responsive and very easy to navigate.

## SUMMARY OF ALL TESTS 
- **As user**:
    - Navigation bar links directed me to the correct pages as expected
    - Clicking through site logo gets me back to home page
    - Login, registration and logout worked as expected
        - Verification email request received upon registration
    - Browsing the site, clicking through listed games
    - Adding games to shopping basket, increasing/decreasing quantities
    - Completing successful checkout, including payment
        - Upon successful order placement, order confirmation email received
    - Left a review on a game
    - Edited and deleted a review on a game
    - Adding games to favourites and removing them
    - Subscribed to newsletter service
    - Tested footer social media links, quick links, privacy policy link
        - Facebook link took me to Games Exclusives business page
        - Instagram link to me to Games Exclusives account
        - Twitter link took me to a Twitter page
        - Privacy Policy link took me to Games Exclusives privacy policy page
    - Contact link, which is present in the footer, tested
        - Confirmation email received

- **As administrator**:
    - Added a new game with and without image
    - Edited an existing listed game
    - Deleted a listed game

---
## **USER STORIES - USER TESTING**
### **SITE USER / SHOPPER**

- As a **New User/Shopper** I can easily register on this website so that I can place an order quickly and easily

    - I can find a registration link in the main nav bar

        ![Registration link in main nav bar](media/testing/user-stories/Top_nav_drop_account_not_logged.JPG)

    - I am also prompted to register if I try to access favourites section or add a game to favourites, and try to add review

        ![Registration prompt when accessing favourites and trying to add a review](media/testing/user-stories/registration_prompt.png)

    - I am also reminded of logging in or creating an account when on checkout page

        ![Registration reminder on checkout page](media/testing/user-stories/registration_prompt_checkout.png)

- As a **Registered Shopper** I can easily login/logout of my account so that I can access my personal details, view my orders history and view my favourite games

    - Main navbar in the header contains link to account **Login** 

        ![Login link in main nav bar](media/testing/user-stories/Top_nav_drop_account_not_logged.JPG)

    - The **Login** link changes to **Logout** when I log in

        ![Logout link in top nav bar](media/testing/user-stories/Top_nav_drop_account_user.JPG)

- As a **Shopper** I will receive an email to verify my newly created account so that I can confirm my account registration was genuine and successful

    - On registering for an account, a verification email is sent to user's registered email so they can verify their account and log in

        ![Registration email](media/testing/user-stories/registration_email.JPG)

- As a **Shopper** I can register my profile so that I can add or change delivery address and view my current and previous orders

    - On registration of a new account, a personal profile is automatically rendered. Here the shopper can view their order history, delivery information and access the favourites page via the link in their account

        ![Profile page](media/testing/user-stories/profile_page.JPG)

    - When I clicked on old order number, I was taken to an order confirmation page where I was immediately notified by a toast message in the top right corner, that this is a past confirmation for an order. I could return to my profile page via the button at the bottom of this page

        ![Order confirmation page via profile page](media/testing/user-stories/order_confirmation_page_via_profile.JPG)

- As a **Registered Shopper** I can leave a game review so that I can share my opinion on said game

    ![Game info with review link](media/testing/user-stories/game_info_page_review.png)

    - Any registered user can leave a review via a form on game info page which will ask them to add title and text of their review

        ![Review form](media/testing/user-stories/game_review_form.JPG)

    - Submitted review will show title, body, username and date

        ![Review view as a user](media/testing/user-stories/review_user_view.JPG)

    - Once I click **Add Game Review** button, review is added to the game detail page and a notification toast pops up in the top right corner announcing I added my review

        ![Added review toast notification](media/testing/user-stories/added_game_review_toast.JPG)

- As a **Registered Shopper** I can edit my game review that I can share a correct view on a game

    - As an author of the review I can edit it via the link shown below the review's title

        ![Review view as an author](media/testing/user-stories/review_author_view.JPG)

    - Once I click on the **Edit** link, I am taken to a **Edit Review** page

        ![Edit review page](media/testing/user-stories/edit_game_review.JPG)

    - The **Back to game** button returns me back to the game page, the **Update Game Review** button updates the review and notification toast pops up in the top right corner announcing I updated my review

        ![Updated review toast notification](media/testing/user-stories/updated_game_review_toast.JPG)

- As a **Registered Shopper** I can delete my game review when it's no longer applicable

    - As an author of the review I can delete it via the link shown below the review's title

    - Once I click on the **Delete** link, a modal appears asking if I am sure I want to delete said review

        ![Delete review modal](media/testing/user-stories/delete_review_modal.JPG)

    - The **Cancel** button returns me back to the review, the **delete** button deletes the review and notification toast pops up in the top right corner announcing I deleted my review

        ![Deleted review toast notification](media/testing/user-stories/deleted_game_review_toast.JPG)
    
- As a **Shopper** I can type in search bar name of a product or related keyword so that I can be taken to a searched for product or list of similar ones

    - There is a search bar in the header which allows users to search for games based on keywords in the description or name fields

        ![Search bar](media/testing/user-stories/search_bar.JPG)

    - When a search query is submitted, the user is brought to a filtered games page. Here they can see the games which align with their search, as well as an indicator of how many items were found relating to the search query

        ![Search by keyword](media/testing/user-stories/search_keyword.JPG)

- As a **Shopper** I can browse through all listed products so that I can make a purchase

    - I can see a list of product cards with listed games, showing their image, name, price and **Add to favourites** link

        ![Games page with game cards](media/testing/user-stories/games_cards.JPG)

- As a **Shopper** I can click on a product so that I can view all listed details about it

    - Once I click on a desired product, I am taken to product info page where I can see the image, title, price, category and description

        ![Game detail page](media/testing/user-stories/game_detail_page.JPG)

- As a **Shopper** I want to be able to sort all products by name, price and product category so that I can see them in desired order to ease site navigation and for faster shopping experience

    - There is a **'sort-by'** selector box on games page which allowed me to sort the games by category, name and price in ascending or descending order

        ![Sort-by drop down menu](media/testing/user-stories/sort-by-drop-down.jpg)

    - I could also view games sorted by their category, name or price via the main navigation bar - when I clicked on **Games**, dropdown menu opened up with three categories

        ![Main nav dropdown menu with categories](media/testing/user-stories/main-nav-drop-down-sort-menu.jpg)

- As a **Shopper** I want to be able to read games review so that I can make informed decision before making a purchase

    - If I want to read reviews about a desired game, I have to click on the game card to get into its game detail page and see if there are any reviews in the **Review** section at the bottom of the page

        ![Reviews](media/testing/user-stories/reviews.png)

- As a **Shopper** I can add a product in to the shopping basket so that I can buy this product

    ![Adding a product to shopping basket](media/testing/user-stories/adding_to_basket_arrow.png)

    - Once I click on **Add to Basket** button, success toast pops up in the top right corner announcing I successfully added said game to a shopping basket and a pop up showing my current shopping basket summary, prices, total cost and shipping cost, if I haven't crossed the minimum spend for a free shipping. It also contains a button to a secure checkout

        ![Shopping basket toast and pop-up message](media/testing/user-stories/adding_to_basket_toast_pop_up.JPG)

- As a **Shopper** I can add or remove products in the shopping basket so that I can buy the wanted amount if I change my mind

    - There is a quantity increment and decrement button with an update button that allows the user to increase or decrease the number of the specific item they wish to purchase

        ![Adjusting shopping basket volume button](media/testing/user-stories/adjusting_basket_volume.png)

    - If choose to increase or decrease the volume, I need to click on the update button after I have selected the desired amount

        ![Adjusting shopping basket update](media/testing/user-stories/adjusting_basket_volume_update.png)

    - Once I clicked on update, success toast popped up in the top right corner announcing I successfully increased/decreased quantity and updated pop-up view of shopping basket with total and checkout link button

        ![Adjusting shopping basket toast and pop up](media/testing/user-stories/adjusting_basket_volume_update_toast.png)

    - When I clicked on remove button, the item got removed from the shopping basket, the total has updated, and success toast popped up in the top right corner announcing I successfully removed the game and an updated pop-up view of shopping basket with total and checkout link button

        ![Removing items from shopping basket button](media/testing/user-stories/adjusting_basket_volume_remove_toast.png)

- As a **Shopper** I can checkout my shopping bag so that I can complete my purchase and see a summary of my order

    - The shopping basket icon in the header gives an up-to-date counter of the current shopping basket total

        ![Shopping basket icon in top nav](media/testing/user-stories/basket_icon.png)

    - When I clicked on the shopping basket icon, I was redirected to a shopping basket page which allowed me to view all games currently in my basket, quantity, and total cost and shipping cost *(if applicable)*

        ![Shopping basket page view](media/testing/user-stories/basket_page_view.png)

    - Once I reviewed my basket and was happy with its contents I clicked on **Secure Checkout** button

         ![Secure checkout button](media/testing/user-stories/secure_checkout.jpg)

    - I was then taken to a **Checkout** page where I had to fill in my full name as it is not stored in my profile

        ![Checkout form missing info](media/testing/user-stories/checkout_form.jpg)

    - I had to then enter my card details and zip or post code - this automatically changes according to if I enter a UK card number or from another country

        ![Card details](media/testing/user-stories/card_details.jpg)

    - Once I clicked on **Complete Order** button, overlay appeared on the screen and after a short while I was taken to a page confirming my order

        ![Payment overlay](media/testing/user-stories/payment_overlay.JPG)

- As a **Shopper**, I can view the order confirmation page after I made a payment so that I know my order and payment have gone through successfully

    - Once I clicked on **Complete Order** button I was taken to **checkout success** page with my order summary of what I ordered and quantities, my billing information, my delivery information and how much I spent in total

        ![Checkout Success page](media/testing/user-stories/checkout_success.JPG)

    - A success toast pops up in the top right corner announcing I have placed my order successfully and I will receive an email confirming this

        ![Checkout Success toast](media/testing/user-stories/checkout_success_toast.JPG)

- As a **Shopper** I want to be able to receive an order confirmation email after I finalise checkout so that I can verify that I placed my order successfully

    - Once I clicked on **Complete Order** button and was taken to order confirmation page, I have received an email confirming my order with all the details

        ![Order email confirmation](media/testing/user-stories/confirmation_email.JPG)

- As a **Registered Shopper** I can add or remove a game to my favourites so that I can either purchase it again or go back to it at later stage without prolonged searches

    - I could add a game to my favourites from the main game page view by clicking the link **Add to favourites** with red heart icon

        ![Adding to favourites](media/testing/user-stories/adding_to_favourites.png)

    - I could add a game to my favourites from within the game detail page by clicking on the heart icon which is displayed far right next to the game title 

        ![Adding to favourites from game detail page](media/testing/user-stories/adding_to_favourites_game_page.png)

    - When I clicked on the heart icon to add a game to my favourites list, success toast message popped up in the top right corner

        ![Adding game to favourites toast](media/testing/user-stories/favourites_add_toast.JPG)

    - When I clicked on the heart icon of the same game to add it to my favourites list, error toast message popped up in the top right corner notifying me that the game is already in my favourites list

        ![Adding the same game to favourites toast](media/testing/user-stories/favourites_error_toast.JPG)

    - I could visit my favourites page by clicking the heart icon in the top nav bar 

        ![Visiting favourites page](media/testing/user-stories/favourites_icon.png)

    - I could also access my favourite page via my **My Profile** page by clicking on the **Favourites** link there

        ![Visiting favourites page via profile page](media/testing/user-stories/profile_page_favourites_link.png)

    - I could view all games on my favourites page where I could either click on link called **Details** to visit the game page or I could click on the **trash icon** to remove the game from my favourites list

        ![Favourites page view](media/testing/user-stories/favourites_page_view.png)

    - When I clicked on the trash icon, game was removed from my favourites page and success toast message popped up in the top right corner I have succesfully removed the game from my favourites, and because it was the only game there, I have also received a notification my favourites list was empty

        ![Removing game from favourites toast](media/testing/user-stories/favourites_removal_toast.JPG)

- As a **Shopper** I can subscribe with my email address so that I will get informed about promotions, sales and new games coming in

    ![Subscription section](media/testing/user-stories/subscription_view.JPG)

    - I could find the subscription service on home page and contact page

    - Once I entered my email address and pressed **Subscribe** button, I was redirected to a page confirming my subscription

        ![Subscription section](media/testing/user-stories/subscription_confirmation.JPG)

- As a **Shopper** I want to be able to contact the site admin so that I can ask a question, make a suggestion or send a compliment

    ![Contact confirmation email](media/testing/user-stories/contact_page.JPG)

    - Once I sent my query, confirmation of its successful submission was shown on screen via a toast message in the top right corner

        ![Successful contact submission toast](media/testing/user-stories/contact_form_success_msg.JPG)

    - I have also received a confirmation email saying someone will be in touch within 48 hours

        ![Contact confirmation email](media/testing/user-stories/contact_confirmation_email.JPG)

---
### **SHOP OWNER / ADMINISTRATOR** 
- As a **Site Admin** I can add a new product so that I can add variety to my e-store

    - When logged in as superuser, I can access the **Game Management** section via a link which is in the **Account** dropdown in the top nav bar

        ![Accessing game management page](media/testing/user-stories/game_management_link.png)

    - Once clicked, the superuser will be taken to a **Game Management - Add a game** page, where I had to select a category, and fill in the game details like game name, description and price. Optional fields are SKU number, image URL and uploading game image

        ![Add game page form](media/testing/user-stories/add_game_form_page.png)

    - If I chose to not to upload a game image, an automated placeholder image was uploaded

        ![Added game with no image](media/testing/user-stories/added_game_no_image.jpg)

- As a **Site Admin** I can change product details so that I can reflect any changes like a new description or price change

    - I can do this by selecting a game I want to edit, entering the game's info page and click on the **Edit** link which is placed underneath the category tag and is only visible to super users

        ![Game detail page with edit game link](media/testing/user-stories/edit_game_link.png)

    - I can also view this link on the main games page underneath each game

        ![Games page with edit/delete links](media/testing/user-stories/games_edit_delete_link.png)

    - Once clicked, the super user will be taken to a **Game Management - Edit a game** page, where they can make planned change like update prices, description, add or remove image, and add or change a SKU number

        ![Edit game page form](media/testing/user-stories/edit_game_form_page.JPG)

- As a **Site Admin** I want to be able to delete a game so that I can remove it if it's no longer available

    - I can do this by selecting a game I want to delete, entering the game's info page and click on the **Delete** link which is placed underneath the category tag and is only visible to super users

        ![Game detail page with delete game link](media/testing/user-stories/delete_game_link.png)

    - Once clicked on the **delete** link, game gets deleted immediately and a notification toast pops up in the top right corner

        ![Game deleted toast](media/testing/user-stories/game_deleted_toast.JPG)

- Additional testing was done to avoid any security issues - I have copied a [**Edit game**](https://games-exclusives.herokuapp.com/games/edit/6/) link and pasted it into a different browser, which resulted in the site asking me to login

    - When logged in as standard user, an error toast message popped up in the top right corner telling me, only store owners could access the editing page 

        ![Store owner access only](media/testing//user-stories/store_owner_access.JPG)

    - I have done the same testing for [**Add game**](https://games-exclusives.herokuapp.com/games/add/) and the outcome was the same

---

[Back to top](#)

---
## **AUTOMATED TESTING - CODE VALIDATORS**

<details>
<summary>HTML Validator Testing</summary>

- No errors were returned when passing through the official W3C validator

**HOME PAGE**
![W3C Validator - home page](media/testing//validators/html_validator_home.JPG)

**GAMES PAGE**
![W3C Validator - games page](media/testing//validators/html_validator_games.JPG)

**GAME DETAIL PAGE**
![W3C Validator - game detail page](media/testing//validators/html_validator_game_detail.JPG)

**SHOPPING BASKET PAGE**
![W3C Validator - shopping basket page](media/testing//validators/html_validator_basket.JPG)

**CHECKOUT PAGE**
![W3C Validator - checkout page](media/testing//validators/html_validator_checkout.JPG)

**CHECKOUT SUCCESS PAGE** 
![W3C Validator - checkout success page](media/testing//validators/html_validator_checkout_success.JPG)

**LOGIN PAGE**
![W3C Validator - login page](media/testing//validators/html_validator_login.JPG)

**LOGOUT PAGE**
![W3C Validator - logout page](media/testing//validators/html_validator_logout.JPG)

**REGISTRATION PAGE**
![W3C Validator - register page](media/testing//validators/html_validator_signup.JPG)

**PROFILE PAGE**
![W3C Validator - profile page](media/testing//validators/html_validator_profile.JPG)

**CONTACT PAGE** 
![W3C Validator - contact page](media/testing//validators/html_validator_contact.JPG)
</details>

<details>
<summary>CSS Validator Testing</summary>

- No errors were found when passing through the official Jigsaw validator

    ![Jigsaw Validator](media/testing/validators/css_validator.JPG)
</details>


<details>
<summary>Python Validator Testing</summary>

- As **PEP8 validator** is down I had to use the built-in **pycodestyle** linter checker as per CI tutor advice

- All code was checked and minor issues like blank spaces were fixed on all files
</details>

<details>
<summary>JS Validator Testing</summary>

- I have run the JS code through [**jshint**](https://jshint.com/)

**CHECKOUT PAGE**
![Checkout page - jshint validator](media/testing/validators/jshint_validator_checkout.JPG)

**QUANTITY INPUT SCRIPT**
![Checkout page - jshint validator](media/testing/validators/jshint_validator_quantity_input_script.JPG)

</details>

---
## **Lighthouse Testing**
<details>
<summary>Desktop lighthouse testing</summary>
  
  **HOME PAGE**

  ![Home page - lighthouse desktop](media/testing/validators/lighthouse_desktop.JPG)

  **GAMES PAGE**

  ![Games page - lighthouse desktop](media/testing/validators/lighthouse_games_desktop.JPG)

  **GAME DETAIL PAGE**

  ![Game detail page - lighthouse desktop](media/testing/validators/lighthouse_game_detail_desktop.JPG)

 **PROFILE PAGE**

  ![Profile page - lighthouse desktop](media/testing/validators/lighthouse_profile_desktop.JPG)

 **FAVOURITES PAGE**

  ![Favourites page - lighthouse desktop](media/testing/validators/lighthouse_favourites_desktop.JPG)

**CONTACT PAGE**

  ![Contact page - lighthouse desktop](media/testing/validators/lighthouse_contact_desktop.JPG)

  **SHOPPING BASKET PAGE**

  ![Shopping basket - lighthouse desktop](media/testing/validators/lighthouse_shopping_basket_desktop.JPG)

  **CHECKOUT PAGE**

  ![Checkout page - lighthouse desktop](media/testing/validators/lighthouse_checkout_desktop.JPG)
</details>

<details>
<summary>Mobile lighthouse testing</summary>

- While Lighthouse testing was quite high in desktop version, the performance during mobile testing was lacking. It is mostly due to render-blocking resources like jquery, bootstrap js and css. 

- I have originally got a very high score on Lighthouse under mobile performance, but it had dropped down and it's moving around 70-87 points only on Performance. 

 **HOME PAGE - first test**

![Home page - lighthouse first mobile testing](media/testing/validators/lighthouse_mobile.JPG)

**HOME PAGE - following tests**

![Home page - lighthouse first mobile testing](media/testing/validators/lighthouse_mobile_second.JPG)
</details>

---
## ACCESSIBILITY

I checked that the chosen colours and fonts are easy to read. All pages have passed through the Lighthouse reporting tool in Chrome developer tools on both mobile and desktop.

- **CONTRAST CHECKER - BODY TEXT and HOVER SELECTOR FOR ALL BUTTONS (*unless specified otherwise*)**
![Contrast checker - body text](media/testing/validators/contrast_checker_body.JPG)

![Contrast checker - hover links](media/testing/validators/contrast_checker_hover_links.JPG)

- **CONTRAST CHECKER - HOVER SELECTOR FOR BUTTONS WITH CLASS btn-dark**
![Contrast checker - hover selector](media/testing/validators/contrast_checker_hover.JPG)

---
[Back to top](#)