# Django-Blog Portfolio Project 4

## Welcome to the Django Blog App!

🚀 Elevate your blogging experience with our dynamic and user-friendly Django-powered blog platform. Whether you're a content creator or a tech enthusiast, our app empowers you to craft, manage, and share your ideas effortlessly. Dive into the world of modern web development and showcase your content with style. Let's make blogging exciting again! 🌐✨

![Responsive](media/images/Responsive.png)

**[View the live project here.](https://djangobblog-4328bed47b45.herokuapp.com/)**

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [User Stories](#user-stories)


    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
    * [Navigation](#Navigation-bar)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [add your pages](#)
    * [Login page](#profile-page)
    * [Sign up page](#signup-page)

3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgment](#acknowledgment)

## Design & Planning:

### User Stories
First-time Visitor:
- As a first-time visitor, I want to easily understand the purpose of the blog site.
- As a first-time visitor, I want to navigate the site easily and find a list of recent blog posts.
- As a first-time visitor, I want to view individual blog posts with a clear layout and readable content.
- As a first-time visitor, I want the option to sign up for an account to engage more with the site.


#### Registered User:
- As a registered user, I want to log in to my account securely.
- As a registered user, I want a personalized dashboard displaying my profile information.
- As a registered user, I want to create, edit, or delete my own blog posts.
- As a registered user, I want to be able to comment on blog posts and interact with other users.
- As a registered user, I want to customize my profile settings and preferences.


#### Site Owner:
- As a site owner, I want to have administrative access to manage all aspects of the blog.
- As a site owner, I want to be able to create, edit, or delete any blog post on the site.
- As a site owner, I want to have access to user analytics and engagement metrics.
- As a site owner, I want the ability to moderate and manage user comments and interactions.
- As a site owner, I want to customize the overall look and feel of the blog site.

### Desktop Wireframes

![Homepage](media/images/Home%20Page.png)

![Login Page](media/images/Login%20Page.png)

![Dashboard Page](media/images/Dashboard%20Page.png)

![Category page](media/images/Categories%20Page.png)

![Users Page](media/images/Users%20Page.png)

![All Posts](media/images/Post%20Page.png)

### Mobile Wireframes
![Mobile](media/images/Mobile%20Wireframes.png)

### Agile Methodology

Explain agile approach to your project (itterations, user stories, tasks,acceptance criteria, labels, story points...) and insert screenshoots of your Kanban board 

### Typography

Explain font you've used for your project

### Colour Scheme

![Screenshot](media/images/coolors.png)

### DataBase Diagram
Image of the database diagram for your project, you can name your database models as well and how they are connected

## Features:

## This section outlines the key features and functionalities of the Django Blog app.

### 1. User Authentication
   - Users can create accounts, log in, and log out securely.
   - Passwords are hashed for security.

### 2. CRUD Operations for Blog Posts
   - **Create:** Authors can create new blog posts.
   - **Read:** Users can view published blog posts.
   - **Update:** Authors can edit and update existing posts.
   - **Delete:** Authors can delete posts they created.

### 3. Navigation Bar
   - User-friendly navigation bar for easy access to different sections of the app such as Sports, Politics, Technology, Business, Science, Health and Featured Cars.

   - Dynamic links to categories, and other relevant pages.

### 4. Footer
   - Informative footer providing links to important pages, contact information, etc.

### 5. Login Page
   - Secure login page with validation checks.
   - Remember me and forgot password functionality for enhanced user experience.

### 6. Sign Up Page
   - User-friendly registration page with necessary form fields.

### 7. 404 Page
   - Customized 404 page for a better user experience.
   - Helpful error messages and suggestions for lost users.

### 8. Categories 
   - Organize posts by assigning categories.
   - Users can easily filter content based on categories.

### 9. Commenting System
   - Readers can leave comments on blog posts.

### 10. Responsive Design
   - The app is built with a responsive design, ensuring a seamless experience across devices.

### 11. Search Functionality
   - Users can search for specific posts using a robust search feature.

### 12. Social Media Integration
   - Added Social Media links

### 13. Featured Post
   - Highlight a selected post as the "Featured Post" on the homepage.
   - Attract attention to specific content or announcements.

### 14. Recent Articles
   - Display a section showcasing the most recent blog articles.
   - Allow users to stay updated on the latest content.

## Technologies Used
- [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq) was used to create the wireframes.
- [LucidChart](https://www.lucidchart.com/pages/) was used to design the database schema.
- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the mark up.
- [CSS](https://en.wikipedia.org/wiki/CSS)  was used to style the site.
- [Django](https://www.djangoproject.com/) was the framework that was used.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), django is a python framework.
- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) was also used to style the site.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for interactiveness.
- [Gitpod](https://www.gitpod.io/about) was used to create this site and then push everything to github.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) is used to host this site.
- [Github](https://en.wikipedia.org/wiki/GitHub) was used to store the code.
- [Git](https://en.wikipedia.org/wiki/Git) was used for version control.
- [Cloudinary](https://cloudinary.com/) was used to store the images.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the database.
- [Grammarly](https://app.grammarly.com/) was used to check typography.

## Testing
Important part of your README!!!

### Google's Lighthouse Performance
### Desktop

![Desktop Screenshot](media/images/Lighthouse%20Desktop.png)

### Mobile

![Mobile Screenshot](media/images/Lighthouse%20Mobile.png)

### Browser Compatibility
Check compatability with different browsers (Firefox, Edge, Chrome)

### Responsiveness
Screenshots of the responsivness, pick few devices

### Code Validation
Validate your code HTML, CSS, JS & Python (Validate all your templates, static files, views, forms, models, urls), display screenshots

### Manual Testing user stories
Test all your user stories, you an create table 
User Story |  Test | Pass
--- | --- | :---:
paste here you user story | what is visible to the user and what action they should perform | &check;
- attach screenshot

### Manual Testing features
Test all your features, you can use the same approach 
| Status | feature
|:-------:|:--------|
| &check; | description
- attach screenshot

### Automated testing
If you created automated tests, insert screenshoots of your coverage and number of tests

## Bugs
List of bugs and how did you fix them, you can create simple table
| Bug | Fix
|:-------:|:--------|
|   |    |

## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database On ElephantSQL
- Log into the [ElephantSQL](https://www.elephantsql.com/) website and click **Create new Instance**
- Enter a **Name** and keep the plan as **Tiny Turtle Free**, then **tags** field can be left blank, Select a region closest to you, I selected **EU-West-1(Ireland)** as I'm in Ireland. Then click **Review** and afterward click **create an instance**.
- On The Dashboard click on your database instance name.
- You will see the details for your database instance, in the URL section click on the copy icon to copy the database URL.
- Head over to gitpod and create a **Database URL** environment variable in your env.py file and set it equal to the copied URL.

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.
## Credits
List of used resources for your website (text, images, snippets of code, projects....)
## Acknowledgment

- I would like to thank Juliaa Konovalova for being my guiding light in the world of Django. Your expertise and encouragement have made this coding journey an incredible experience. I am sincerely grateful for your mentorship 😊.

- I would like to thank Code Institutes Slack Community, and tutor support (Especially Joanne) as this helped me so much when I got stuck on part of my project.

- I would also like to thank our cohort facilitator Marko, for answering any course-related questions I asked and for providing us with weekly guidance information about the project

- I would also like to express my gratitude to my fellow colleagues John, Angus who helped me with debugging and also for general advices. 

[def]: media/images/coolors.png