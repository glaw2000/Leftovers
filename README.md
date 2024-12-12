# Title 
Live site link : https://leftovers-app-32aa0915dd0b.herokuapp.com/


## Overview
This is a full stack application that stores and presents blog posts, ingredient information, user like numbers, user details and user comments. This site was developed using a django framework for a capstone project during a Full Stack Development Bootcamp run by Code Institute. 

### Purpose
The purpose of this blog is to provide readers with advice, ideas and inspiration for what to do with leftover food to help cut down on food waste and save people money. It is not intended to be a recipe site.

## User Stories

### Must-Have User Stories
**User Management:**<br/>
As the site administrator I want to be able to grant, modify or delete user accounts so that I can manage access to the site.</br>
**Acceptance Criteria:**
- Admin is able to add users
- Admin is able to delete users
- Admin is able to grant different levels of rights to users
<pre></pre>

**Author Submission of Posts:**<br/>
As the author of the blog I want to submit posts so that I can share my tips and ideas with others about what to do with leftover food in an attempt to reduce food waste.</br>
**Acceptance Criteria:**
- Author can post to the site and include photos if required
- Author's posts can be viewed by anyone
<pre></pre>

**Author Edit and Delete Posts**<br/>
As the author I want to be able to update or delete posts so that I can control the content of my blog</br>
**Acceptance Criteria:**
- Author can edit and delete posts
<pre></pre>

**View All Posts:**<br/>
As a general site user I want to view the blog posts with ease so that I can find inspiration on what to do with leftover food without frustration or confusion.</br>
**Acceptance Criteria:**
- Home page presented to user for them to click through to a listing of all posts
- From post listings, user can choose a post to read in full
- Site is consistent with in-built navigation links
- Site is responsive on all devices
<pre></pre>

**View Post by Leftover Type:**<br/>
As a user I want to view the blog posts by food category so that I can filter the view of posts to only those relevant to the leftovers I have.</br>
**Acceptance Criteria:**
- User can select a food type from the home page to take them to a list of all posts related to that food type
<pre></pre>

**User Add Comments:**<br/>
As a registered user I want to be able to submit comments about posts so that I can interact with the author and share my thoughts and ideas with other users</br>
**Acceptance Criteria:**
- A logged in user has the option to comment on each post
- A logged in user can see the comments they have made below each post
- A logged in user can see if their comment has been approved for display to all
<pre></pre>

**User View Comments:**<br/>
As a registered user I want to be able to view peoples' comments about posts so that I can read their thoughts and ideas about posts</br>
**Acceptance Criteria:**
- A logged in user is able to see all approved comments under each post
<pre></pre>

**Author Reply to Comments:**<br/>
As the author of the blog I want to be able to reply to users comments so that they feel a connection to the blog and myself</br>
**Acceptance Criteria:**
- author can reply to comments on posts by leaving and author written comment.
<pre></pre> 

**Manage Comments:**<br/>
As the site administrator I want to be able to manage user comment submissions so that quality of the site content is maintained</br>
**Acceptance Criteria:**
- Admin can accept or reject comment submissions from users
- Admin can create, edit and delete comments
- Only the user that has written the comment can view that comment in 'draft' state
- All users can only view comments by other members once they have been approved by the site admin and published.
<pre></pre>

**Branding:**<br/>
As the author of the blog I want to present a cohesive and consistent designed site so that I can build a brand that is recognisable to my audience.</br>
**Acceptance Criteria:**
- Blog has consistent layouts between pages, consistent design elements and writing style.
- Blog reflects author's passion of using up leftover food and avoiding waste.
<pre></pre>

### Should-Have User Stories
**Like Posts:**<br/>
As a registered user I want to be able to give a thumbs up to a post so that I can show my liking of a post </br>
**Acceptance Criteria:**
- A logged in user is able to click on a thumbs up icon next to each post to show they like it
<pre></pre>

