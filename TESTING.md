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


### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

# noqa was used where line breaks in strings would have broken Django functionality.


| Bag contexts.py |

![screenshot](documentation/testing/python/bag/contexts.png)

Pass: No Errors

| Bag urls.py |

![screenshot](documentation/testing/python/bag/urls.png)

Pass: No Errors

| Bag views.py |

![screenshot](documentation/testing/python/bag/views.png)

Pass: No Errors

| Journal admin.py | 

![screenshot](documentation/testing/python/journal/admin.png) 

Pass: No Errors

| Journal forms.py | 

![screenshot](documentation/testing/python/journal/forms.png) 

Pass: No Errors 

| Journal models.py |

![screenshot](documentation/testing/python/journal/models.png)

Pass: No Errors

| Journal urls.py |

![screenshot](documentation/testing/python/journal/urls.png)

Pass: No Errors

| Journal views.py |

![screenshot](documentation/testing/python/journal/views.png) 

Pass: No Errors


| Checkout admin.py |

![screenshot](documentation/testing/python/checkout/admin.png)

Pass: No Errors

| Checkout forms.py |

![screenshot](documentation/testing/python/checkout/forms.png) 

Pass: No Errors

| Checkout models.py |

![screenshot](documentation/testing/python/checkout/models.png)

Pass: No Errors


| Checkout signals.py |

![screenshot](documentation/testing/python/checkout/signals.png)

Pass: No Errors 


| Checkout urls.py |

![screenshot](documentation/testing/python/checkout/urls.png)

 Pass: No Errors


| Checkout views.py |

![screenshot](documentation/testing/python/checkout/views.png)

Pass: No Errors

| Checkout webhook_handler.py |

![screenshot](documentation/testing/python/checkout/webhook_handler.png)

 Pass: No Errors

| Checkout webhooks.py |

![screenshot](documentation/testing/python/checkout/webhooks.png) 

Pass: No Errors



| Contact admin.py |  ![screenshot](documentation/testing/python/contact/admin.png) | Pass: No Errors |
| Contact forms.py |  ![screenshot](documentation/testing/python/contact/forms.png) | Pass: No Errors |
| Contact models.py | ![screenshot](documentation/testing/python/contact/models.png) | Pass: No Errors |
| Contact urls.py |  ![screenshot](documentation/testing/python/contact/urls.png) | Pass: No Errors |
| Contact views.py |  ![screenshot](documentation/testing/python/contact/views.png) | Pass: No Errors |





| Reveiws admin.py | ![screenshot](documentation/testing/python/reviews/admin.png) | Pass: No Errors |
| Reviews Codes forms.py |  ![screenshot](documentation/testing/python/reviews/forms.png)  | Pass: No Errors |
| Reviews Codes models.py |  ![screenshot](documentation/testing/python/reviews/models.png)  | Pass: No Errors |
| Reviews Codes urls.py |  ![screenshot](documentation/testing/python/reviews/urls.png)  | Pass: No Errors |
| Reviews Codes Views.py |  ![screenshot](documentation/testing/python/reviews/views.png)  | Pass: No Errors |



| Home urls.py | ![screenshot](documentation/testing/python/home/urls.png)  | Pass: No Errors |
| Home views.py | ![screenshot](documentation/testing/python/home/views.png) | Pass: No Errors |





| Products admin.py | ![screenshot](documentation/testing/python/products/admin.png) | Pass: No Errors |
| Products forms.py | ![screenshot](documentation/testing/python/products/forms.png) | Pass: No Errors |
| Products models.py | ![screenshot](documentation/testing/python/products/models.png) | Pass: No Errors |
| Products urls.py |  ![screenshot](documentation/testing/python/products/urls.png) | Pass: No Errors |
| Products views.py |  ![screenshot](documentation/testing/python/products/views.png) | Pass: No Errors |
| Products widgets.py |  ![screenshot](documentation/testing/python/products/widgets.png) | Pass: No Errors |



| Profiles forms.py | ![screenshot](documentation/testing/python/profiles/forms.png) | Pass: No Errors |
| Profiles models.py | ![screenshot](documentation/testing/python/profiles/models.png) | Pass: No Errors |
| Profiles urls.py | ![screenshot](documentation/testing/python/profiles/urls.png) | Pass: No Errors |
| Profiles views.py | ![screenshot](documentation/testing/python/profiles/views.png) | Pass: No Errors |



| Project Level settings.py | ![screenshot](documentation/testing/python/project/settings.png) | Pass: No Errors |
| Project Level urls.py | ![screenshot](documentation/testing/python/project/urls.png) | Pass: No Errors |
| Project Level views.py | ![screenshot](documentation/testing/python/project/views.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on Chrome and firefox browsers to check for compatibility issues.

| Browser | Notes |
| --- | --- |
| Chrome | Works as expected |
| Firefox | Works as expected |


### Responsiveness

I tested for responsiveness on many different sized viewports from 320px wide up to Ultrawide resolutions, and using different hardware (Monitors, Laptops, Phones).

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.
Performance needs to be improved but I will note I had quite a bit of slow down and internet outages during testing 

Home | Desktop
![screenshot](documentation/testing/lighthouse/index_desktop.png)

Home | Mobile
![screenshot](documentation/testing/lighthouse/index_mobile.png)

All Products | Desktop
![screenshot](documentation/testing/lighthouse/products_desktop.png)

All Products | Mobile
![screenshot](documentation/testing/lighthouse/products_mobile.png)

Product Detail | Desktop
![screenshot](documentation/testing/lighthouse/productdetail.png)

Product Detail | Mobile
![screenshot](documentation/testing/lighthouse/productdetailmob.png)

Contact | Desktop
![screenshot](documentation/testing/lighthouse/contact_us_desk.png)

Contact | Mobile  
![screenshot](documentation/testing/lighthouse/contact_us_mobile.png)

Blog | Desktop 
![screenshot](documentation/testing/lighthouse/journal_desktop.png)

Blog | Mobile
![screenshot](documentation/testing/lighthouse/journal_mobile.png)

Reviews | Desktop 
![screenshot](documentation/testing/lighthouse/reviews_desk.png)


Reviews | Mobile
![screenshot](documentation/testing/lighthouse/reviews_mobile.png)

