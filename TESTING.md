# Testing

Return back to the [README.md](README.md) file.

I've run a lot of tests throughout the project's development to make sure the website functions properly. All of the site's testing are documented in this area.

## Code Validation

I have validated all of my code using the recommended tools for each language.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.


| Index | 
![screenshot](documentation/testing/html/index.png) 
Pass: No Errors 

| All Products |
 ![screenshot](documentation/testing/html/all_products.png) 
Pass: No Errors 

| Individual Product | 
![screenshot](documentation/testing/html/Product_detail.png) 
Pass: No Errors

| Contact|
![screenshot](documentation/testing/html/contact_page.png) 
Pass: No Errors

| Journal | 
![screenshot](documentation/testing/html/Journal.png) 
Pass: No Errors 

| Journal Post | 
![screenshot](documentation/testing/html/journal_post.png) 
**Error**: The  `font`  element is obsolete.  [ Found late in submission process to return and fix ]

| Register | 
![screenshot](documentation/testing/html/Register.png)
Pass: No Errors 

| Login |
![screenshot](documentation/testing/html/login.png) 
Pass: No Errors

| Log Out | 
![screenshot](documentation/testing/html-validation-logout.png) 
Pass: No Errors

| Checkout Bag | 
![screenshot](documentation/testing/html/checkout_bag.png)
Pass: No Errors

Checkout Bag | 
![screenshot](documentation/testing/html/Checkout_bag_no_item.png) 
Pass: No Errors |

| Checkout | 
![screenshot](documentation/testing/html/Checkout_spinner_error.png)
 Warning: Empty heading (Loading spinner after submitting checkout form)

| Checkout Success
![screenshot](documentation/testing/html/Checkout_success.png)
Pass: No Errors

| Profile | 
![screenshot](documentation/testing/html/profile_page.png) 
Pass: No Errors

| Add Product  |
![screenshot](documentation/testing/html/add_product.png) 
Pass: No Errors

| Edit Product  |
![screenshot](documentation/testing/html/edit_product.png) 
Error: An img element must have an alt attribute, except under certain conditions (Current image for product being edited)

| Delete Product  
![screenshot](documentation/testing/html/Delete_blog.png) 
Pass: No Errors

| Add Blog |
![screenshot](documentation/testing/html/add_blog_post.png)
Multiple Errors all from summernote widget for blog content field

| Edit Blog |
![screenshot](documentation/testing/html/edit_blog.png)
Multiple Errors all from summernote widget for blog content field

| Delete Blog |
![screenshot](documentation/testing/html/Delete_blog.png) 
Pass: No Errors 

| Contact us | 
![screenshot](documentation/testing/html/contact_page.png)
Pass: No Errors 

| Contact us Success |
![screenshot](documentation/testing/html/contact_success.png) 
Pass: No Errors

| Reviews |
![screenshot](documentation/testing/html/review_page.png) 
Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Base.css | 
[screenshot](documentation/testing/css/basecss.png) | Pass: No Errors |

| checkout.css |
![screenshot](documentation/testing/css/checkoutcss.png) | Pass: No Errors |

| profile.css | 
![screenshot](documentation/testing/css/profilecss.png) | Pass: No Errors |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| countryfields.js | ![screenshot](documentation/testing/js/countryselect.png) | Pass: No Errors |
| add_product.html | ![screenshot](documentation/testing/js/add_product_js.png) | Pass: No Errors |
| edit_product.html| ![screenshot](documentation/testing/js/edit_product_js.png) | Pass: No Errors |
| products.html | ![screenshot](documentation/testing/js/productsjs.png) | Pass: No Errors |
| bag.html ![screenshot](documentation/testing/js/bagjs.png) | Pass: No Errors |
| quantity_input_script.html | ![screenshot](documentation/testing/js/quantity_input_script_js.png) | Pass: No Errors |
| stripe_elements.js | ![screenshot](documentation/testing/js/stripe_elementsjs.png) | Undefined Stripe variable |