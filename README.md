Intro
Creating a full stack ecomm site for a spectacle frame retailer

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
3. (12-18) checkout / stripe
4. (19 - 25) profiles deploy / journal / contact us
5. (26 - 2) style / readme / ecomm / robots / fb page / tidy submit

landing page images
https://www.pexels.com/photo/two-clear-eyeglasses-with-gray-frames-1493112/
https://www.pexels.com/photo/portrait-photo-of-woman-in-yellow-turtleneck-sweater-and-eyeglasses-in-front-of-blue-background-3765124/
https://www.pexels.com/photo/stylish-eyeglasses-placed-on-beige-surface-4226877/

wireframe 
https://wireframepro.mockflow.com/editor.jsp?editor=on&publicid=Me55d7974c8b9921ba0e8317d6a0614db1697961926877&perm=Create&projectid=MxuLS39jMh&spaceid=MqwXAeI7Lpb&ptitle=p5%20-%20eyedeal&bgcolor=white&category=web&pcompany=C7b4955d147c64bb6990d17826f0d480e&space=MqwXAeI7Lpb#/page/188b81619924412797f2a96d32f9d838

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

https://elfsight.com/blog/how-to-create-recent-sales-notification-popup/#:~:text=The%20Recent%20Sales%20Notification%20popup,many%20e%2Dcommerce%20businesses%20nowadays.

Popup? 

credits
boutique ado project used a boilerplate
use bootstrap 4 https://getbootstrap.com/docs/4.6/getting-started/introduction/

design eyewear group https://designeyeweargroup.kontainer.com/folder/4250#token=s4lkLCrIra&type=direct
orgreen optics https://orgreenoptics.presscloud.com/digitalshowroom/#/gallery
Any product is used for educational purposes only

Generating sku codes
https://www.3dsellers.com/free-tools/sku-generator

https://releases.jquery.com/

django documentation - bag_tools


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

Cups of coffee = 26