**User Feedback:**<br/>
As the author of the blog I want to receive feedback on my posts so that I can proactively improve and tailor my content to appeal to my audience.</br>
**Acceptance Criteria:**
- Users can leave comments on author's posts
- Users can show if they like a post
- A count of likes next to each post
<pre></pre>

**Bookmark Posts:**<br/>
As a registered users I want to bookmark my favourite posts so that I can easily access specific posts of interest to me </br>
**Acceptance Criteria:**
- A logged in user has the option to bookmark each post
- A logged in user can see all their bookmarked posts listed in once place
<pre></pre>

**Remove Bookmarks:**<br/>
As a registered users I want to to be able to remove bookmarks so that I can manage my bookmarked list of posts </br>
**Acceptance Criteria:**
- A logged in user has the option to remove their bookmark from any previously bookmarked post
<pre></pre>

**About Author:**<br/>
As the author of the blog I want to have an area of the site that tells the readers about who I am and why I set up the blog so that my audience can feel connected to my blog.</br>
**Acceptance Criteria:**
- About section in the site that has information about the author their passion of the blog subject.
- Place for photo of the author
<pre></pre>

**User Edit of Comments:**<br/>
As a registered users I want to be able to edit comments I have made about posts so that I can manage my interactions with the author and other users</br>
**Acceptance Criteria:**
- A logged in user is able to edit their comments they have made on posts
- A logged in user is able to see their edited comment below the post
- Approved edited comments can be viewed by all users
<pre></pre>

**User Deletion of Comments:**<br/>
As a registered user I want to be able to delete a comment I have made about posts so that I can manage my interactions with the author and other users </br>
**Acceptance Criteria:**
- A logged in user is able to delete their comments they have made on posts 
<pre></pre>


### Could-Have User Stories
**View Posts by Meal Type:**<br/>
As a user I want to view the blog posts by meal type so that I can filter the view of posts by the meal I want to prepare. </br>
**Acceptance Criteria:**
- User can select a meal type (eg breakfast/lunch/dinner/snacks....) to present them with a list of all posts related to that meal type
<pre></pre>

**Sort Port Listing View:**<br/>
As a user I want to be able to sort the listing of posts by certain criteria so that I can find posts I'm interested in quicker</br>
**Acceptance Criteria:**
- A user is able to sort posts by date created on
- A user is able to sort posts by date updated on
- A user is able to sort posts by most liked
- A user is able to sort posts by what is currently trending ie most viewed in a current time range

### Won't-Have User Stories
**Community board:**<br/>
As a registered user I want to be able to post onto a community board within the site so that I and other users can share thoughts, ideas and experiences with regards to leftovers and the blog.</br>
**Acceptance Criteria:**
- An area in the site where registered users can post text and photos to.
- An area in the site where registered users can read posts by other users
<pre></pre>

**Video content:**<br/>
As the blog author I want to be able to add videos to my posts so that I can share step by step videos showing how I use up leftovers  </br>
**Acceptance Criteria:**
- Author is able to upload video to each blog post they create
- Users are able to watch videos embedded in the blog posts
<pre></pre>

**Social Sharing:**<br/>
As a user I want to be able to to click on social media buttons for each post so that I can easily share posts across platforms like Pinterest, Instagram and Facebook  </br>
**Acceptance Criteria:**
- Have social media buttons under/next to each post
- User can click on a posts social media button and it will allow them to re-post the blog post on their feed.
<pre></pre>

**Post Rating:**<br/>
As a user I want to **be able to rate a post ** so that I can share my view of how good a post is with others  </br>
**Acceptance Criteria:**
- Start rating system of 1-5 can be selected by user next to each post
- Other users and the author are able to see an average star rating next to each post
<pre></pre>

**Search Posts:**<br/>
As a registered user I want to **be able to search all posts ** so that I can easily find posts relevant to me</br>
**Acceptance Criteria:**
- A logged in user is able to enter a string into a search box and search all posts
- A logged in user will receive a lists of post results relevant to their search
<pre></pre>

