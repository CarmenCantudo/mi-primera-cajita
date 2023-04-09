# Mi Primera Cajita

![Responsive web image](static/testing/am-i-responsive.jpg)

The Live Website can be accessed [HERE!](https://mi-primera-cajita.herokuapp.com/)

Mi Primera Cajita is an E-Commerce store that has been developed using Python, Django, JavaScript, CSS, HTML, and Bootstrap5. It integrates Stripe payments and has role-based permissions for users to interact with the central dataset. The site also features user authentication and complete CRUD functionality for products.

Mi Primera Cajita is a small business based in Marbella (Spain), that sells personalised baby products (cord for the pacifier or the teether, bibs, muslins, case to store the teether or pacifier or whatever you want) as a first present for the new-born.

The site’s main purpose is to allow users to browse and view baby products whether they are registered or not. Registered users can also buy products, change their information, add them to favourites, like or dislike products, and leave comments that can be updated or deleted by the user.

Please note that this version has been created solely for Project 5 of the Code Institute Diploma in Software Development. Therefore, no real payments will be accepted, and any orders placed will not be fulfilled.

However, we will soon be launching a fully functional live site at www.miprimeracajita.com.

If you want to test the payment functionality, please use the following card details when prompted:

´´´
Card number: 4242 4242 4242 4242
Expiration Date: Any future date (e.g., 04 / 24)
CVC: Any 3 digits (e.g., 242)
ZIP: 42424
´´´

## Table of Contents

- [My First Box](#mi-primera-cajita)
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

<details>
  <summary>Home Page</summary>

![Home page](static/testing/home.png)

</details>

##### Navigation & Viewing

The website has a user-friendly navigation system that allows customers to easily browse and search for products. They can view products in list form and see detailed product descriptions, including customer reviews, to make informed purchasing decisions.

<details>
  <summary>Navigation section</summary>

![Navigation section](static/testing/navigation.jpg)

</details>

<details>
  <summary>Search section</summary>

![Search section](static/testing/search.jpg)

</details>

<details>
  <summary>Welcome section</summary>

![Welcome section](static/testing/home-welcome.jpg)

</details>

<details>
  <summary>Categories section</summary>

![Categories section](static/testing/home-categories.jpg)

</details>

<details>
  <summary>Latest News section</summary>

![Latest News section](static/testing/home-news.jpg)

</details>

<details>
  <summary>Footer social section</summary>

![Footer social section](static/testing/home-social.jpg)

</details>

<details>
  <summary>Footer menu section</summary>

![Footer menu section](static/testing/home-footer-menu.jpg)

</details>

<details>
  <summary>Scroll Back To Top Button</summary>

![Scroll Back To Top Button](static/testing/scroll-to-top.jpg)

</details>

[Back to top](#mi-primera-cajita)

#### Products Page

The products page displays a list of all the products available for purchase. Each product has an image, name, description, and price displayed. The user can click on a product to go to its details page.

<details>
  <summary>Scroll Back To Top Button</summary>
  
![Products page](static/testing/products.png)

</details>

##### Products Details Page

The product details page displays a larger image of the product, along with the name, description, and price. The user can select the quantity they wish to purchase and add the product to their bag. Also, they can add the product to favourites.

<details>
  <summary>Products Detail</summary>

![Products Detail](static/testing/products-detail.png)

</details>

<details>
  <summary>Products Add to bag</summary>

![Products Add to bag](static/testing/products-add-to-bag.jpg)

</details>

[Back to top](#mi-primera-cajita)

##### Review section

The review section allows users to leave reviews about the products. Only logged-in users can leave reviews. The reviews are displayed on the product details page.

<details>
  <summary>Review section</summary>

![Review section](static/testing/reviews.jpg)

- Leave a Review

![Leave a Review](static/testing/add-reviews.jpg)

- Review Success

![Review Success](static/testing/review-success.jpg)

- Edit Review Page

![Edit Review](static/testing/edit-reviews.png)

- Review Update Success

![Review Update Success](static/testing/review-update-success.jpg)

- Delete Review Success

![Delete Review](static/testing/review-deleted-success.png)

- Delete Review Error

![Delete Review Error](static/testing/review-delete-error.jpg)

</details>

##### Favourites section

The Favourites section in this project allows users to add their favourite products to a list for quick and easy access. To use this feature, simply navigate to the product details page and click the 'Add to Favourites' button.

To view your favourites list, click the 'Favourites' link in My Account menu. From there, you can view and manage your list by adding or removing products as needed.

Note that the Favourites section requires user authentication, so you will need to be logged in to use this feature.

<details>
  <summary>Favourites page</summary>

![Favourites page](static/testing/favourites.png)

![Favourites icon](static/testing/favourites-icon.png)
![Favourites icon2](static/testing/favourites-icon2.png)

</details>

[Back to top](#mi-primera-cajita)

#### Purchasing & Checkout

Customers can easily purchase products by adding items to their shopping bag, selecting product colour and quantity, and securely checking out. During checkout, customers are required to provide their shipping address and payment details. Once the order is completed, customers receive an order confirmation on the website and a confirmation email with their order details.
Stripe is used to securely process payments, ensuring that customers' personal and payment information is kept confidential.

<details>
  <summary>Shopping Bag</summary>

![Shopping Bag](static/testing/shopping-bag.png)

</details>

<details>
  <summary>Purchasing & Checkout page</summary>

![Purchasing & Checkout page](static/testing/checkout.png)

</details>

<details>
  <summary>Order Success page</summary>

![Order Success page](static/testing/checkout-success.png)

</details>

[Back to top](#mi-primera-cajita)

#### Searching & Sorting

Customers can search for products by name, category, or keyword and sort them by price, popularity, or other filters.

<details>
  <summary>Searching & Sorting</summary>

![Sorting](static/testing/sorting.jpg)

![Search section](static/testing/search.jpg)

</details>

##### Store Info Pages

Customers can access relevant company information, such as the about us page, contact us form, faqs, and policies.

<details>
  <summary>Store Info Pages</summary>

![About us](static/testing/about-us.png)

</details>

<details>
  <summary>Privacy Policy Pages</summary>

![Privacy Policy](static/testing/privacy-policy.png)

</details>

<details>
  <summary>Cookie Policy Pages</summary>

![Cookie Policy](static/testing/cookie-policy.png)

</details>

<details>
  <summary>Terms and conditions Pages</summary>

![Terms and conditions](static/testing/terms.png)

</details>

<details>
  <summary>Faqs Pages</summary>

![Faqs](static/testing/faqs.png)

</details>

[Back to top](#mi-primera-cajita)

#### User Registration & Profile Account

Users can register for an account and create a profile where they can manage their personal information, view order history, and add/edit shipping addresses.

<details>
  <summary>Register page</summary>

![Register page](static/testing/accounts-signup.png)

</details>

<details>
  <summary>Login page</summary>

![Login page](static/testing/accounts-login.png)

</details>

<details>
  <summary>Logout page</summary>

![Logout page](static/testing/accounts-logout.png)

</details>

<details>
  <summary>Password Reset page</summary>

![Password Reset page](static/testing/password-reset.png)

</details>

<details>
  <summary>Profile page</summary>

![Profile page](static/testing/accounts-profile.png)

</details>

[Back to top](#mi-primera-cajita)

##### News Page

<details>
  <summary>News Pages</summary>

![News Pages](static/testing/news.png)

</details>

##### Article Page

<details>
  <summary>Article Pages</summary>

![Article Pages](static/testing/article.png)

</details>

#### Store Owner Add Products Page

<details>
  <summary>Add Products Page</summary>

![Add Products Page](static/testing/products-add.png)

</details>

#### Store Owner Edit Products Page

<details>
  <summary>Edit Products Page</summary>

![Edit Products Page](static/testing/products-edit.png)

</details>

#### Store Owner Delete Products Page

<details>
  <summary>Delete Products Page</summary>

![Delete Products Page](static/testing/delete-product-success.jpg)

</details>

#### Store Owner Add Article Page

<details>
  <summary>Add Article Page</summary>

![Add Article](static/testing/add-news.png)

</details>

#### Store Owner Edit Article Page

<details>
  <summary>Edit Article Page</summary>

![Edit Article](static/testing/news-edit.png)

</details>

<details>
  <summary>Delete Article Page</summary>

![Delete Article](static/testing/delete-news.jpg)

</details>

#### Admin Control Page

<details>
  <summary>Admin Control Page</summary>

![Admin Control page](static/testing/admin.png)

</details>

[Back to top](#mi-primera-cajita)

### Future Features

In the future, we plan to add more products to our inventory, including personalised baby blankets and clothing. We also plan to offer gift wrapping options for customers who wish to purchase items as gifts. Additionally, we will continue to improve our website's user interface and security features to provide the best possible online shopping experience for our customers.

- Customise Products with names.
- Implement Comments in Articles.
- Add additional product images.
- Product Image to Expand on Hover Over.

[Back to top](#mi-primera-cajita)

## UX

### Site Purpose

- To provide a user-friendly and secure online shopping experience for customers looking to purchase personalised baby products.

### Agile Methodology

The Agile Methodology was used to plan and manage this project. Epics and Issues were created on GitHub so that tasks could be assigned and prioritised using the [Project Board](https://github.com/users/CarmenCantudo/projects/4).

#### User Stories

**Epic: User Registration & Profile Account**

As a customer I can create a user account, manage my profile information and reset my password so that I can have a personalised shopping experience and easily access my order history and saved information.

As a store owner I can view a list of registered users and their information so that I can manage user's accounts.

1. As a customer I can create an account so that can purchase personalised baby products
2. As a customer I can log in/log out so that I can access my account and view my purchase history.
3. As a customer I can reset my password if I forget it so that I can access my account.
4. As a customer I can update my personal information, such as my name, email address, and shipping address so that I can keep my account up-to-date.
5. As a store owner I can view a list of registered users and their information so that I can manage user's accounts.

**Epic: Navigation & Product Pages**
As a user/costumer I can easily navigate the website, view products in a list format, view the product details and images and leave a review on a product so that I can quickly find the products I'm interested in and easily compare them, make an informed decision about my purchase and share my experience with others.

As a store owner I can approve reviews from costumers so that they will be shown on the product page.

1. As a customer I can navigate the website easily so that I can quickly find the products I'm interested in.
2. As a customer I can view products in a list format so that I can easily compare them.
3. As a customer I can view the product details so that I can make an informed decision about my purchase.
4. As a customer I can leave a review on a product so that I can share my experience with others.
5. As a store owner I can approve reviews from costumers so that they will be shown on the product page.

**Epic: Admin & Store Management**

As a store owner, I need access to an admin section where I can manage my store and products so that I can easily add, update, or delete products as required.

1. As a store owner I can access the admin section from the website so that I can manage my store.
2. As a store owner I can add a new product to the store so that customers can purchase it.
3. As a store owner I can update a product's details so that I can provide more information to customers.
4. As a store owner I can delete a product from the store so that it is no longer available for purchase.
5. As a store owner I can upload product images for new products so that customers can see what they're buying.

**Epic: Searching & Sorting**

As a user/costumer I can search and sort products so that I can quickly find the product I am looking for.

As a store owner I can add and delete product categories and search for costumers orders so that I can organise the products and quickly find specific orders.

1. As a store owner I can add a new product category to the store so that I can organise my products.
2. As a store owner I can delete a product category from the store so that I can reorganise my products.
3. As a store owner I can search for products on the website so that I can find the products I'm looking for quickly and easily.
4. As a store owner I can sort products by different criteria so that I can easily find the products that best fit my needs.
5. As a store owner I can search for orders based on customer information so that I can quickly find specific orders.

**Epic: Purchase & Payment Processing**

As a store owner, I want costumers to add products to their basket, adjust the quantity of the product, personalised the product and view their basket before proceeding to checkout so that they can make sure that the products and quantities they want are correct before completing their purchases.

As a costumer, I can enter my billing and shipping information, select a payment method, review the order details, and submit the order so that I can complete the checkout process and receive the purchased products.

As an store owner, I can view orders that have been placed, update order status and confirm the order has been shipped or refunded so that I can manage the fulfilment process and provide accurate information to shoppers who have placed an order.

1. As a customer I can add a product to my bag, adjust the quantity of the product, select the colour of the product and view my bag before proceeding to checkout so that I can make sure that the products and quantities I want are correct before completing my purchase.
2. As a customer I can enter my billing and shipping information, select a payment method, review my order details, and submit my order so that I can complete the checkout process and receive my purchased products.

**Epic: Favourite Products**

As a store owner I want costumers to be able to add a product to their favourites, view their favourite products, remove a product from their favourites so that they can easily find products they previously liked and purchase them again with ease.

1. As a customer I can add a product to my list of favourite products so that I can easily find it later.
2. As a customer I can view my list of favourite products so that I can see what I have saved.
3. As a customer I can remove a product from my list of favourite products so that I can keep my list up to date.

**Epic: Store Information**

As a Store Owner I want to provide all necessary information about the company and its policies to the customers so that they can make informed decisions and trust our brand.

1. As a customer I can view the company's basic information such as its name, address, and contact details so that I can reach out to the company for any queries or issues.
2. As a customer I can view the store policies such as shipping, return, and refund policy so that I can make informed decisions before making a purchase.
3. As a customer I want to be informed when an error occurs while navigating the website, so that I can understand what happened and how to proceed.
4. As a store owner I want to provide all necessary information about the company and its policies to the customers so that they can make informed decisions and trust our brand.

**Epic: News Section & SEO Optimization**

As a Store Owner I want to create a news section and optimize it for SEO so that I can improve my website's search engine ranking and drive more organic traffic to my site.

1. As a customer I can subscribe to the newsletter so that I can stay updated on the latest news and promotions from the shop.
2. As a customer I can read articles related to babies such as new products, tips, and other relevant topics on the shop's website so that I can learn and stay informed about baby care.
3. As a store owner I want my website to appear at the top of the search results when potential customers search for personalised baby products, so that I can attract more organic traffic and increase sales.

**Epic: Documentation**

As a developer I can create a README documentation for the e-commerce website that I have built using Django so that it will serve as a guide for potential users of the website, providing them with a clear understanding of the website's purpose, features, and functionality.

[Back to top](#mi-primera-cajita)

## Design

The colour scheme for the design of the website is based in warn nature colours.

![Image Colours](/static/testing/palette.png)

### Flow Diagram

![Flow diagram](static/testing/diagram.png)

The flow chart above, created with the website [Lucid chart](https://lucid.app/), provides a simplified overview of what I was trying to accomplish.

[Back to top](#mi-primera-cajita)

## Web Marketing Strategy

This app was built using insights gained from the Design Thinking phase, keyword research, SEO, XML sitemap, robots.txt file, MailChimp, and Facebook as part of our web marketing strategy. These specific features were introduced to enhance the marketing of our business.

### Search Engine Optimisation (SEO)

As an e-commerce website, our users need to find personalized baby products easily and quickly. To meet those needs, we provide a user-friendly interface that allows them to browse and filter our products based on their preferences. We also offer detailed product descriptions, images, and customer reviews to help users make informed decisions.

To make the information easy to understand, we use simple language and clear visuals. We also organize our products into categories and provide filters to help users narrow down their search.

To demonstrate expertise, authoritativeness, and trustworthiness, we include information about our company and team, as well as any certifications or awards we have received. We also make sure to use accurate and up-to-date information throughout our website.

There are opportunities to link back to other pages within our own site, such as related products or product bundles. We can also link to external websites that already rank highly on Google, such as parenting blogs or baby product review websites.
To help users discover other relevant parts of our web application, we include related products, recommended products, and product bundles on our product pages. We also have a search bar and navigation menu that allow users to explore our website more easily.

**_Short-tail and long-tail keywords_**

- Personalised baby products
- Pacifier cords
- Teethers
- Bibs
- Muslins
- Baby gifts
- New-born essentials
- Baby shower gifts
- Newborn baby accessories
- Customisable baby products
- Pacifier clips
- Bibs and burp cloths
- Teething toys
- Muslin blankets
- Baby product storage
- Unique baby products
- Handmade baby products
- Baby product safety

[Back to top](#mi-primera-cajita)

### Web Marketing

- Users:

As an e-commerce shop selling personalised baby products, the users of this website are likely to be parents, expecting parents, family members and friends of parents, or anyone looking for a unique and personalized gift for a newborn baby.

- Online platforms:

It is common for these types of e-commerce shops to find a lot of their users on popular online platforms such as search engines like Google, social media sites like Facebook and Instagram, and marketplaces like Amazon and eBay.

- Social media users:

Social media platforms can be effective for reaching and engaging with potential customers. The specific social media platforms that the users of this e-commerce shop might use can depend on various factors such as demographics, interests, and location. It is recommended for the e-commerce shop to conduct market research to identify the social media platforms that their target audience is most active on and develop a social media strategy to reach and engage with them.

- User's needs:

The users may need information about the products, their features, and usage guidelines. They may also need help with choosing the right product for their needs, as well as assistance with the ordering and delivery process.

One way to meet these needs is by providing high-quality product descriptions, including images and videos that showcase the products' features and benefits. Additionally, creating informative blog posts, tutorials, and frequently asked questions (FAQs) can help users make informed decisions and provide solutions to their problems.

To deliver this content to the users, the e-commerce shop could create a blog section on its website and share posts on social media platforms. The website could also have a prominent "Help" or "Support" section that provides information on frequently asked questions and ordering and delivery processes.

Email marketing campaigns could also be used to deliver useful content to users who have subscribed to the shop's mailing list. The emails could include product updates, promotions, and helpful tips and guides.

Overall, the key is to create content that is informative, engaging, and easy to understand, and to make it easily accessible to users through multiple channels.

- Running sales or offer discounts:

Running sales and offering discounts can be an effective way to attract and retain customers. To inform our users about these offers, we’ll consider using various marketing channels such as email marketing, social media, and pop-up notifications on our website. We’ll also offer exclusive discounts to subscribers of our email list or followers on social media platforms to encourage them to engage with our brand and stay updated on promotions.

- Business goals:

As an e-commerce business, the goals of this business include increasing sales, generating brand awareness, and building customer loyalty. Some marketing strategies that will help meet these goals include:

1. Search Engine Optimization (SEO): By optimizing the website's content and structure for search engines, the business can increase its visibility in search results and attract more traffic to the website.

2. Pay-Per-Click Advertising (PPC): Using platforms like Google Ads or Facebook Ads, the business can create targeted ads that reach potential customers based on their demographics, interests, and behaviours.

3. Social Media Marketing: By creating and sharing engaging content on social media platforms like Instagram and Facebook, the business can build a following and connect with potential customers.

4. Email Marketing: By building an email list of subscribers and sending regular newsletters and promotions, the business can keep its brand top-of-mind and encourage repeat purchases.

5. Influencer Marketing: Partnering with influencers in the baby and parenting niche can help the business reach a wider audience and generate buzz around its products.

- Business budget:

It's possible that this business might need to work with free or low-cost options to market itself, especially if it has a limited marketing budget. There are many effective ways to market a business without spending a lot of money, such as social media marketing, email marketing, content marketing, influencer marketing, and search engine optimization (SEO). By focusing on these strategies and creating high-quality, engaging content that resonates with their target audience, this business can effectively market itself and grow its customer base without breaking the bank.

[Back to top](#mi-primera-cajita)

### XML Sitemap

The website App includes a sitemap file containing a list of important URLs. This file helps search engine spiderbots crawl the business website quickly and retrieve all relevant content.

The sitemap file was created using [XML-Sitemaps.com](https://www.xml-sitemaps.com/).

### Robots

The robots.txt file was implemented to guide search engine spider bots on which parts of the website to avoid, leading to better site quality and ultimately improving our SEO rating. We received assistance in setting up this feature from Walkthrough Boutique Ado.

## Testing

Throughout the development of the app, testing was conducted to identify and rectify any bugs that may have been present. Manual testing was performed on all aspects of the app, and responsiveness was tested using Dev Tools. Particular attention was paid to the app's appearance and user experience.

### Manual Testing

During the development of this app, manual testing was carried out for all epics/user stories. The header, main navigation, and footer were tested on all pages throughout the app. Additionally, various features were tested, including toast pop-ups, verification requests, and sending/receiving verification emails. These features were demonstrated with images to showcase the successful manual testing.

#### Header

<details>
  <summary>Top navbar: Logo, Search, Account and Bag</summary>

| **Feature**      | **Expect**                   | **Action**             | **Pass/Fail** |
| ---------------- | ---------------------------- | ---------------------- | ------------- |
| Logo             | Go to Home page              | Click on               | &check;       |
| Search Bar       | Searching for products       | Type and click / enter | &check;       |
| My Account       | Drop down                    | Click on               | &check;       |
| Account Register | Go to Sign up Page           | Click on               | &check;       |
| Account Login    | Go to Sign in Page           | Click on               | &check;       |
| Add Product      | Go to Add Product Page       | Click on               | &check;       |
| Add News         | Go to Add Article Page       | Click on               | &check;       |
| My Profile       | Go to Profile Page           | Click on               | &check;       |
| My Favourites    | Go to My Favourites Page     | Click on               | &check;       |
| Account Logout   | Go to Logout Page            | Click on               | &check;       |
| Bag              | Go to Shopping Bag           | Type and click / enter | &check;       |
| Bag Amount       | Show 0 or different amount € | Click on               | &check;       |

</details>

<details>
  <summary>Navbar main Menu</summary>

| Feature                      | Expect                                    | Action   | Pass/Fail |
| ---------------------------- | ----------------------------------------- | -------- | --------- |
| All Products                 | Drop down                                 | Click on | &check;   |
| By Price                     | Display All Products Page By Price        | Click on | &check;   |
| By Category                  | Display All Products Page By Category     | Click on | &check;   |
| All Products                 | Go to All Products Page                   | Click on | &check;   |
| Muslins                      | Drop down                                 | Click on | &check;   |
| Cotton Muslins               | Display Cotton Muslins only               | Click on | &check;   |
| Cotton & Bamboo Muslins      | Display Cotton & Bamboo Muslins only      | Click on | &check;   |
| Premium Soft Muslins         | Display Premium Soft Muslins only         | Click on | &check;   |
| All muslins                  | Go to All Muslins Page                    | Click on | &check;   |
| Pacifier Chains              | Drop down                                 | Click on | &check;   |
| Mini pacifier chains         | Display Mini pacifier chains only         | Click on | &check;   |
| Personalised pacifier chains | Display Personalised pacifier chains only | Click on | &check;   |
| Pacifier holder case         | Display Pacifier holder case only         | Click on | &check;   |
| All pacifiers                | Go to All Pacifiers Page                  | Click on | &check;   |
| Teethers                     | Drop down                                 | Click on | &check;   |
| Stroller Chain Teethers      | Display Stroller Chain Teethers only      | Click on | &check;   |
| Teether Toy Figures          | Display Teether Toy Figures only          | Click on | &check;   |
| All Teethers                 | Go to All Teethers Page                   | Click on | &check;   |
| More Pretty Things           | Drop down                                 | Click on | &check;   |
| Bibs                         | Display Bibs only                         | Click on | &check;   |
| Breasfeeding Necklaces       | Display Breasfeeding Necklaces only       | Click on | &check;   |
| Personalised Keyrings        | Display Personalised Keyrings only        | Click on | &check;   |
| Bracelets                    | Display Bracelets only                    | Click on | &check;   |
| All Pretty Things            | Go to All Pretty Things Page              | Click on | &check;   |
| About                        | Drop down                                 | Click on | &check;   |
| News                         | Go to News Page                           | Click on | &check;   |
| About Us                     | Go to About Us Page                       | Click on | &check;   |
| Contact Us                   | Go to Contact Us Page                     | Click on | &check;   |
| Privacy Policy               | Go to Privacy Policy Page                 | Click on | &check;   |
| Cookie Policy                | Go to Cookie Policy Page                  | Click on | &check;   |
| Terms                        | Go to Terms Page                          | Click on | &check;   |
| Faqs                         | Go to Faqs Page                           | Click on | &check;   |

</details>

#### Account

<details>
  <summary>Register</summary>

| Feature               | Expect                             | Action   | Pass/Fail |
| --------------------- | ---------------------------------- | -------- | --------- |
| Register              | Go to Sign Up Page                 | Click On | &check;   |
| Sign Up Form          | Input Fields                       | Type     | &check;   |
| Input Fields          | Valid / Filled required            | Warning  | &check;   |
| Sign Up button        | Submits Sign Up Form               | Click on | &check;   |
| Success Toast Message | Displays after submitting the form | Toast    | &check;   |
| Back to Login button  | Go to Login Page                   | Click on | &check;   |

</details>

<details>
  <summary>Login</summary>

| Feature               | Expect                             | Action   | Pass/Fail |
| --------------------- | ---------------------------------- | -------- | --------- |
| Login                 | Go to Sign In Page                 | Click On | &check;   |
| Sign In Form          | Input Fields                       | Type     | &check;   |
| Input Fields          | Valid / Filled required            | Warning  | &check;   |
| Remember Me           | Remembers Log In Details           | Tick Box | &check;   |
| Home button           | Go to Home Page                    | Click on | &check;   |
| Sign In button        | Submits Sign Up Form               | Click on | &check;   |
| Success Toast Message | Displays after submitting the form | Toast    | &check;   |
| Forgot Password       | Go to Password Reset Page          | Click on | &check;   |

</details>

<details>
  <summary>Password Reset</summary>

| Feature                  | Expect                      | Action   | Pass/Fail |
| ------------------------ | --------------------------- | -------- | --------- |
| Password Reset Form      | Input Fields                | Type     | &check;   |
| Input Fields             | Valid / Filled required     | Warning  | &check;   |
| Back to Login button     | Go back to Login Page       | Click on | &check;   |
| Reset My Password button | Submits Password Reset Form | Click on | &check;   |

</details>

<details>
  <summary>Logout</summary>

| Feature               | Expect                                  | Action   | Pass/Fail |
| --------------------- | --------------------------------------- | -------- | --------- |
| Logout                | Go to Sign Out Page                     | Click on | &check;   |
| Cancel button         | Go to Home Page                         | Click on | &check;   |
| Sign Out button       | Log out of Account                      | Click on | &check;   |
| Success Toast Message | Displays after clicking Sign Out Button | Toast    | &check;   |

</details>

<details>
  <summary>My Profile</summary>

| Feature                           | Expect                                            | Action   | Pass/Fail |
| --------------------------------- | ------------------------------------------------- | -------- | --------- |
| Default Delivery Information Form | Input Information                                 | Type     | &check;   |
| Country Drop down bar             | Drop down arrow shows Countries                   | Click on | &check;   |
| Update Information button         | Submits Updated Information                       | Click on | &check;   |
| Success Toast Message             | Displays after clicking Update Information Button | Toast    | &check;   |

</details>

#### Footer

<details>
  <summary>Follow Us</summary>

| Feature        | Expect               | Action   | Pass/Fail  |
|----------------|----------------------|----------|------------|
| Facebook Icon  | Link open in new tab | Click on | &check;    |
| Twitter Icon   | Link open in new tab | Click on | &check;    |
| Instagram Icon | Link open in new tab | Click on | &check;    |
| YouTube Icon   | Link open in new tab | Click on | &check;    |

</details>

<details>
  <summary>Subscribe - Mail Chimp</summary>

| Feature              | Expect                                 | Action   | Pass/Fail |
| -------------------- | -------------------------------------- | -------- | --------- |
| Email Address        | Input email address                    | Type     | &check;   |
| Subscribe Button     | Click to submit form                   | Click on | &check;   |
| Mail Chimp image     | Link in new tab                        | Click on | &check;   |
| Subscription message | Shows thank you message after clicking | -        | &check;   |
| MailChimp            | Receive a welcome email                | Click on | &check;   |

</details>

<details>
  <summary>Footer menu</summary>

| Feature            | Expect                       | Action   | Pass/Fail |
| ------------------ | ---------------------------- | -------- | --------- |
| Muslins            | Go to All Muslins Page       | Click on | &check;   |
| Pacifiers          | Go to All Pacifiers Page     | Click on | &check;   |
| Teethers           | Go to All Teethers Page      | Click on | &check;   |
| More Pretty Things | Go to All Pretty Things Page | Click on | &check;   |
| All Products       | Go to All Products Page      | Click on | &check;   |
| Account Register   | Go to Sign up Page           | Click on | &check;   |
| Account Login      | Go to Sign in Page           | Click on | &check;   |
| Add Product        | Go to Add Product Page       | Click on | &check;   |
| Add News Article   | Go to Add Article Page       | Click on | &check;   |
| My Profile         | Go to Profile Page           | Click on | &check;   |
| My Favourites      | Go to My Favourites Page     | Click on | &check;   |
| Account Logout     | Go to Logout Page            | Click on | &check;   |
| About Us           | Go to About Us Page          | Click on | &check;   |
| Contact Us         | Go to Contact Us Page        | Click on | &check;   |
| Privacy Policy     | Go to Privacy Policy Page    | Click on | &check;   |
| Cookie Policy      | Go to Cookie Policy Page     | Click on | &check;   |
| Terms              | Go to Terms Page             | Click on | &check;   |
| Faqs               | Go to Faqs Page              | Click on | &check;   |

</details>

<details>
  <summary>All pages</summary>
  
| Feature                  | Expect            | Action   | Pass/Fail |
|--------------------------|-------------------|----------|-----------|
| Back to Top Arrow Button | Go to top of page | Click on | &check;   |

</details>

#### Home

<details>
  <summary>Home</summary>

| Feature                 | Expect                          | Action   | Pass/Fail |
| ----------------------- | ------------------------------- | -------- | --------- |
| 3 Image Carousel        | Moves through images            | -        | &check;   |
| Arrow Controls          | Moves through images manually   | Click on | &check;   |
| Shop Now Button         | Go to All Products Page         | Click on | &check;   |
| Categories Links        | Go to clicked Products category | Click on | &check;   |
| Latest Articles Cards   | Go to clicked Article           | Click on | &check;   |
| Read More Articles link | Go to News                      | Click on | &check;   |

</details>

#### All Products

<details>
  <summary>All Products</summary>

| Feature                               | Expect                                   | Action   | Pass/Fail |
| ------------------------------------- | ---------------------------------------- | -------- | --------- |
| By Price / By Category / All Products | Display Products by selected option      | Click on | &check;   |
| Number of products                    | Displayed on All Product Pages           | -        | &check;   |
| Sort By Bar                           | Select from Drop down menu               | Click on | &check;   |
| Price, (Low to High)                  | Display Products by Price, (Low to High) | Click on | &check;   |
| Price, (High to Low)                  | Display Products by Price, (High to Low) | Click on | &check;   |
| Name (A - Z)                          | Display Products by Name (A - Z)         | Click on | &check;   |
| Name ( Z- A)                          | Display Products by Name ( Z- A)         | Click on | &check;   |
| Category (A - Z)                      | Display Products by Category (A - Z)     | Click on | &check;   |
| Category ( Z- A)                      | Display Products by Category ( Z- A)     | Click on | &check;   |

</details>

<details>
  <summary>Products Cards</summary>

| Feature       | Expect                                  | Action   | Pass/Fail |
| ------------- | --------------------------------------- | -------- | --------- |
| Products Card | Go to product detail page               | Click on | &check;   |
| Category Tag  | View all products in that Category Page | Click on | &check;   |
| Edit Button   | Go to Edit Product Page - Admin Only    | Click on | &check;   |
| Delete Button | Go to Delete Product Page - Admin Only  | Click on | &check;   |

</details>


#### Product Detail

<details>
  <summary>Products Detail</summary>

| Feature                    | Expect                                               | Action   | Pass/Fail |
| -------------------------- | ---------------------------------------------------- | -------- | --------- |
| Category Tag               | View all Products in that Category Page              | Click on | &check;   |
| Favourites icon            | Add/delete favourite to My Favourites page           | Click on | &check;    |
| Colour                     | Drop down arrow selector                             | Click on | &check;   |
| Quantity Selector Add      | Add Number of Item Qty                               | Click on | &check;   |
| Quantity Selector Subtract | Subtract Number of Item Qty                          | Click on | &check;   |
| Keep Shopping Button       | Go to All Products page                              | Click on | &check;   |
| Add to Cart Button         | Adds the Item to the Shopping Cart.                  | Click on | &check;   |
| Success Toast              | Displays On Clicking the Add to Cart Btn             | Toast    | &check;   |
| Secure Checkout Button     | Goes to Shopping Cart Page -Success Pop Up           | Click on | &check;   |
| Leave A Review -Logged Out | No Access Message Displayed                          | -        | &check;   |
| Login Here Button          | Goes to Login Page                                   | Click on | &check;   |
| Leave A Review - Logged In | Input Field                                          | Type     | &check;   |
| Rating - Logged In         | Use Stars to Rate Color Change                       | Click on | &check;   |
| Submit Button              | Submits Review & Rating                              | Click on | &check;   |
| Cancel Button              | Clears Review Input & Star Rating                    | Click on | &check;   |
| Customer Reviews           | Shows 0 if None                                      | -        | &check;   |
| Customer Displayed         | Shows Name of Reviewer, Date & Time, Review & Rating | -        | &check;   |
| Edit Button                | Goes to Edit Reivew Page - Only Reviewer             | Click on | &check;   |
| Delete Button              | Goes to Delete Review Page - Only Reviewer           | Click on | &check;    |

</details>

<details>
  <summary>Reviews</summary>

| Feature                  | Expect                               | Action   | Pass/Fail |
| ------------------------ | ------------------------------------ | -------- | --------- |
| Edit Review Input Field  | Type Update of Review in             | Type     | &check;   |
| Edit Rating              | Adjust Rating using stars            | Click on | &check;   |
| Return to Product Button | Returns to the smae Product / Review | Click on | &check;   |
| Update Button            | Updates the Review                   | Click on | &check;   |
| Delete Review            | No changes can be made               | Click on | &check;   |

</details>

#### Shopping Bag

<details>
  <summary>Shopping Bag</summary>
  
| Feature                    | Expect                                               | Action   | Pass/Fail  |
|----------------------------|------------------------------------------------------|----------|------------|
| Qty control bar            | Add or Subtract up & down Qty toggle                 | Click on | &check;    |
| Qty - Button               | Subtract Product Qty                                 | Click on | &check;    |
| Qty + Button               | Add Product Qty                                      | Click on | &check;    |
| Update                     | Updates Qty Cahnges made                             | Click on | &check;    |
| Remove                     | Removes Product from Shopping Cart                   | Click on | &check;    |
| Keep Shopping Button       | Go to All Products Page                              | Click on | &check;    |
| Secure Checkout Button     | Go to Secure Checkout Page                           | Click on | &check;    |

</details>

#### Secure Check Out

<details>
  <summary>Secure Check Out</summary>

| Feature                     | Expect                                | Action   | Pass/Fail |
| --------------------------- | ------------------------------------- | -------- | --------- |
| Order From                  | Type In Details                       | Type     | ✔         |
| Save delivery information   | Saves delivery information to profile | Tick Box | ✔         |
| Payment Input Field         | Input Card Validates if Correct       | Type     | ✔         |
| Adjust Shopping Cart Button | Goes to Shopping Cart Page            | Click on | &check;   |
| Complete Order Button       | Processes the Order & Payment         | Click on | &check;   |

</details>

#### Products pages

<details>
  <summary>Products pages</summary>

| Feature                      | Expect                                             | Action   | Pass/Fail |
| ---------------------------- | -------------------------------------------------- | -------- | --------- |
| Cotton Muslins               | Display Cotton Muslins Products only               | Click on | &check;   |
| Cotton & Bamboo Muslins      | Display Cotton & Bamboo Muslins Products only      | Click on | &check;   |
| Premium Soft Muslins         | Display Premium Soft Muslins Products only         | Click on | &check;   |
| All pacifiers                | Display All Muslins Page                           | Click on | &check;   |
| Mini pacifier chains         | Display Mini pacifier chains Products only         | Click on | &check;   |
| Personalised pacifier chains | Display Personalised pacifier chains Products only | Click on | &check;   |
| Pacifier holder case         | Display Pacifier holder case Products only         | Click on | &check;   |
| All pacifiers                | Display All Pacifiers Page                         | Click on | &check;   |
| Stroller Chain Teethers      | Display Stroller Chain Teethers only               | Click on | &check;   |
| Teether Toy Figures          | Display Teether Toy Figures only                   | Click on | &check;   |
| All Teethers                 | Display All Teethers Page                          | Click on | &check;   |
| Bibs                         | Display Bibs only                                  | Click on | &check;   |
| Breasfeeding Necklaces       | Display Breasfeeding Necklaces only                | Click on | &check;   |
| Personalised Keyrings        | Display Personalised Keyrings only                 | Click on | &check;   |
| Bracelets                    | Display Bracelets only                             | Click on | &check;   |
| All Pretty Things            | Display All Pretty Things Page                     | Click on | &check;   |

</details>

#### News

<details>
  <summary>News</summary>

| Feature          | Expect                                   | Action   | Pass/Fail |
| ---------------- | ---------------------------------------- | -------- | --------- |
| Image Card       | Go to Article page                       | Click on | &check;   |
| Read More Button | Go to Article page                       | Click on | &check;   |
| Edit Button      | Goes to Edit Article page - Admin only   | Click on | &check;   |
| Delete Button    | Goes to Delete Article page - Admin only | Click on | &check;   |

</details>

<details>
  <summary>Article details</summary>

| Feature             | Expect                               | Action   | Pass/Fail |
| ------------------- | ------------------------------------ | -------- | --------- |
| Back to News Button | Go to News page                      | Click on | &check;   |
| Edit Button         | Go to Edit Article page - Admin only | Click on | &check;   |
| Delete Button       | Go to News page - Admin only         | Click on | &check;   |

</details>

#### About Pages

<details>
  <summary>About Pages</summary>

| Feature        | Expect                      | Action   | Pass/Fail |
| ------------------- | -----------------------| -------- | --------- |
| News           | Display News Page           | Click on | &check;   |
| About Us       | Display About Us Page       | Click on | &check;   |
| Contact Us     | Display Contact Us Page     | Click on | &check;   |
| Privacy Policy | Display Privacy Policy Page | Click on | &check;   |
| Cookie Policy  | Display Cookie Policy Page  | Click on | &check;   |
| Terms          | Display Terms Page          | Click on | &check;   |
| Faqs           | Display Faqs Page           | Click on | &check;   |

</details>

#### Contact Us Page

<details>
  <summary>Contact Us</summary>

| Feature       | Expect                  | Action   | Pass/Fail |
| ------------- | ----------------------- | -------- | --------- |
| Contact form  | Fill in form            | Type     | &check;   |
| Submit Button | Submit the Contact form | Click on | &check;   |
| Cancel Button | Go to Home page         | Click on | &check;   |

</details>

#### Faqs Page

<details>
  <summary>Faqs</summary>

| Feature            | Expect               | Action   | Pass/Fail |
| ------------------ | -------------------- | -------- | --------- |
| Accordion question | Click reveals answer | Click on | &check;   |
| Accordion question | Click hides answer   | Click on | &check;   |

</details>

#### Admin Control Front End

<details>
  <summary>Add Product</summary>

| Feature          | Expect                          | Action   | Pass/Fail |
| ---------------- | ------------------------------- | -------- | --------- |
| Add Category     | Select from Drop Down use arrow | Click on | &check;   |
| Add Product Form | Type in fields                  | Type     | &check;   |
| Colour           | Select from drop down           | Click on | &check;   |
| Cancel Button    | Go to All Products Page         | Click on | &check;   |
| Add Product      | Submit Form to add Product      | Click on | &check;   |

</details>

<details>
  <summary>Edit Product</summary>

| Feature           | Expect                          | Action   | Pass/Fail |
| ----------------- | ------------------------------- | -------- | --------- |
| Edit Category     | Select from Drop Down use arrow | Click on | &check;   |
| Edit Product Form | Edit fields                     | Type     | &check;   |
| Edit Colour       | Select from drop down           | Click on | &check;   |
| Cancel Button     | Go to All Products Page         | Click on | &check;   |
| Add Product       | Submit Form to add Product      | Click on | &check;   |

</details>

<details>
  <summary>Delete Product</summary>

| Feature        | Expect                  | Action   | Pass/Fail |
| -------------- | ----------------------- | -------- | --------- |
| Cancel Button  | Go to All Products Page | Click on | &check;   |
| Delete Product | Delete Product          | Click on | &check;   |

</details>

<details>
  <summary>Add News Article</summary>

| Feature           | Expect                     | Action   | Pass/Fail |
| ----------------- | -------------------------- | -------- | --------- |
| Add Article Form  | Add Title and content      | Type     | &check;   |
| Choose File Image | Add Image                  | Click on | &check;   |
| Cancel Button     | Go to News Page            | Click on | &check;   |
| Add Article       | Submit form to add article | Click on | &check;   |

</details>

<details>
  <summary>Edit News Article</summary>

| Feature           | Expect                        | Action    | Pass/Fail |
| ----------------- | ----------------------------- | --------- | --------- |
| Edit Article Form | Edit Title and content        | Type      | &check;   |
| Clear             | Remove current Image          | Check Box | &check;   |
| Choose File Image | Add Image                     | Click on  | &check;   |
| Cancel Button     | Go to News Page               | Click on  | &check;   |
| Update Article    | Submit form to update article | Click on  | &check;   |

</details>

<details>
  <summary>Delete News Article</summary>

| Feature        | Expect          | Action   | Pass/Fail |
| -------------- | --------------- | -------- | --------- |
| Cancel Button  | Go to News Page | Click on | &check;   |
| Delete Article | Delete Article  | Click on | &check;   |

</details>

### Validator Testing

#### HTML - W3C Html Validator

<details>
  <summary>No Errors Found</summary>

![W3C Html Validator](W3C_Html_Validator.jpg)

</details>

#### CSS - W3C CSS Validator

<details>
  <summary>No Errors Found</summary>

![W3C Css Validator](W3C_Css_Validator.jpg)

</details>

#### Python - Pep8ci CI Python Linter

<details>
  <summary>No Errors Found</summary>

![Pep8ci CI Python Linter](python_inter.jpg)

</details>

#### Lighthouse

<details>
  <summary>Lighthouse</summary>

![Lighthouse](lighthouse.jpg)

</details>

### Bugs to fix

- Retrieving a Product detail page shows a 500 error sometimes.
- Adding a product occasionally shows an error.
- Mobile responsiveness needs improvement on certain pages.
- Fix rating system to show in all products page.


[Back to top](#mi-primera-cajita)

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
- [Amazon AWS](https://aws.amazon.com/): To host static and media files for the site.
- [Lucid chart](https://www.lucidchart.com/): Used to make a flow diagram to help with the logic & flow of the code.
- [Balsamiq](https://balsamiq.com/): To create wireframes for the project.
- [Am I Responsive?](https://ui.dev/amiresponsive): To ensure the project looked good across all devices.
- [Favicon](https://favicon.io/favicon-converter/) - To create the favicon icon.

[Back to top](#mi-primera-cajita)

## Deployment

This project was deployed using

- Github - To store code and deploy the site.
- ElephantSql.com - To create an external database.
- Django and Heroku - To host the deployed project.
- Amazon AWS - To host the static and media files.

### GitHub

To create a new repository, I took the following steps:

1. Logged into GitHub.
2. Click the ‘repositories’ section.
3. Click the green ‘new’ button to create new repository.
4. Choose ‘repository template’ Used the code institute template as recommended from the dropdown menu.
5. Add repository name then clicked the green ‘create repository button’ at the bottom of the page.
6. Open the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

### ElephantSql

Setting up ElephantSQL:

1. Access your ElephantSQL dashboard by logging in to ElephantSQL.com.
2. Click on "Create New Instance".
3. Set up your plan by giving it a name (usually the name of your project), selecting the Tiny Turtle (Free) plan, and leaving the Tags field blank.
4. Click on "Select Region" and then click on "Review".
5. Check your details and then click on "Create instance".
6. Go back to the ElephantSQL dashboard and click on the name of the database instance for your project.
7. To copy the database URL to your clipboard, click on the copy icon in the URL section.

### Django and Heroku

To set up the Django framework and configure the Heroku deployment, I followed these step-by-step instructions:

1. Installed Django framework and revisited the Walkthrough provided by Code institutes for assistance.
2. Logged into Heroku, went to the Dashboard and clicked on New to create a new app.
3. Gave the app a name, selected the region closest to me, and clicked Create app to confirm.
4. Opened the Settings tab and added the config var DATABASE_URL, and for the value, copied in the database URL from ElephantSQL.
5. Installed dj_database_url and psycopg2 in the terminal, both of which are required to connect to an external database.
6. Updated the requirements.txt file with the newly installed packages using pip freeze > requirements.txt.
7. Imported dj_database_url in the settings.py file and updated the DATABASES section with the new connection to the ElephantSQL database.
8. Ran the showmigrations command in the terminal to confirm the connection to the external database.
9. Migrated the database models to the new database using python3 manage.py migrate command.
10. Loaded in the fixtures in the correct order: categories first and then products.
11. Created a superuser for the new database using python3 manage.py createsuperuser command.
12. Deleted the database from the settings.py file to prevent exposing it when pushing to GitHub and reconnected to the local sqlite database.
13. Deployed the final version with DEBUG = 'DEVELOPMENT' in os.environ.

Note: For safety and security reasons, I generated a new Django secret key using a Django key generator and added it to both the env.py file and Heroku config vars. This ensured that even if the secret key had been pushed accidentally to GitHub, it would now be an invalid key.

### Amazon AWS

- #### Setting up Amazon AWS

To set up Amazon AWS, the following steps were taken (following the Code Institute walkthroughs to assist in setting up Amazon AWS):

1.  Log into Amazon AWS and signed in to the upper right by accessing the AWS management console under my account.
2.  Navigate to the Storage menu under All Services and clicked the link that says S3.
3.  Click the orange button that says 'Create Bucket'.
4.  Name the bucket and selected the closest region to me.
5.  Follow the [steps](https://codeinstitute.s3.amazonaws.com/fullstack/AWS%20changes%20sheet.pdf) supplied by the Code Institute for Object Ownership.

- #### Connecting Django to S3

To connect Django to S3, the following steps were taken:

1.  Install the `Boto3` and `Django storages` packages by running the following commands:

    `pip3 install boto3`

    `pip3 install django-storages`

2.  Run the following command to save the installed packages to the `requirements.txt` file:

    `pip3 freeze > requirements.txt`

3.  Add 'storages' to the installed apps section inside the `settings.py` file.

4.  Add some additional settings to the same file to let Django know what bucket it's communicating with:
    - Near the bottom of the file, write an `if` statement to check if there is an environment variable called `USE_AWS` and add the following code inside:

```
if USE_AWS in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```

5.  Add the following config vars in Heroku:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - USE_AWS set to True
6.  Remove the `DISABLE_COLLECTSTATIC` variable in Heroku.
7.  Go to the `settings.py` file in my Django project and add the following line inside the `if` statement written earlier:

    `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`

8.  Create a custom_storages.py file and import my settings as well as the s3boto3 storage.
9.  Add the following two classes inside the `custom_storages.py` file:

```
class StaticStorage(S3Boto3Storage):
	location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
	location = settings.MEDIAFILES_LOCATION
```

10. In the `settings.py` file, underneath the bucket config settings but still inside the `if` statement, add the following lines:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
```

11. Override and explicitly set the URLs for static and media files using my custom domain and new locations. Add the following two lines inside the same if statement:

```
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

12. After pushing the changes, the S3 bucket has a static folder with all the static files inside.

- #### Caching, Media Files & Stripe

To set up caching, media files, and Stripe, the following steps were taken:

1.  Open your `settings.py` file and add an `if` statement to handle media files caching. This allows static files to be cached for a long time and speeds up the loading of your site. Here's the code to add:

```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

2.  Save your changes to `settings.py`, then add, commit, and push your changes to Git.
3.  Log in to your Amazon AWS account and navigate to your S3 bucket. Create a new folder called "media" and save it.
4.  Inside the new "media" folder, click "Upload," "Add files," and select all of the images you're using on your site. Note that your media folder must match the media folder within your Workspace gitpod.io.
5.  Under "Permissions," select "Grant public-read access" and click Upload. You may also need to check an acknowledgement warning checkbox.
6.  With those steps completed, all of your static and media files should automatically link from Django to your S3 bucket.
7.  In the Django admin, confirm the email address for the superuser in the Postgres database. This is necessary for the user to log in to the store.
8.  Add your Stripe keys to the Heroku Config Vars.
9.  Sign in to your Stripe account and navigate to the "Developers" tab at the top right of the navbar.
10. Under "Developers," click "Webhooks," then "Add endpoint" in the side-nav.

11. On the next page, enter the link to your Heroku app followed by `/checkout/wh/`. It should look something like this:

`https://your-app-name.herokuapp.com/checkout/wh/`

12. Click "+ Select events" and check the "Select all events" checkbox at the top. Then click "Add events" at the bottom to complete the form.

13. Your webhook is now created, and it should have generated a secret key. You'll need this to add to your Heroku config vars.

14. Navigate to your app in Heroku and go to the "Config Vars" section under settings. You'll need the secret key you generated for your webhook, as well as your publishable key and secret key that you can find in the API keys section in Stripe.

15. Add these values under these keys:

```
STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
STRIPE_SECRET_KEY = 'insert your secret key'
STRIPE_WH_SECRET = 'insert your webhooks secret key'
```

16. Finally, go back to your `settings.py` file in Django and insert the following near the bottom of the file:

```
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```

With these steps completed, you should be all set with caching, media files, and Stripe integration for your Django project.

[Back to top](#mi-primera-cajita)

### How to Fork it

1. On GitHub, go to [CarmenCantudo/mi-primera-cajita](https://github.com/CarmenCantudo/mi-primera-cajita).
2. In the top right, click "Fork".

### How to Clone it

1. Go to the main page of the repository.
2. Above the file list, click "Code".
3. Select HTTPS, SSH, or GitHub CLI and then click copy to clone it.
4. Open Git Bash.
5. Change the location of your cloned repository.
6. Type `git clone` and then paste the URL you copied.
7. Press “Enter” to create your clone.

### Making a Local Clone

1. Locate the [Repository](https://github.com/CarmenCantudo/mi-primera-cajita).
2. Click "Code".
3. Click Clone or Download.
4. Copy the Git URL from the dialogue box.
5. Open a terminal window in your chosen directory using your preferred development editor.
6. Change the location to where you want the cloned directory to be.
7. Type `git clone`, and then paste the URL you copied.
8. Press Enter, and your local clone will be created.

[Back to top](#mi-primera-cajita)

## Credits

Resources used in the process of the "My First Box" website design and build:

- [Code Institute](https://codeinstitute.net/ie/) walkthrough projects.
- [Stack Overflow](https://stackoverflow.com/): Help with general questions.
- Boutique Ado Code Institute project.
- Images from [Freepik](https://www.freepik.com/).
- No image icon from [Flaticon](https://www.flaticon.com/free-icon/image_467857?k=1679858790030)
- [Slack community](https://slack.com).
- [Django Documentation](https://docs.djangoproject.com/en/4.1/).
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/).
- [Privacy Policy](https://www.freeprivacypolicy.com/live/b8cc74ed-4388-46c3-81c5-fc710ec5a780)
- [Terms and Conditions](https://www.termsandconditionsgenerator.com/download.php?lang=en&token=7PXp6g2qp1dRm45czvyNyDfaUaczzJe7)
- [Cookies Policy](https://www.freeprivacypolicy.com/live/9a7d89d6-d6a7-42ee-81d8-051fe47b47ff)
- [XML-Sitemaps](https://www.xml-sitemaps.com/details-mi-primera-cajita.herokuapp.com-2d88e4e2b.html)

[Back to top](#mi-primera-cajita)
