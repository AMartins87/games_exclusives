# **INTRODUCTION**

Games Exclusives is an e-commerce website built using Django, Python, HTML, CSS and JavaScript as part of the Code Institute Diploma in Full Stack Software Development.

Purpose of this e-commerce store is to sell game versions which are only exclusive to only one type of game console or were developed only for a PC. 

Live project can be found [here](https://games-exclusives.herokuapp.com/).

![Am I Responsive](media/wireframes/air_main_image.JPG)

*Please press **Ctrl** in Windows or **Command** on Mac button and click for any links which you would like to open in a new tab when in the README.md file*

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

***Web Admin Expectations***
- Can update, add or remove products

## **USER STORIES**

### **Agile planning**
The development of this project was managed and implemented using GitHub project Kanban board and can be found [**here**](https://github.com/users/AMartins87/projects/7).

User stories were labeled with <span style="color:#c5f015">**Must Have**</span>, <span style="color: #FBCA04">**Nice to have**</span>, <span style="color:#7057ff">**Future development**</span> and <span style="color:#35EE53">**CRUD**</span>. 

Documentation like README, TESTING md files and preview of my business Facebook page were assigned a <span style="color: #1589F0">**Documentation**</span> label.
<hr>

# **FEATURES**
## **Home Page**
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

# **GAMES**
 
All **Games** pages display all listed games with preview of an image, the their name, price, category and add to favourites button with heart icon

![All Games image](media/features/games_lg.JPG)

## **Games by category** 
### **Playstation**

![PlayStation Games image](media/features/games_ps_lg.JPG)

### **Xbox**

![Xbox Games image](media/features/games_xbox_lg.JPG)

### **Nintendo**

![Nintendo Games image](media/features/games_nintendo_lg.JPG)

### **PC Classics**

![PC Classics Games image](media/features/games_pc_lg.JPG)

### **Special offers: Clearance**

![Clearance Games image](media/features/games_clearance_lg.JPG)

## **Add a product page**

![Add a game page image](media/features/)

## **Update/remove product page**

![Update/Remove product page image](media/features/)

# **MY PROFILE PAGE**
![My Profile page on large screens](media/features/profile_lg.JPG)

# **FAVOURITES PAGE**
![Favourites page on large screens](media/features/favourites_lg.JPG)

# **CONTACT PAGE**
Users can contact the site administrator by filling in the simple form on the screen where they are required to give their **name**, **email address**, and then type in their **message**.

![Contact page](media/features/contact_lg.JPG)

**Wireframes**
All wireframes were created using Balsamiq.
![Home Page](media/wireframes/)
![All Games](media/wireframes/)
![Game Page with description](media/wireframes/)
![Registration](media/wireframes/)
![Login/Logout Page](media/wireframes/)
![Contact Page](media/wireframes/)

# **MARKETING**

Facebook and Instagram are our main marketing platforms. 

I have created a [Facebook dummy page](https://www.facebook.com/profile.php?id=100086484473315) for Games Exclusives. This page contains description of our online store in ***About*** section, you can also find a link to our application in there images of some of our games and has a business description as video games store.

![Facebook Page](media/wireframes/FB_page_overwiew.JPG)

# **SEARCH ENGINE OPTIMISATION**

To find the relevant keywords for this website I made the following searches on Google, Word Tracker...and selected keywords which would be important to the customers and added them in the meta tag. 

![screenshot]

- Keywords
- Long-tail keywords

# BUGS

issues with installing fixtures both with categories and games 
categories had a typo in model "model":"games.category",
games had several " " within " " in description of some games

# UNFIXED BUGS

# **DEPLOYMENT**

This project was created using GitHub and Gitpod. Branches were created and after committing to the branch it was pushed up to the repository. 

Later, the project was deployed to Heroku, Heroku deployment was set to Enable Automatic Deploys, which meant that every time that the repository was pushed, Heroku was also updated.

Full deployment procedure can be found [here](DEPLOYMENT.md).

# CREDITS

Favicon - https://www.flaticon.com/free-icon/game-console_2949874 

## ACKNOWLEDGEMENTS