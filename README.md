Intro
Creating a full stack ecomm site for a spectacle frame retailer

live link https://eye-deal-e27624539e49.herokuapp.com/

Milestones
Home
Registration
Products
Basket
Checkout
Payment
Profile
Admin
Reviews

1. Full CRUD
2. checkout functionality 
3. ui/ux updates
4. Finishing documentation, SEO, meta data, facebook page, 

CUSTOM MODELS (potentially):
contact us page
reviews
journal for site owner
wishlist for products?

sprints oct/nov 23
1. (29 - 4) product setup filter & sort - done
2. (5- 11) shopping bag - adding products - done
3. (12-18) checkout / stripe - done
4. (19 - 25) profiles deploy / journal / contact us
remember - mailchimp, meta descriptions, sitemap, robot.txt, 404 facebook mockup, favicon
5. (26 - 2) style / readme / ecomm / robots / fb page / tidy submit



landing page images
https://www.pexels.com/photo/two-clear-eyeglasses-with-gray-frames-1493112/
https://www.pexels.com/photo/portrait-photo-of-woman-in-yellow-turtleneck-sweater-and-eyeglasses-in-front-of-blue-background-3765124/
https://www.pexels.com/photo/stylish-eyeglasses-placed-on-beige-surface-4226877/

wireframe 
https://wireframepro.mockflow.com/editor.jsp?editor=on&publicid=Me55d7974c8b9921ba0e8317d6a0614db1697961926877&perm=Create&projectid=MxuLS39jMh&spaceid=MqwXAeI7Lpb&ptitle=p5%20-%20eyedeal&bgcolor=white&category=web&pcompany=C7b4955d147c64bb6990d17826f0d480e&space=MqwXAeI7Lpb#/page/188b81619924412797f2a96d32f9d838

Bootstrap Product List Carousel for Ecommerce Website
https://www.tutorialrepublic.com/snippets/preview.php?topic=bootstrap&file=product-list-carousel-for-ecommerce-website

Erd
import diagram

inital commit
setup all auth
setting up base.html
index.html

Ignoring adding sizes to products as majority of stock single pieces / handmade, one size available.
possibly return to add functionality later (adding products part 4)

CHANGE FONT FROM LATO to custom!
Merriweather chosen
"Meriweather is quite popular and one of the widely used brand fonts for websites. Especially for the e-commerce ones. Indeed, it is pleasant to look at because of its condensed letterforms. Also, it is ideal for font pairings. If you wish to have a high-end brand image, then Merriweather is the best fonts style for it!"
Taken from https://codetheorem.co/blogs/best-fonts-for-ecommerce-website

Bugs
Search bar returning products, not exactly correct?
removing male / female dropdown toggle as filtering not working on gender? return to fix, below code removed from header "for him" "for her"
        <li class="nav-item dropdown">
            <a class="logo-font font-weight-bold nav-link text-black mr-5" href="#" id="mens-link" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                For Him
            </a>
            <div class="dropdown-menu border-0" aria-labelledby="mens-link">
                <a href="{% url 'products' %}?category=Glasses&gender=Male" class="dropdown-item">Glasses</a>
                <a href="{% url 'products' %}?category=Male,Sunglasses" class="dropdown-item">Sunglasses</a>
                <a href="{% url 'products' %}?category=Male,Glasses,Sunglasses" class="dropdown-item">All Mens Frames</a>
            </div>
        </li>

I noticed you have a field for gender but also there is category class. (with thanks to Dayana for this one)
If gender is part of your product model then you will need to refine your products by gender instead of category. 
You could also create a separate class gender like a subcategory connected to your product and filter that way too


Bug - update number not reflecting in shopping bag, followed ado, number not reflecting items. return to fix!
Roman From Ci Tutor Team helped me spot this one!
value="{{ item.quantity }}" tou your increment/decrement form in bag.html

https://elfsight.com/blog/how-to-create-recent-sales-notification-popup/#:~:text=The%20Recent%20Sales%20Notification%20popup,many%20e%2Dcommerce%20businesses%20nowadays.

Popup? 

Bug - allauth login page not loading, after much searching and with help from the CI tutor support, clearing the cookies / cache helped to display the login page


env file setup - as per CI Tutor Roman
For setting env vars locally, we recommend setting them like this:
Create a file named env.py in the root directory of your project. This is the file you will use to define your environment variables.
If you don't have one already, create a file named .gitignore  in the root directory of your project.
 Next we need to stop git from pushing this file to github, and so keep your environment variables secret. To do this, open your .gitignore  file add the following text to it: env.py 
