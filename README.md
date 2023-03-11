# My First Box

![Responsive web image](assets/testing/am-i-responsive.png)

The Live Website can be accessed [HERE!](https://.herokuapp.com/)

This is an e-commerce website selling personalised baby products (cord for the pacifier or the teether, bibs, muslins, case to store the teether or pacifier or whatever you want) as a first present for the new-born. The site’s main purpose is to allow users to browse and view baby products whether they are registered or not. Registered users can also buy products, change their information, add them to favourites, like or dislike products, and leave comments that can be updated or deleted by the user.



## Table of Contents
- [My First Box](#my-first-box)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Home Page](#home-page)
        - [Navigation \& Viewing](#navigation--viewing)
        - [Purchasing \& Checkout](#purchasing--checkout)
        - [Searching \& Sorting](#searching--sorting)
        - [Store Info Pages](#store-info-pages)
      - [Products Page](#products-page)
      - [Products Details Page](#products-details-page)
      - [Comments section](#comments-section)
      - [User Registration \& Profile Account](#user-registration--profile-account)
      - [Store Owner Panel Page](#store-owner-panel-page)
      - [Store Owner Add Products Page](#store-owner-add-products-page)
      - [Store Owner Edit Products Page](#store-owner-edit-products-page)
      - [Store Owner Delete Products Page](#store-owner-delete-products-page)
      - [Store Owner Orders Page](#store-owner-orders-page)
      - [Admin Control](#admin-control)
    - [Future Features](#future-features)
  - [UX](#ux)
    - [Site Purpose](#site-purpose)
    - [Agile Methodology](#agile-methodology)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Flow Diagram](#flow-diagram)
  - [Testing](#testing)
    - [User Testing](#user-testing)
    - [Manual Testing](#manual-testing)
    - [Bugs to fix](#bugs-to-fix)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
    - [GitHub](#github)
    - [Django and Heroku](#django-and-heroku)
      - [Final Deployment](#final-deployment)
    - [How to Fork it](#how-to-fork-it)
    - [How to Clone it](#how-to-clone-it)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)

## Features
### Existing Features
#### Home Page

![Home page](static/testing/home.png)

##### Navigation & Viewing
The website has a user-friendly navigation system that allows customers to easily browse and search for products. They can view products in list form and see detailed product descriptions, including customer reviews, to make informed purchasing decisions.

##### Purchasing & Checkout
Customers can add products to their cart, select product size and quantity, and securely checkout using various payment options. They receive confirmation of their order and a confirmation email after checkout.

##### Searching & Sorting
Customers can search for products by name, category, or keyword and sort them by price, popularity, or other filters.

##### Store Info Pages
Customers can access relevant company information, such as the company's mission statement, privacy policy, and shipping and return policies.

#### Products Page

![ page](static/testing/.png)

#### Products Details Page

![Products Detail](static/testing/.png)


#### Comments section

<details>
  <summary>Comments section</summary>

![Comment section](static/testing/comments.png)

- Leave a comment

![Leave a comment](static/testing/leave_comment.png)

- Comment Approval

![Comment approval](static/testing/comment_approval.png)

- Edit Comment Page

![Edit Comment](static/testing/edit_comment.png)

- Delete Comment Page

![Delete Comment](static/testing/delete_comment.png)

</details>

#### User Registration & Profile Account

Users can register for an account and create a profile where they can manage their personal information, view order history, and add/edit shipping addresses.

<details>
  <summary>User/Costumer Account Pages</summary>

- Register page

![Register page](static/testing/register.png)

- Login page
  
![Login page](static/testing/login.png)

- Logout page

![Logout page](static/testing/logout.png)

- Profile page

![Profile page](static/testing/.png)

</details>

<details>
  <summary>Store Owner Pages</summary>

#### Store Owner Panel Page

![](static/testing/.png)

#### Store Owner Add Products Page

![](static/testing/.png)

#### Store Owner Edit Products Page

![](static/testing/.png)

#### Store Owner Delete Products Page

![](static/testing/.png)

#### Store Owner Orders Page

![](static/testing/.png)

</details>

#### Admin Control

![Admin Control page](static/testing/admin.png)

[Back to top](#my-first-box)

### Future Features

In the future, we plan to add more products to our inventory, including personalized baby blankets and clothing. We also plan to offer gift wrapping options for customers who wish to purchase items as gifts. Additionally, we will continue to improve our website's user interface and security features to provide the best possible online shopping experience for our customers.

[Back to top](#my-first-box)

## UX
### Site Purpose
- To provide a user-friendly and secure online shopping experience for customers looking to purchase personalised baby products.

### Agile Methodology

The Agile Methodology was used to plan and manage this project. Epics and Issues were created on GitHub so that tasks could be assigned and prioritised using the Project Board.

### User Stories

- 

[Back to top](#my-first-box)

## Design

The colour scheme for the design of the website is based in warn nature colours.

![Image Colours](/static/testing/.png)

### Flow Diagram

![Flow diagram](static/testing/Database_ER_diagram.jpeg)

The flow chart above, created with the website [Lucid chart](https://lucid.app/), provides a simplified overview of what I was trying to accomplish.

[Back to top](#my-first-box)

## Testing

The website was constantly tested during development.

### User Testing

- User Testing:
  
  - Expectations:
  
  

  - Result:


### Manual Testing

| **Navigation Bar** | Status
|:-------:|:--------|
| Click on navbar logo loads home page | &check;
| Click on the Home tab loads the home page | &check;
| Click on Login loads the login page | &check;
| Click on Signup loads the signup page | &check;
| Click on Logout loads the logout page | &check;

| **Navigation Footer** | Status
|:-------:|:--------|
| Click on Facebook Icon opens external Tab | &check;
| Click on Twitter opens external Tab | &check;
| Click on Instagram opens external Tab | &check;
| Click on YouTube opens external Tab | &check;

| **Home Page** | Status
|:-------:|:--------|
| Sign up and Login visible when logged out | &check;
| Logout and Profile visible when logged in | &check;
| Username visible when logged in | &check;


### Bugs to fix


[Back to top](#my-first-box)

## Technologies Used

- HTML: Used to structure all the templates on the site.
- CSS: To provide extra styling to the site.
- Python: To provide the functionality to the site. Packages used in the project can be found in requirements.txt.
- Django: Python framework used in the project.
- JavaScript: Minimum JavaScript was used to fade out alerts.
- Bootstrap 4: To create layouts and styles for the website.
- [GitHub](https://github.com/): Used to store my repository for submission.
- [Gitpod](https://gitpod.io/): Used to develop the application.
- GitBash: Used to push the repository to GitHub.
- [Heroku](https://www.heroku.com/): Used to deploy the website.
- [ElephantSQL](https://www.elephantsql.com/): Used for the database during development and deployment.
- [Cloudinary](https://cloudinary.com/): To host Static files for the site.
- [Lucid chart](https://www.lucidchart.com/): Used to make a flow diagram to help with the logic & flow of the code.
- [Balsamiq](https://balsamiq.com/): To create wireframes for the project.
- [Am I Responsive?](https://ui.dev/amiresponsive): To ensure the project looked good across all devices.
- [Favicon](https://favicon.io/favicon-converter/) - To create the favicon icon.

[Back to top](#my-first-box)

## Deployment

### GitHub 

To create a new repository, I took the following steps:

1. Logged into GitHub.
2. Click the ‘repositories’ section.
3. Click the green ‘new’ button to create new repository.
4. Choose ‘repository template’ Used the code institute template as recommended from the dropdown menu.
5. Add repository name then clicked the green ‘create repository button’ at the bottom of the page.
6. Open the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

### Django and Heroku

To get the Django framework installed and set up I followed Code institute Boutique Ado.

#### Final Deployment 
    DEBUG = False

    X_FRAME_OPTIONS = 'SAMEORIGIN' 

    In Heroku go to Reveal Congfig Vars  
    Remove Disable_Collectstatic

    Go to Deploy Tab & Deploy Branch

### How to Fork it
1. On GitHub, go to [CarmenCantudo/my-first-box]( https://github.com/CarmenCantudo/my-first-box).
2. In the top right, click "Fork".

### How to Clone it
1. Go to the main page of the repository.
3. Above the file list, click "Code".
4. Select HTTPS, SSH, or GitHub CLI and then click copy to clone it.
5. Open Git Bash.
6. Change the location of your cloned repository.
7. Type `git clone` and then paste the URL you copied.
8. Press “Enter” to create your clone.

### Making a Local Clone
1. Locate the [Repository]( https://github.com/CarmenCantudo/my-first-box).
2. Click "Code".
3. Click Clone or Download.
4. Copy the Git URL from the dialogue box.
5. Open a terminal window in your chosen directory using your preferred development editor.
6. Change the location to where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL you copied.
8. Press Enter, and your local clone will be created.

[Back to top](#my-first-box)

## Credits

Resources used in the process of the "My First Box" website design and build:
- [Stack Overflow](https://stackoverflow.com/): Help with general questions.
- Boutique Ado Code Institute project.
- [Images and icon](https://www.freepik.com/).

[Back to top](#my-first-box)