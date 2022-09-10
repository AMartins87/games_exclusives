# **GAMES EXCLUSIVES - TESTING**

Testing.md document records all reports from validators and gives a brief summary of manual testing which got carried out.

# **Manual Testing**

I have tested the site functionality and created a couple of normal user accounts during this process.

## **1. Menu/navbar links**
### **Purpose: Test if all present link take users to the correct pages**

These were tested by clicking on each navigation link from each page.
All links are directed to the correct pages as expected.

---

## **2. Registration & Login**
### **Purpose:Test if users can register to the website**

1. Enter [Games Exclusives e-commerce site](https://games_exclusives.herokuapp.com/) and click on [**Register** link](https://games_exclusives.herokuapp.com/users/register/) in top navbar

    ![Registration testing](media/testing/)

2. Write in the username, first and last name, email, password, and again password to confirm. Then click *Register* button

    ![Registration testing 2](media/testing/)

3. Once the user clicks on the register button, they will be taken **Login page** to log in with their new login details

4. User is successfully logged and redirected to home page

---

## **3. Logout**
### **Purpose: Test if users can logout of their account**

1. log in to [Games Exlusives](https://games_exclusives.herokuapp.com/)
2. Top navbar links change from Login / Register to **Logout** and **My Profile** link will appear
3. Click on **Logout**

    ![Logout testing](media/testing/)

4. User will be asked if they are sure they want to loggout and if clicked yes, user is successfully logged out and redirected to the home page

---

## **4. Adding product into shopping basket**
### **Purpose: Test if users can add a product into a shopping basket**

---

# **5. Checkout**
### **Purpose: Test if users can checkout**

---

# **6. Ameding quantities and removing itesm from a shopping basket**
### **Purpose: Test if users can change quantities of products in their basket and/or remove them**

---

## **7. Add to favourites testing**
### **Purpose: Test if favourite button works**

1. If shopers are not logged in, the favourite icon won't show on the screen

    ![Favorite icon testing - not logged in](media/testing/)

2. If shoppers are logged in, the favourite icon will show on the screen

    ![Favorite icon testing  - logged in](media/testing/)

3. By clicking on the **Favourite** icon, the product will save in shoppers account and they will be able to view it when clicking on **My Account** link in top nav bar

    ![Favorite icon testing  - favourited](media/testing/)

---

## **8. Edit/Update listed product**
### **Purpose: Test if listed products can be updated with new price, information or with a new image**

1. To be able to edit/update a product I have to be logged in as an administrator


---

## **9. Delete listed product**
### **Purpose: Test if a product can be deleted**

1. To be able to delete a product, I have to be logged in as an administrator
2. Once logged in, I have to click on **My Account** in top right corner and then product management link 

    ![Delete product testing](media/testing/)
 
---

## **10. Footer - social media links**
### **Purpose: Test if all social media links take users to their respective links and open in new windows**

These were tested by clicking on each social media icon.
All of these opened respective social media sites in new windows as expected.

## **11. Footer - contact page link**
### **Purpose: Test if users can successfully contact the site administrator via the Contact page link**

1. Click on [**Contact Us**](https://games_exclusives.herokuapp.com/contact/) link within a footer
2. The page opened, I was able to fill it in and submitted. All site users, both registered and not, can use the contact form by filling all the required details - Name, email, reason of their contact and then the message text
    ![Contact form testing of name input](media/testing/contact_page_testing_name.png)
    ![Contact form testing of email input](media/testing/contact_page_testing_email.png)
    ![Contact form testing of subject input](media/testing/contact_page_testing_subject.png)
    ![Contact form testing of message input](media/testing/contact_page_testing_body.png)

3. Confirmation of its succesfull submission was shown on screen and confirmation email received.

---

All of these tests were performed on desktop PC, Dell laptop, and iPhone8, iPhone 8, iPhone 12, and iPad Pro and worked as planned. The app was responsive and very easy to navigate.

### SUMMARY OF ALL TESTS 
- Menu links tested
- Login and registration
- Browsing and clicking through of listed products
- Added a new product with and without image
- Edited an existing listed product
- Deleted a product listing
- Left a rating/review on a product
- Added a product to favourites
- Tested all footer social media links
- Tested contact link and filled in the contact form

---

# Validator Testing

## **HTML**
- No errors were returned when passing through the official W3C validator

    ![W3C Validator](media/testing//validators/)

## **CSS**
- No errors were found when passing through the official Jigsaw validator

    ![Jigsaw Validator](media/testing/validators/)

## **PEP8**
- All python code was checked via [PEP8](http://pep8online.com/) with no errors reported.)
    
  ### **Games app**
  #### **admin.py**

  ![PEP8 admin.py](media/testing/validators/)

  #### **forms.py**

  ![PEP8 forms.py](media/testing/validators/)

  #### **models.py**

  ![PEP8 models.py](media/testing/validators/)

  #### **urls.py**

  ![PEP8 urls.py](media/testing/validators/)

  #### **views.py**

  ![PEP8 views.py](media/testing/validators/)

# Accessibility

I checked that the chosen colors and fonts are easy to read. All pages have passed through the Lighthouse reporting tool in Chrome developer tools on both mobile and desktop.

- [Contrast checker - body text](media/testing/validators/)
- [Contrast checker - links](media/testing/validators/)
- [Contrast checker - hover selector](media/testing/validators/)

---

## **Lighthouse Testing**

  ### **Desktop**
  
  ![Lighthouse_desktop](media/testing/validators/)

  ### **Mobile**

  ![Lighthouse_mobile](media/testing/validators/)