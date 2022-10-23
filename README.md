# **INTRODUCTION**

Games Exclusives is an e-commerce website built using Django, Python, HTML, CSS and JavaScript as part of the Code Institute Diploma in Full Stack Software Development.

Purpose of this e-commerce store is to sell game versions which are only exclusive to only one type of game console or were developed only for a PC. 

Live project can be found [here](https://games-exclusives.herokuapp.com/).

![Am I Responsive](media/wireframes/air_main_image.JPG)

*Please press **Ctrl** in Windows or **Command** on Mac button and click for any links which you would like to open in a new tab when in the README.md file*

---
## **USER EXPERIENCE**

This website is based on a Business to Consumer (B2C) model. 

The target market for this store are game enthusiasts, collectors and fellow gamers with peculiar tastes in games. 

### **Shopper Expectations**
- Ability to view and purchase games
- Easy to search and filter by category, name and price
- Can save a game into favourites
- Can access their account and view order history, favourite games and change personal information
- Can contact the owner via simple contact form
- Can leave, edit and delete their review

### **Website Expectations**
- Has links to Facebook, Instagram and Twitter
- Privacy Policy link is included

### ***Web Admin Expectations***
- Can update, add or remove products

---
## **USER STORIES**

### **Agile planning**
The development of this project was managed and implemented using GitHub project Kanban board and can be found [**here**](https://github.com/users/AMartins87/projects/7) *(press Ctrl in Windows or Command on Mac button while clicking on the link for it to open in a new tab)*.

User stories were labeled with <span style="color:#c5f015">**Must Have**</span>, <span style="color: #FBCA04">**Nice to have**</span>, <span style="color:#7057ff">**Future development**</span> and <span style="color:#35EE53">**CRUD**</span>. 

Documentation like README, TESTING md files and preview of my business Facebook page were assigned a <span style="color: #1589F0">**Documentation**</span> label.

---
## **FEATURES**
### **Home Page**
- Delivery banner (on every page for constant reminder to a shopper)
- Shop name/logo with built in link to home page
- Top Navbar (on every page for ease of access)
    - Account
    - Favourites
    - Basket

- Main Navbar (on every page for ease of navigation)
    - Home 
    - All Games
    - Games
    - Special Offers

![Delivery banner, top navbar and main navigation](media/features/top_nav_main_nav.JPG)

**Top navbar of a user who is not logged in:**
Register | Login

![Top navbar - not logged in](media/features/Top_nav_drop_account_not_logged.JPG)

**Top navbar when logged in as a standard user:**
My Profile | Logout
![Top navbar - logged in](media/features/Top_nav_drop_account_user.JPG)

**Top navbar when logged in as an admin:**
Admin Dashboard | Game Management | My Profile | Logout

![Top navbar - admin logged in](media/features/Top_nav_drop_account_admin.JPG)

**Main navbar with search banner on large screens**

![Main navbar on large screens](media/features/main_nav_lg.JPG)

**Main navbar with collapsible menu icon for screens with a width of 991px or less**

![Main navbar on medium and small screens](media/features/Top_nav_bar_md_all.JPG)

**Main navbar with collapsed menu for screens with a width of 991px or less**
![Medium and small navbar collapsed](media/features/main_nav_md_sm.JPG)

**Main navbar - games dropdown menu on large screens:**
By Category | By Name | By Price 
![Main navbar on large screens - games menu](media/features/menu_drop_games.JPG)

**Main navbar - games dropdown menu on screens with a width of 991px or less:**
![Main navbar on medium and small screens - games menu](media/features/main_nav_md_sm_games.JPG)

**Main navbar - all games dropdown menu on large screens:**
All Games | PlayStation | Xbox | Nintendo | PC Classics
![Main navbar on large screens - all games menu](media/features/menu_drop_all_games.JPG)


**Main navbar - all games dropdown menu on screens with a width of 991px or less:**
![Main navbaron medium and small screens - all games menu](media/features/main_nav_md_sm_all_games.JPG)

**Main navbar - special offers dropdown menu on large screens:**
Clearance 
![Main navbar on large screens - special offers menu](media/features/menu_drop_clearance.JPG)

**Main navbar - clearance dropdown menu on screens with a width of 991px or less:**
![Main navbar on medium and small screens - special offers menu](media/features/main_nav_md_sm_clearance.JPG)

**Home page with a welcome text box and *SHOP NOW* button**

![Home page](media/features/hero_img_text_btn.JPG)

**Mailchimp - Subscription section**

![Mailchimp subscription section](media/features/MC_subscribe_window_lg.JPG)

**Footer on large screens**
- Social media links for Facebook, Instagram and a link for a contact page
- Policy Privacy link
- Copyright information

![Footer on large screens](media/features/Footer_lg.JPG)

**Footer on medium and small screens with a width of 767px or less**
![Footer on medium and small screens](media/features/Footer_sm.JPG)

## **GAMES**
 
All **Games** pages display all listed games with preview of an image, the their name, price, category and add to favourites button with heart icon

![All Games image](media/features/games_lg.JPG)

### **GAMES BY CATEGORY** 
#### **Playstation**

![PlayStation Games image](media/features/games_ps_lg.JPG)

#### **Xbox**

![Xbox Games image](media/features/games_xbox_lg.JPG)

#### **Nintendo**

![Nintendo Games image](media/features/games_nintendo_lg.JPG)

#### **PC Classics**

![PC Classics Games image](media/features/games_pc_lg.JPG)

#### **Special offers: Clearance**

![Clearance Games image](media/features/games_clearance_lg.JPG)

### **ADD A GAME PAGE**

![Add a game page image](media/features/add_game_form_page.png)

### **EDIT A GAME PAGE**

![Update/Remove product page image](media/features/edit_game_form_page.JPG)

### **MY PROFILE PAGE**
- Shows shopper's profile page with their delivery information and button to submit any changes made to their details
- Order history with linked order numbers which will take them to their order confirmation page
- Link to their favourites page

![My Profile page on large screens](media/features/profile_lg.JPG)

### **FAVOURITES PAGE**
- Shows shoppers' favourites games they saved while browsing the site. Page also contains a **Browse Games** button which will take them to a Games page

![Favourites page on large screens](media/features/favourites_lg.JPG)

### **CONTACT PAGE**
- Shoppers can contact the site administrator by filling in the simple form on the screen where they are required to give their **name**, **email address**, and then type in their **message**.

![Contact page](media/features/contact_lg.JPG)

---
## **WIREFRAMES**
All wireframes were created using Balsamiq

<details><summary>View wireframe images here</summary>

**Home page**
![Home Page](media/wireframes/home.JPG)

**Games page**
![All Games](media/wireframes/games.JPG)

**Game detail page**
![Game page with description and reviews](media/wireframes/game_detail.JPG)

**Edit game page**
![Edit Game page](media/wireframes/edit_game.JPG)

**Add game page**
![Add Game page](media/wireframes/add_game.JPG)

**Registration page**
![Registration](media/wireframes/register.JPG)

**Login page**
![Login Page](media/wireframes/login.JPG)

**Logout page**
![Logout Page](media/wireframes/logout.JPG)

**Profile page**
![Profile page](media/wireframes/profile.JPG)

**Favourites page**
![Favourites page](media/wireframes/favourites.JPG)

**Contact page**
![Contact Page](media/wireframes/contact.JPG)

</details>

--- 
## **DESIGN**

### **FONT**
Electrolize font was used across the whole site, and sourced from [**Google Fonts**](https://fonts.google.com/?query=electrolize).

### **COLOUR SCHEME**

The main background colour for the site is white, apart from the footer background which was set to #e85320.

Apart from the website logo and links in a footer, all text is black.

The footer text, links and icons are white.

---
# **MARKETING**

Facebook and Instagram are our main marketing platforms. 

I have created a [Facebook dummy page](https://www.facebook.com/profile.php?id=100086484473315) for Games Exclusives. This page contains description of our online store in ***About*** section, you can also find a link to our application, privacy policy and business description as video games store.

![Facebook Page](media/wireframes/facebook.JPG)

Instagram page was also created for purpose of this project [Instagram dummy page](https://www.instagram.com/gamesexclusives/)

![Instagram Page](media/wireframes/instagram.jpg)

---
# **SEARCH ENGINE OPTIMISATION**

To find the relevant keywords for this project I made searches on [Wordtracker](https://www.wordtracker.com/), [ahrefs](https://ahrefs.com/free-seo-tools) and [Game shop website](https://www.game.co.uk/), and selected keywords which would be important to customers, and added them in the meta tag section of my base.html 

---
# **BUGS**

- I had issues with installing fixtures with both categories and games fixtures. After a review I found I had a typo in category model, and my games fixtures contained double quotation marks within double quotation marks in the games description. Once I changed these to single quote marks all was loading correctly. 

--- 
# **DEPLOYMENT**

This project was created using GitHub and Gitpod. Branches were created and after committing to the branch it was pushed up to the repository. 

Later, the project was deployed to Heroku, Heroku deployment was set to Enable Automatic Deploys, which meant that every time that the repository was pushed, Heroku was also updated.

Full deployment procedure can be found [here](DEPLOYMENT.md).

---
# **CREDITS**

Background image was created in [Canva](https://www.canva.com/)


Favicon - https://www.flaticon.com/free-icon/game-console_2949874 

---
## **ACKNOWLEDGEMENTS**

Tutor support - John 
send_confirmation_emails