**Share posts:**<br/>
As a registered user I want to share posts so that I can send posts to my contacts that may interest them  </br>
**Acceptance Criteria:**
- A logged in user has the option to share any post with their contacts
- A logged in user receives confirmation that the post they shared has been sent to the contacts they chose 
<pre></pre>

## Design Decisions

### Wireframes
I wanted the design of this site to be visually impactful but simple to navigate and not over complicated. 

Designed mobile first and with the idea of using flex boxes so that the display would scale responsively. The following wireframes show the initial design idea:
![picture alt](/documentation/wireframes/home_page.png)
![picture alt](/documentation/wireframes/listings_page.png)
![picture alt](/documentation/wireframes/post_page.png)
![picture alt](/documentation/wireframes/about_page.png)

The login, logout and register pages were going to be handled by allauth so these were not drafted out as wirefranes. Once created in the app I just updated the colours of the text and buttons to match my chosen colour theme.

During development and testing I realised that the images and text were too cramped when presented in a 3 x 3 layout. The 3 x 3 layout worked well on desktops and laptops so I used a media query to change the display to be a column of 1 on smaller devices. 

The colour theme of blue and yellow was chosen because the yellow is bright and cheerful and makes an impact and the blue is a great contrasting colour that meets accessibility requirements. No tool was used to generate the theme.

### Accessibility Considerations
Colours were tested through lighthouse for accessibility. 
All images have aria labels and buttons and menus have been given roles so screenreaders can intrpret these elements.

## Features Implementation

### Core Features (Must-Haves User Stories)

**User Management:**<br/>
Implemented - the site administrator can grant, modify or delete user accounts using the admin dashboard</br>

**Author Submission of Posts:**<br/>
Implemented - using the admin dashboard the author of the blog can post to the site with images and these posts can be viewed by anyone.

**Author Edit and Delete Posts**<br/>
Implemented - using the admin dashboard the author of the blog site can update or delete posts</br>

**View All Posts:**<br/>
Implemented - a general site user can view the blog posts. The Home page is presented to user for them to click through to a listing of all posts. From post listings, user can choose a post to read in full. The site is consistent with inbuilt navigation links and is responsive on all devices.

**View Poast by Leftover Type:**<br/>
Implemented - a user can select a food type from the home page to take them to a list of all posts related to that food type.

**User Add Comments:**<br/>
Implemented - a logged in user has the option to comment on each post; see the comments they have made below each post and see if their comment has been approved for display to all.

**User View Comments:**<br/>
Implemented - a registered users is able to see all approved comments under each post.

**Author Reply to Comments:**<br/>
Implemented - the author can reply to comments on posts by leaving a written comment when logged in.

**Manage Comments:**<br/>
Implemented - an admin user can accept or reject comment submissions from user and create, edit and delete comments. Only the user that has written the comment can view that comment in 'draft' state. All users can only view comments by other members once they have been approved by the site admin and published.

**Branding:**<br/>
Implemented -  the Blog has consistent layouts between pages, consistent design elements and writing style and reflects author's passion of using up leftover food and avoiding waste as detailed on the About page.

### Optional Features (Should-Have User Stories)

**Like Posts:**<br/>
Implemented - a registered user is able to click on a thumbs up icon next to each post to show they like it.

**User Feedback:**<br/>
Implemented -  the author can receive feedback on posts through users being able to 
leave comments and show if they like a post. A count of user likes next to each post can also be seen by the author. 

**About Author:**<br/>
Implemented - About section in the site has information about the author their passion of the blog subject. There is place for a photo of the author.

**User Edit of Comments:**<br/>
Implemented - a logged in user is able to edit their comments they have made on posts and see their edited comment below the post. Approved edited comments can be viewed by all users.

**User Deletion of Comments:**<br/>
Implemented a logged in user is able to delete their comments they have made on posts. 