At the top of your env.py  file, you need to import os so that you can set the environment variables in the operating system. Once you have added the line “import os” underneath you can assign your environment variables using the following syntax: 
os.environ["Variable Name Here"] = "Value of Variable Goes Here" 
Example: os.environ["SECRET_KEY"] = "ohsosecret" 
Then the following code imports this new env.py file where you need to use your environment variables. For example your app.py file for flask project or settings.py file for Django project. Add this under your other imports at the top of the file. 
import os
if os.path.exists("env.py"):
  import env 
The if statement here is so that the env.py file is only pulled when working on your code in your workspace, not when it is deployed on heroku. For deployment you can set your environment variables in the heroku dashboard in settings > config vars.
Now that your environment variables have been set in your env.py file, and the file has been imported into your project, you can use them as needed using the following syntax: 
SECRET_KEY = os.environ.get('SECRET_KEY')
Make sure you save all your files before testing if it works.

bug - on mobile contact us success page hidden by navbar, return to fix



migration
Hi David, the only data that you really need to be concerned about is your products, Users should not be transferred over as this can lead to problems (I know this from debugging so many of these issues)

you can follow these steps for the app that you want to transfer the data over, if you have more than 1 app that you want to transfer over, then do them separately:

​﻿1. Make sure you are connected to the local Sqlite3 database in Gitpod.


​﻿2. Make a backup of the app's data that you want. For the example, we will use the "product" app.
﻿- (type this command, do not copy and paste):
﻿- python3 manage.py dumpdata products > products.json
​
​﻿3. Make sure you are connected to the online Postgres database in Heroku.


​﻿﻿4. Transfer the backup json file data that you just created.
﻿- (type this command, do not copy and paste):
﻿- python3 manage.py loaddata products.json
​﻿﻿5. Repeat for any other apps you wish to transfer.

credits
boutique ado project used a boilerplate
use bootstrap 4 https://getbootstrap.com/docs/4.6/getting-started/introduction/

design eyewear group https://designeyeweargroup.kontainer.com/folder/4250#token=s4lkLCrIra&type=direct

orgreen optics https://orgreenoptics.presscloud.com/digitalshowroom/#/gallery
Any product is used for educational purposes only

https://claritydev.net/blog/adding-a-blog-to-your-django-website
adding a blog

adding a contact us form 
https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid

building an image gallery with django
https://reintech.io/blog/building-image-gallery-in-django

https://unsplash.com/photos/silver-framed-eyeglasses-on-wooden-surface-KZa_RBuBLu4 
404 page image

https://www.pexels.com/photo/red-sunglasses-on-pink-surface-1532244/

journal / blog
https://github.com/adamgilroy22/retro-reboot/tree/main
CI I think therefore i blog

contact us form:
https://medium.com/@k.lancemeister/django-crispy-forms-cb6f97200299
https://www.youtube.com/watch?v=w4ilq6Zk-08

reviews
https://michaelstromer.nyc/books/intro-to-django/django-reviews

wishlist
https://data-flair.training/blogs/python-django-wishlist-app/

SEO keywords https://www.wordtracker.com/search

https://www.shapedivider.app/

adding wishlist to profile app
https://stackoverflow.com/questions/51230409/how-to-assign-userprofile-with-wishlist-without-using-a-default-user

Generating sku codes
https://www.3dsellers.com/free-tools/sku-generator

https://releases.jquery.com/

django key generator
https://miniwebtool.com/django-secret-key-generator/

xmlsitemap
https://www.xml-sitemaps.com/

django documentation - bag_tools

generating returns policy, privacy policy https://app.termsfeed.com/

on mail used for store email


https://cubitts.com/blogs/journal?TN - inspo for journal app

designing for the visually impaired / low vision
https://fuzzymath.com/blog/improve-accessibility-for-visually-impaired-users/

checklist taken with thanks from https://github.com/Shaga-Matula
## Tasks :
- [ ] <label><input type="checkbox" disabled /> Task 1 : ###############</label>
- [ ] <label><input type="checkbox" disabled /> Task 2 : ###############</label>
- [ ] <label><input type="checkbox" disabled /> Task 3 : ###############</label>
## Acceptance Criteria :
- [ ] <label><input type="checkbox" disabled /> Criteria 1 :  ############## </label>
- [ ] <label><input type="checkbox" disabled /> Criteria 1 :  ############## </label>


Been a day fixing this...  so dont fall into this one... its remove in shoping basket if you cut and paste you will get and error...  here is the fix..    bag.urls : path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
js code: var url = `/bag/remove/${itemId}/`;
My code:
bag.urls : path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
js code: let url = `remove/${itemId}/`;   - remove this part /bag/

Cups of coffee = 54