### Optional Features (Could-Have User Stories)
**View Posts by Meal Type:** 
Partially implemented 
Although it may seem odd to partially implement a could have user story before all the should haves user stories, the reason for doing this was two fold. To avoid future corruption of the database by adding a new field into the post model at a later date when it became populated. The backend table to enable this feature has been implemented as has the field in the Post model. In a future dev cycle it would not take much effort to use this information in the front for the user to filter posts by (like is currently offered for by ingredient). Secondly, the work to get this set up in the backend was so similar to the work done for the filter by ingredient type user story that it was extremely 'doable' in the time given for this dev cycle. Starting the bookmark user stories, which really would need both to be implemented for a good user experience, would not have got finished in the time available.

## Testing and Validation

### Testing Results
Manual testing ......

Screen responsive testing ..... 

Issues were faced with .....

Manual test results 
- Title of test - pass / fail



- Responsiveness was tested thoughout using chrome dev tools which enabled me to view the site on different devices as well as by specific width and height viewport settings.
- Accessibility Testing - Please see a snippet of the WAVE report below:
![picture alt](documentation/test%20results/WAVE%20Summary.png)
![picture alt](documentation/test%20results/WAVE%20Details.png)<br>
I chose to ignore the two redundant link alerts which were concerning the links to the home page from both the logo and the title in the top heading bar of my page. I want users to be able to get back to the home page if they click either of these. 
Initially when I ran wave I incurred the error shown below. This was because in both my nav sections I had multiple nav items setting aria-current to page. By introducing an if statement check on the request.path this error was resovled.
![picture alt](documentation/test%20results/WAVE%20error%20Screenshot%202024-12-11%20103555.png)  

 

### Validation
All validation result screenshots are in the following folder: [test results](/documentation/test%20results/)
 of this repository and summarised below:

- Using https://validator.w3.org/#validate_by_input each of the template pages I had created or updated was validated. I incurred one error on the post_detail page due to the text of the blog post input in the text editor by the blog post author was causing the validator to think there were an uneven number of opening and closing p tags. This was resolved on advice from a peer on the course (thanks Ricky Smithson) by placing my post.content template variable inside my div directly and not within p tags.</br>
I incurred one warning about the aria label for the like button on the post_detail page. This has remained unresolved after trying several combinations to describe the thumbs up button a user can press on a post. The label is a succinct and descriptive as I could think of. 
Home page (landing.html) validation
![picture alt](/documentation/test%20results/HTML%20Validation%20of%20page.png)
All Posts (blog.html) page validation
![picture alt](/documentation/test%20results/HTML%20Validation%20of%20All%20Posts%20page.png)
Post (post_detail.html) page validation with Error
![picture alt](/documentation/test%20results/Error%20Waning%20HTML%20validation%20post_detail%20page.png)
Post (post_detail.html) page validation with Error resolved
![picture alt](/documentation/test%20results/Error%20resolved%20HTML%20validation%20post_detail%20page.png)


- Using https://jigsaw.w3.org/css-validator/ the styles.css file was validated. The same Error was seen 4 times due to using setting font-optical-sizing: auto. I removed the setting of font-optical-sizing: auto; from these items and problem was resolved. 
![picture alt](/documentation/test%20results/CSS%20Validator%20Result.png)

- Using https://jshint.com/ both the comments.js and the likes.js files were validated and passed. The validator called out that the variable postSlug was not set in the likes.js file. This varible was actually set in the post_detail.html file using inline script tags before calling the likes.js script as it was the only way I could get the feature to work.
![picture alt](/documentation/test%20results/likes%20js%20file%20-%20jshint%20report.png)
![picture alt](/documentation/test%20results/comments%20js%20file%20-%20jshint%20report.png)

- Using https://pep8ci.herokuapp.com/  the Python files created or modified by myself were validated. All passed once the errors around either too much white space or not enough, and a few lines being too long, were resolved.

| Feature | admin.py | forms.py | models.py | urls.py | views.py |
|---------|----------|----------|-----------|---------|----------|
| config  | na | na | na | [no errors](documentation/test%20results/config%20urls%20py%20file%20validated.png) | na |
| landing | na | na | na | [no errors](documentation/test%20results/landing%20urls%20py%20file%20validated.png) | [no errors](documentation/test%20results/landing%20views%20py%20file%20validated.png) |
| about | na  | na  | na | [no errors](documentation/test%20results/about%20urls%20py%20file%20validated.png) | [no errors](documentation/test%20results/about%20views%20py%20file%20validated.png) | 
| blog | [no errors](documentation/test%20results/blog%20admin%20py%20file%20validated.png) | [no errors](documentation/test%20results/blog%20forms%20py%20file%20validated.png) | [no errors](documentation/test%20results/blog%20models%20py%20file%20validated.png) | [no errors](documentation/test%20results/blog%20urls%20py%20file%20validated.png) | [no errors](documentation/test%20results/blog%20views%20py%20file%20re-validated%20after%20redirect%20added.png) |




- Dev tools lighthouse report summary :



## Deployment

### Deployment Process

  
## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

## Django Project Setup

1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject config .```
4. Create a new app eg. ```python3 mangage.py startapp blog```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'blog',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfromPostgreSQL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn config.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```
## PostgreSQL

A new database instance can be created on PostgreSQL from Code Institute (https://dbs.ci-dbs.net/) for your project. 

- Enter CodeInstitute student email address and submit
- Retrieve the database URL value from the email generated
- Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


## Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   - **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['8000-glaw2000-leftovers-lajp76mi6xk.ws.codeinstitute-ide.net', 'leftovers-app-32aa0915dd0b.herokuapp.com'].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose '**Manual**' deployment method and click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project.

## Reflection on Development Process

### Successes
A working MVP at the end of the dev cycle. 
Completing all the must have user stories. 
Getting some of the should have user stories developed. 
Working through bugs and finding solutions. 

### Challenges
Time. Trying to achieve the must have user stories and associated documentation in the time given was challenging. 


### Final Thoughts
This was great practice of working through a sw dev cycle to deliver an MVP in a set amount of time. Just like in the real world, there are always more user stories than you have time to develop in a single dev cycle. By focussing on the must haves it was possible to achieve a working site.  


## Credits
- README headings copied from a previous student hackathon (https://joanne1980.github.io/Name-the-animal/) that I worked on in a team. Original template created by Brian O Grady (github Mrbrianojee), Programme Director at Code Institute.
- Deployment details in README were copied and adapted from a past project created by Code Institute facilitator Amy Richardson (https://freefido.herokuapp.com/)
- Code Institute course materials and trainers - especially Amy Richardson, John Rearden and Mark Briscoe.
- https:djecrety.ir was used to generate a secret key
- pixaby.com for free vectors and images
- convertio.co for image compression
- google fonts for Roberto mono font used throughout the site
- https://validator.w3.org/#validate_by_input  for validating html
- https://jigsaw.w3.org/css-validator/ for validating css
- https://jshint.com/ for validating java script 
- https://pep8ci.herokuapp.com/ Python linter to validate code
- Chrome Dev tools lighthouse for testing performance and accessibility of site
- https://wave.webaim.org/ to test accessibility of site


## Future Improvements
### Fixes
- Fix Image sizing of images. All images were converted to webp and compressed but the light house report suggests this is an area where further improvement could be made. The css styling if the image elements could be improved too.
- Fix the aria label on the post like button. Several variations were tried but nothing that the HTML validator liked.

### Enhancements
Having trending post information on the landing page could be a nice future enhancement based on the like count that is already implemented.<br>
I would also like to change the way the user comments work. If a user makes a comment and it gets approved the comment is visible to all. It the user then clicks to edit that comment, regardless of if they make any changes to it or not, the comment automatically goes back into an un approved state and is removed from view to everyone other than the user who wrote it and admin. It would be nice to leave the original on screen. 
The following non implemented user stories could be developed in future dev cycles:
- Add and Remove Bookmarks of posts
- View Posts by Meal Type
- Sort capability for viewing post listings
- Community board
- Capability for author to upload Video content to posts
- Capability for users to share posts via social media or with their contacts
- Capability for users to rate posts on a scale 1 -5
- Capability to be able to search for certain posts<br>


